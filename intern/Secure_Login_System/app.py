from flask import Flask, render_template, request, redirect, session
import sqlite3
import bcrypt

app = Flask(__name__)

app.secret_key = "secretkey"

# =========================================
# DATABASE CONNECTION
# =========================================

conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

conn.commit()

# =========================================
# HOME PAGE
# =========================================

@app.route("/")
def home():

    if "user" in session:
        return redirect("/dashboard")

    return redirect("/login")

# =========================================
# REGISTER
# =========================================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # Input Validation
        if len(password) < 6:
            return "Password must be at least 6 characters."

        # Hash Password
        hashed = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )

        # Store User
        cursor.execute(
            "INSERT INTO users(username, password) VALUES(?, ?)",
            (username, hashed)
        )

        conn.commit()

        return redirect("/login")

    return render_template("register.html")

# =========================================
# LOGIN
# =========================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        cursor.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        )

        user = cursor.fetchone()

        if user:

            stored_password = user[2]

            if bcrypt.checkpw(
                password.encode("utf-8"),
                stored_password
            ):

                session["user"] = username

                return redirect("/dashboard")

        return "Invalid Username or Password"

    return render_template("login.html")

# =========================================
# DASHBOARD
# =========================================

@app.route("/dashboard")
def dashboard():

    if "user" in session:
        return render_template(
            "dashboard.html",
            username=session["user"]
        )

    return redirect("/login")

# =========================================
# LOGOUT
# =========================================

@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect("/login")

# =========================================
# RUN APP
# =========================================

if __name__ == "__main__":
    app.run(debug=True)