import sqlite3

class BookDB:
    def __init__(self, db_name="book_db"):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.connection:
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                genre TEXT,
                rating INTEGER
            );
            """)

    def add_book(self, title, author, genre, rating):
        with self.connection:
            self.connection.execute(
                "INSERT INTO books (title, author, genre, rating) VALUES (?, ?, ?, ?);",
                (title, author, genre, rating)
            )

    def get_all_books(self):
        return self.connection.execute("SELECT * FROM books;").fetchall()

    def get_books_by_title(self, title):
        return self.connection.execute(
            "SELECT * FROM books WHERE title = ?;", (title,)
        ).fetchall()

    def get_books_by_author(self, author):
        return self.connection.execute(
            "SELECT * FROM books WHERE author = ?;", (author,)
        ).fetchall()

    def get_books_by_rating_range(self, min_rating, max_rating):
        return self.connection.execute(
            "SELECT * FROM books WHERE rating BETWEEN ? AND ?;",
            (min_rating, max_rating)
        ).fetchall()

    def get_best_book_by_author(self, author):
        return self.connection.execute(
            "SELECT * FROM books WHERE author = ? ORDER BY rating DESC LIMIT 1;",
            (author,)
        ).fetchone()

    def delete_book_by_title(self, title):
        with self.connection:
            self.connection.execute("DELETE FROM books WHERE title = ?;", (title,))

    def delete_book_by_id(self, book_id):
        with self.connection:
            self.connection.execute("DELETE FROM books WHERE id = ?;", (book_id,))
