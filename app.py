from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret_key"


def db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    if "user_id" not in session:
        return redirect("/login")
    return redirect("/profile")


# -------- AUTH --------
@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        try:
            conn = db()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO user (username,password) VALUES (?,?)",
                (request.form["username"], request.form["password"])
            )
            conn.commit()
            conn.close()
            return redirect("/login")
        except:
            error = "Username already exists"

    return render_template("register.html", error=error)


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        conn = db()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM user WHERE username=? AND password=?",
            (request.form["username"], request.form["password"])
        )
        user = cur.fetchone()
        conn.close()

        if user:
            session["user_id"] = user["user_id"]
            return redirect("/profile")

        error = "Invalid credentials"

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


# -------- PROFILE --------
@app.route("/profile")
def profile():
    conn = db()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM portfolio WHERE user_id=?",
        (session["user_id"],)
    )
    portfolios = cur.fetchall()
    conn.close()
    return render_template("profile.html", portfolios=portfolios)


# -------- ADD PORTFOLIO --------
@app.route("/add_portfolio", methods=["GET", "POST"])
def add_portfolio():
    if request.method == "POST":
        conn = db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO portfolio (user_id,title,description) VALUES (?,?,?)",
            (session["user_id"], request.form["title"], request.form["description"])
        )
        conn.commit()
        conn.close()
        return redirect("/profile")

    return render_template("add_portfolio.html")


# -------- DELETE PORTFOLIO --------
@app.route("/delete_portfolio/<int:portfolio_id>")
def delete_portfolio(portfolio_id):
    conn = db()
    cur = conn.cursor()
    cur.execute("DELETE FROM portfolio WHERE portfolio_id=?", (portfolio_id,))
    conn.commit()
    conn.close()
    return redirect("/profile")


# -------- PORTFOLIO VIEW --------
@app.route("/portfolio/<int:pid>")
def portfolio(pid):
    conn = db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM portfolio WHERE portfolio_id=?", (pid,))
    portfolio = cur.fetchone()

    search = request.args.get("search", "")
    category = request.args.get("category", "")

    query = "SELECT * FROM work WHERE portfolio_id=?"
    params = [pid]

    if search:
        query += " AND (title LIKE ? OR description LIKE ?)"
        params += [f"%{search}%", f"%{search}%"]

    if category:
        query += " AND category=?"
        params.append(category)

    cur.execute(query, params)
    works = cur.fetchall()

    cur.execute(
        "SELECT DISTINCT category FROM work WHERE portfolio_id=?",
        (pid,)
    )
    categories = [c[0] for c in cur.fetchall() if c[0]]

    conn.close()

    return render_template(
        "portfolio.html",
        portfolio=portfolio,
        works=works,
        categories=categories,
        search=search,
        selected_category=category
    )


# -------- ADD WORK --------
@app.route("/add_work/<int:pid>", methods=["GET", "POST"])
def add_work(pid):
    if request.method == "POST":
        conn = db()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO work
            (portfolio_id,title,description,media_type,file_path,category)
            VALUES (?,?,?,?,?,?)
            """,
            (
                pid,
                request.form["title"],
                request.form["description"],
                request.form["media_type"],
                request.form["file_path"],
                request.form["category"]
            )
        )
        conn.commit()
        conn.close()
        return redirect(f"/portfolio/{pid}")

    return render_template("add_work.html", pid=pid)


# -------- DELETE WORK --------
@app.route("/delete_work/<int:work_id>")
def delete_work(work_id):
    conn = db()
    cur = conn.cursor()

    cur.execute("SELECT portfolio_id FROM work WHERE work_id=?", (work_id,))
    row = cur.fetchone()

    if row:
        pid = row["portfolio_id"]
        cur.execute("DELETE FROM work WHERE work_id=?", (work_id,))
        conn.commit()
        conn.close()
        return redirect(f"/portfolio/{pid}")

    conn.close()
    return redirect("/profile")


if __name__ == "__main__":
    app.run(debug=True)
