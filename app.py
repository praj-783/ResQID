from flask import Flask, request, render_template, url_for
import uuid
import qrcode
import os
import sqlite3

app = Flask(__name__, static_folder="static")

# ---------- CONFIG ----------
# 1. ADDED: Your secret password for disabling/enabling IDs
ADMIN_SECRET = "my-super-secret-password-123" 

DB_NAME = "users.db"
QR_FOLDER = os.path.join(app.static_folder, "qrcodes")
os.makedirs(QR_FOLDER, exist_ok=True)

# ---------- DATABASE ----------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id TEXT PRIMARY KEY,
        full_name TEXT,
        blood_group TEXT,
        allergies TEXT,
        emergency_contact TEXT,
        is_active INTEGER DEFAULT 1
    )
    """)
    conn.commit()
    conn.close()

init_db()

# ---------- ROUTES ----------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    full_name = request.form["full_name"]
    blood_group = request.form["blood_group"]
    allergies = request.form["allergies"]
    emergency_contact = request.form["emergency_contact"]

    user_id = str(uuid.uuid4())

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (id, full_name, blood_group, allergies, emergency_contact, is_active)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (user_id, full_name, blood_group, allergies, emergency_contact, 1))
    conn.commit()
    conn.close()

    # 2. FIXED: This now works on Localhost, Ngrok, or PythonAnywhere automatically
    base_url = request.host_url.rstrip('/') 
    emergency_url = f"{base_url}/view/{user_id}"

    # Generate QR
    qr = qrcode.QRCode(version=2, error_correction=qrcode.constants.ERROR_CORRECT_Q, box_size=10, border=4)
    qr.add_data(emergency_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(os.path.join(QR_FOLDER, f"{user_id}.png"))

    return render_template("success.html", full_name=full_name, user_id=user_id, emergency_url=emergency_url)

@app.route("/view/<user_id>")
def view(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ? AND is_active = 1", (user_id,))
    user = cursor.fetchone()
    conn.close()

    if not user:
        return "<h2 style='text-align:center;'>🚫 Inactive or Invalid ID</h2>", 404

    _, full_name, blood_group, allergies, emergency_contact, _ = user
    return render_template("emergency.html", full_name=full_name, blood_group=blood_group, 
                           allergies=allergies, emergency_contact=emergency_contact)

# 3. FIXED: These routes now require ?key=my-super-secret-password-123
@app.route("/disable/<user_id>")
def disable(user_id):
    key = request.args.get("key")
    if key != ADMIN_SECRET:
        return "<h1>🚫 Access Denied: Incorrect Secret Key</h1>", 403

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET is_active = 0 WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    return "<h3>Emergency ID disabled successfully</h3>"

@app.route("/enable/<user_id>")
def enable(user_id):
    key = request.args.get("key")
    if key != ADMIN_SECRET:
        return "<h1>🚫 Access Denied: Incorrect Secret Key</h1>", 403

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET is_active = 1 WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    return "<h3>Emergency ID enabled successfully</h3>"

if __name__ == "__main__":
    # Use the PORT provided by the server, or default to 5000
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)