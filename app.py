from book_db import BookDB
from book_ui import BookTrackerUI

class BookApp:
    def __init__(self):
        self.db = BookDB()
        self.ui = BookTrackerUI(self.db)

    def run(self):
        print("📚 Welcome to the Ultimate Book Tracker 4++! 📚")
        self.ui.run()

if __name__ == "__main__":
    app = BookApp()
    app.run()
