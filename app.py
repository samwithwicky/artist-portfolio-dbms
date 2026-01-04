from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        user="root",
        password="admin",
        host="127.0.0.1",
        database="artist_portfolio_db",
        port=3306,
        use_pure=True,
        connection_timeout=5
    )

# GALLERY – VIEW ARTWORKS
@app.route("/")
def gallery():
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("""
        SELECT a.artwork_id, a.title, a.medium, a.year_created, a.image_path,
               c.category_name
        FROM artwork a
        LEFT JOIN artwork_category ac ON a.artwork_id = ac.artwork_id
        LEFT JOIN category c ON ac.category_id = c.category_id
        ORDER BY a.artwork_id DESC
    """)

    artworks = cur.fetchall()
    conn.close()
    return render_template("gallery.html", artworks=artworks)

# ADD ARTWORK
@app.route("/add", methods=["GET", "POST"])
def add_artwork():
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM category")
    categories = cur.fetchall()

    if request.method == "POST":
        title = request.form["title"]
        medium = request.form["medium"]
        year = request.form["year"]
        image_path = request.form["image_path"]
        category_id = request.form["category"]

        cur.execute("""
            INSERT INTO artwork (title, medium, year_created, image_path, portfolio_id)
            VALUES (%s, %s, %s, %s, 1)
        """, (title, medium, year, image_path))

        artwork_id = cur.lastrowid

        cur.execute("""
            INSERT INTO artwork_category (artwork_id, category_id)
            VALUES (%s, %s)
        """, (artwork_id, category_id))

        conn.commit()
        conn.close()
        return redirect(url_for("gallery"))

    conn.close()
    return render_template("add.html", categories=categories)


# EDIT ARTWORK
@app.route("/edit/<int:artwork_id>", methods=["GET", "POST"])
def edit_artwork(artwork_id):
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM artwork WHERE artwork_id = %s", (artwork_id,))
    artwork = cur.fetchone()

    if request.method == "POST":
        cur.execute("""
            UPDATE artwork
            SET title=%s, medium=%s, year_created=%s, image_path=%s
            WHERE artwork_id=%s
        """, (
            request.form["title"],
            request.form["medium"],
            request.form["year"],
            request.form["image_path"],
            artwork_id
        ))

        conn.commit()
        conn.close()
        return redirect(url_for("gallery"))

    conn.close()
    return render_template("edit.html", artwork=artwork)

# DELETE ARTWORK
@app.route("/delete/<int:artwork_id>")
def delete_artwork(artwork_id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM artwork WHERE artwork_id=%s", (artwork_id,))
    conn.commit()
    conn.close()

    return redirect(url_for("gallery"))

# RUN APP
if __name__ == "__main__":
    app.run(debug=True)
