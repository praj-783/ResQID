/* -------- GLOBAL RESET & BASE -------- */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

:root {
    --primary-red: #8E0000;
    --primary-green: #2e7d32;
    --bg-light: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    --bg-dark: linear-gradient(135deg, #121212 0%, #1e1e1e 100%);
    --text-light: #333;
    --text-dark: #e0e0e0;
    --shadow-light: rgba(0,0,0,0.08);
    --shadow-dark: rgba(0,0,0,0.3);
    --border-radius: 20px;
    --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

body {
    font-family: 'Inter', 'Segoe UI', Roboto, Arial, sans-serif;
    background: var(--bg-light);
    color: var(--text-light);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    transition: var(--transition);
}

body.dark {
    background: var(--bg-dark);
    color: var(--text-dark);
}

/* -------- LOADING SPINNER -------- */
.loading {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    font-size: 18px;
    color: var(--primary-red);
}

.spinner {
    border: 4px solid rgba(142, 0, 0, 0.3);
    border-top: 4px solid var(--primary-red);
    border-radius: 50%;
    width: 40px;
    height: 40px;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* -------- MAIN CONTAINER -------- */
.emergency-container, .home-container {
    max-width: 450px;
    margin: 0 auto;
    padding: 24px;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

/* -------- HEADER -------- */
.emergency-header {
    background: linear-gradient(135deg, #8E0000, #5F0000);
    color: white;
    padding: 24px 28px;
    border-radius: 20px;
    font-size: 24px;
    font-weight: 800;
    margin-bottom: 32px;
    box-shadow: 0 12px 36px rgba(142, 0, 0, 0.4);
    position: relative; /* For absolute positioning of toggle */
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: flex-start; /* Brand starts from left */
    min-height: 80px;
}

.emergency-header::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(45deg, rgba(255,255,255,0.1) 0%, transparent 50%, rgba(255,255,255,0.1) 100%);
    pointer-events: none;
}

body.dark .emergency-header {
    background: linear-gradient(135deg, #6A0000, #3E0000);
}

/* -------- BRAND (Logo Left, Name After) -------- */
.brand {
    display: flex;
    align-items: center;
    gap: 18px;
    position: relative;
    z-index: 1;
    flex-shrink: 0;
}

.logo-wrapper {
    width: 60px;
    height: 60px;
    background: rgba(255, 255, 255, 0.2);
    border-radius: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}

.brand-logo {
    width: 50px;
    height: 50px;
    object-fit: contain;
}

.brand-text {
    display: flex;
    flex-direction: column;
    text-align: left;
}

.brand-name {
    font-size: 24px;
    font-weight: 900;
    color: #ffffff;
    letter-spacing: 0.6px;
    text-shadow: 0 2px 6px rgba(0,0,0,0.4);
}

.brand-tagline {
    font-size: 14px;
    color: rgba(255, 255, 255, 0.9);
    margin-top: 4px;
    font-weight: 500;
}

/* -------- HEADER THEME TOGGLE (Always in Top-Right Corner) -------- */
.header-theme-toggle {
    position: absolute;
    top: 16px;
    right: 20px;
    width: 44px;
    height: 44px;
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 50%;
    font-size: 20px;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    display: flex;
    align-items: center;
    justify-content: center;
    backdrop-filter: blur(10px);
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    z-index: 2;
}

.header-theme-toggle:hover {
    background: rgba(255, 255, 255, 0.25);
    transform: scale(1.05);
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}

body.dark .header-theme-toggle {
    background: rgba(0, 0, 0, 0.3);
    border-color: rgba(255, 255, 255, 0.4);
    color: #ffffff;
}

body.dark .header-theme-toggle:hover {
    background: rgba(0, 0, 0, 0.4);
}

/* -------- RESPONSIVE ADJUSTMENTS -------- */
@media (max-width: 480px) {
    .emergency-header {
        padding: 20px 24px;
        flex-direction: column; /* Stack vertically if needed, but toggle stays in corner */
        align-items: flex-start; /* Brand aligns left */
        gap: 12px;
    }
    
    .brand {
        flex-direction: row;
        gap: 12px;
        align-self: flex-start;
    }
    
    .brand-text {
        text-align: left;
    }
    
    .brand-name {
        font-size: 20px;
    }
    
    .logo-wrapper {
        width: 50px;
        height: 50px;
    }
    
    .brand-logo {
        width: 42px;
        height: 42px;
    }
    
    /* Toggle remains in top-right corner via absolute positioning */
}
/* -------- PROFILE ROW -------- */
.profile-row {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 18px;
    margin: 32px 0 28px;
}

.profile-icon {
    width: 60px;
    height: 60px;
    background: linear-gradient(135deg, #e3f2fd, #bbdefb);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 30px;
    color: #1976d2;
    box-shadow: 0 8px 24px rgba(0,0,0,0.15);
    border: 2px solid rgba(255,255,255,0.9);
}

body.dark .profile-icon {
    background: linear-gradient(135deg, #2a2a2a, #1e1e1e);
    color: #90caf9;
    border-color: rgba(255,255,255,0.1);
}

/* -------- NAME -------- */
.person-name {
    font-size: 30px;
    font-weight: 900;
    color: var(--text-light);
    letter-spacing: 0.5px;
}

body.dark .person-name {
    color: var(--text-dark);
}

/* -------- CARD -------- */
.info-card {
    background: white;
    border-radius: var(--border-radius);
    padding: 24px;
    margin-bottom: 18px;
    box-shadow: 0 10px 28px var(--shadow-light);
    border: 1px solid rgba(0,0,0,0.05);
    transition: var(--transition);
}

.info-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 14px 36px var(--shadow-light);
}

body.dark .info-card {
    background: linear-gradient(135deg, #1e1e1e, #2a2a2a);
    box-shadow: 0 10px 28px var(--shadow-dark);
    border-color: rgba(255,255,255,0.1);
}

/* -------- INFO -------- */
.info-label {
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    color: #666;
    margin-bottom: 10px;
    font-weight: 600;
}

body.dark .info-label {
    color: #bdbdbd;
}

.info-value {
    font-size: 22px;
    font-weight: 800;
    color: #222;
}

body.dark .info-value {
    color: #ffffff;
}

.alert {
    color: #d32f2f;
    font-weight: 900;
}

/* -------- CALL BUTTON -------- */
.call-btn {
    display: block;
    width: 100%;
    margin-top: 32px;
    padding: 24px;
    background: linear-gradient(135deg, var(--primary-green), #1b5e20);
    color: white;
    text-align: center;
    font-size: 18px;
    font-weight: 800;
    border-radius: var(--border-radius);
    text-decoration: none;
    box-shadow: 0 12px 32px rgba(46, 125, 50, 0.4);
    transition: var(--transition);
    position: relative;
    overflow: hidden;
    letter-spacing: 0.5px;
}

.call-btn::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
    transition: left 0.6s;
}

.call-btn:hover::before {
    left: 100%;
}

.call-btn:hover {
    transform: translateY(-4px);
    box-shadow: 0 16px 40px rgba(46, 125, 50, 0.5);
}

.call-btn:active {
    transform: translateY(-1px);
}

body.dark .call-btn {
    background: linear-gradient(135deg, #1b5e20, #0d3b12);
    box-shadow: 0 12px 32px rgba(27, 94, 32, 0.6);
}

/* -------- FOOTER -------- */
.footer-warning {
    text-align: center;
    margin-top: 36px;
    font-size: 14px;
    color: #777;
    font-weight: 500;
    opacity: 0.8;
}

body.dark .footer-warning {
    color: #aaaaaa;
}

/* -------- FORM STYLING (for home page) -------- */
.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 8px;
    color: var(--text-light);
}

body.dark .form-group label {
    color: var(--text-dark);
}

.form-group input {
    width: 100%;
    padding: 14px;
    border: 1px solid #ddd;
    border-radius: 12px;
    font-size: 16px;
    transition: var(--transition);
    background: white;
    color: var(--text-light);
}

.form-group input:focus {
    outline: none;
    border-color: var(--primary-red);
    box-shadow: 0 0 0 3px rgba(142, 0, 0, 0.1);
}

body.dark .form-group input {
    background: #2a2a2a;
    border-color: #555;
    color: var(--text-dark);
}

.btn-primary {
    width: 100%;
    padding: 16px;
    background: linear-gradient(135deg, var(--primary-red), #5F0000);
    color: white;
    border: none;
    border-radius: var(--border-radius);
    font-size: 18px;
    font-weight: 700;
    cursor: pointer;
    transition: var(--transition);
    box-shadow: 0 8px 20px rgba(142, 0, 0, 0.3);
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 28px rgba(142, 0, 0, 0.4);
}

.btn-secondary {
    display: inline-block;
    padding: 12px 24px;
    background: var(--primary-green);
    color: white;
    text-decoration: none;
    border-radius: 12px;
    font-weight: 600;
    transition: var(--transition);
    margin-top: 16px;
}

.btn-secondary:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(46, 125, 50, 0.3);
}

/* -------- RESPONSIVE DESIGN -------- */
@media (max-width: 480px) {
    .emergency-container, .home-container {
        padding: 16px;
    }
    
    .emergency-header, .home-header {
        padding: 20px;
        font-size: 20px;
    }
    
    .brand-name {
        font-size: 20px;
    }
    
    .person-name {
        font-size: 26px;
    }
    
    .info-value {
        font-size: 18px;
    }
    
    .call-btn, .btn-primary {
        padding: 20px;
        font-size: 16px;
    }
}

/* -------- ACCESSIBILITY -------- */
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}

.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
}
