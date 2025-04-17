class BookTrackerUI:
    MENU = """
📚 -- Book Tracker Menu -- 📚

1️⃣  Add a new book
2️⃣  View all books
3️⃣  Find a book by title
4️⃣  Top-rated book by an author
5️⃣  🔚 Exit
6️⃣  Delete a book by title or ID
7️⃣  Find books within rating range

Choose an option (1-7): """

    def __init__(self, db):
        self.db = db

    def run(self):
        while True:
            choice = input(self.MENU).strip()
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.view_books()
            elif choice == "3":
                self.find_by_title()
            elif choice == "4":
                self.top_by_author()
            elif choice == "5":
                print("👋 Goodbye, happy reading!")
                break
            elif choice == "6":
                self.delete_book()
            elif choice == "7":
                self.rating_range()
            else:
                print("❌ Invalid choice, try again.")

    def add_book(self):
        title = input("📖 Title: ")
        author = input("✍️ Author: ")
        genre = input("🏷️ Genre: ")
        try:
            rating = int(input("⭐ Rating (0–100): "))
            self.db.add_book(title, author, genre, rating)
            print("✅ Book added!")
        except ValueError:
            print("❌ Rating must be a number.")

    def view_books(self):
        print("\n📚 All Books:\n" + "-"*30)
        for book in self.db.get_all_books():
            print(f"#{book[0]} | '{book[1]}' by {book[2]} | Genre: {book[3]} | Rating: {book[4]}/100")
        print("-"*30)

    def find_by_title(self):
        title = input("🔍 Enter title: ")
        books = self.db.get_books_by_title(title)
        if not books:
            print("❌ No books found.")
        else:
            for book in books:
                print(f"'{book[1]}' by {book[2]} | Genre: {book[3]} | Rating: {book[4]}/100")

    def top_by_author(self):
        author = input("👤 Author: ")
        top = self.db.get_best_book_by_author(author)
        if not top:
            print("❌ No books found for this author.")
        else:
            print(f"🏆 Top book by {author}: '{top[1]}' | Genre: {top[3]} | Rating: {top[4]}/100")

    def delete_book(self):
        choice = input("Delete by (1) Title or (2) ID? ")
        if choice == "1":
            title = input("🗑️ Enter title: ")
            self.db.delete_book_by_title(title)
            print("✅ Book(s) deleted.")
        elif choice == "2":
            try:
                book_id = int(input("🗑️ Enter book ID: "))
                self.db.delete_book_by_id(book_id)
                print("✅ Book deleted.")
            except ValueError:
                print("❌ Invalid ID.")
        else:
            print("❌ Invalid choice.")

    def rating_range(self):
        try:
            min_r = int(input("🔽 Min rating: "))
            max_r = int(input("🔼 Max rating: "))
            books = self.db.get_books_by_rating_range(min_r, max_r)
            if books:
                print("\n📊 Books in Rating Range:")
                for book in books:
                    print(f"'{book[1]}' by {book[2]} | {book[4]}/100")
            else:
                print("❌ No books in that range.")
        except ValueError:
            print("❌ Ratings must be numbers.")
