import mysql.connector

print("Connecting...")

conn = mysql.connector.connect(
    user="root",
    password="admin",
    host="127.0.0.1",
    database="artist_portfolio_db",
    port=3306,
    use_pure=True,
    connection_timeout=5
)

print("Connected")
cur = conn.cursor()

print("Inserting artist...")
cur.execute("""
INSERT INTO artist (name, email, bio)
VALUES (%s, %s, %s)
""", (
    "Ahmed Sagar",
    "akkuahmedsagar@gmail.com",
    "Independent artist"
))

artist_id = cur.lastrowid
print("Artist ID:", artist_id)


print("Inserting portfolio...")
cur.execute("""
INSERT INTO portfolio (title, artist_id)
VALUES (%s, %s)
""", (
    "My Portfolio",
    artist_id
))

portfolio_id = cur.lastrowid
print("Portfolio ID:", portfolio_id)


print("Inserting category...")
cur.execute("""
INSERT IGNORE INTO category (category_name)
VALUES ('Painting')
""")

cur.execute("""
SELECT category_id FROM category WHERE category_name = 'Painting'
""")
category_id = cur.fetchone()[0]

print("Category ID:", category_id)



print("Inserting artwork...")
cur.execute("""
INSERT INTO artwork (title, medium, year_created, image_path, portfolio_id)
VALUES (%s, %s, %s, %s, %s)
""", (
    "Test Artwork",
    "Painting",
    2024,
    "images/art_1.jpg",
    portfolio_id
))

artwork_id = cur.lastrowid
print("Artwork ID:", artwork_id)

print("Linking artwork to category...")
cur.execute("""
INSERT INTO artwork_category (artwork_id, category_id)
VALUES (%s, %s)
""", (artwork_id, category_id))

conn.commit()
conn.close()

print("DONE")
