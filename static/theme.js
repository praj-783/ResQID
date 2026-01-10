document.addEventListener("DOMContentLoaded", function () {
    const body = document.body;
    const btn = document.getElementById("themeBtn");

    if (!btn) return;

    // Load saved preference and set initial icon
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "dark") {
        body.classList.add("dark");
        btn.textContent = "☀️"; // Sun for light mode toggle
    } else {
        btn.textContent = "🌙"; // Moon for dark mode toggle
    }

    // Toggle theme on click
    btn.addEventListener("click", function () {
        body.classList.toggle("dark");

        if (body.classList.contains("dark")) {
            localStorage.setItem("theme", "dark");
            btn.textContent = "☀️"; // Switch to sun icon
        } else {
            localStorage.setItem("theme", "light");
            btn.textContent = "🌙"; // Switch to moon icon
        }
    });
});
