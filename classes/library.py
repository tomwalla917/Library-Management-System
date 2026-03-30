"""Library manager for the Library Management System capstone."""

import json
from datetime import datetime, timedelta
from pathlib import Path

from .book import Book
from .member import FacultyMember, StudentMember


class Library:
    def __init__(self):
        self._books = []
        self._members = []
        self._transactions = []
        self._data_path = Path(__file__).resolve().parent.parent / "data" / "library_data.json"
        self.load_data()

    def add_book(self, title, author, isbn):
        # TODO 1: Reject duplicate ISBNs,  
        for book in self.books:
            if book.isbn == isbn:
                return ("Error, this is a duplicate")
            
        # add a Book,
        new_book = Book(title, author, isbn)
        self._books.append(new_book)

        #save data, return a message.
        self.save_data()
        print ("Book has been added successfully")
            
        pass

    def add_member(self, member_type, member_id, name):
        # TODO 2: Reject duplicate member IDs.
        # Build either StudentMember or FacultyMember, save data, and return a message.
        for member_id in self.member_id:
            if member_id == member_id:
                return ("cannot have duplicate member ids")
        
        pass

    def find_book(self, isbn):
        # TODO 3: Return the matching Book object or None.
        for book in self._books:
            if self.isbn == isbn:
                return {self.book}
            else:
                return ("book not found")
        pass

    def find_member(self, member_id):
        # TODO 4: Return the matching member object or None.
        for member in self._members:
            if self.member_id == member_id:
                return {member object?}
        pass

    def view_books(self):
        return [book.details() for book in self._books]

    def view_members(self):
        return [member.details() for member in self._members]

    def borrow_book(self, member_id, isbn):
        # TODO 5: Validate member and book.
        # Block unavailable books.
        # Use member.borrow_book, mark the book checked out, create a transaction,
        # save data, and return a user-friendly message.
        pass

    def return_book(self, isbn):
        # TODO 6: Find the borrowed book and its active transaction.
        # Mark the book available, remove the ISBN from the member,
        # mark the transaction returned, save data, and return a message.
        pass

    def view_overdue_books(self):
        # TODO 7: Return a list of overdue report strings for active transactions.
        # Compare each due date to datetime.now().
        pass

    def save_data(self):
        # TODO 8: Save books, members, and transactions to self._data_path as JSON.
        pass

    def load_data(self):
        if not self._data_path.exists():
            self.save_data()
            return

        with open(self._data_path, "r", encoding="utf-8") as handle:
            data = json.load(handle)

        self._books = [Book.from_dict(item) for item in data.get("books", [])]
        self._members = []
        for item in data.get("members", []):
            member_class = FacultyMember if item.get("member_type") == "faculty" else StudentMember
            self._members.append(
                member_class(item["member_id"], item["name"], item.get("borrowed_books", []))
            )
        self._transactions = data.get("transactions", [])

    def _find_active_transaction(self, isbn):
        for transaction in self._transactions:
            if transaction["isbn"] == isbn and not transaction.get("returned", False):
                return transaction
        return None

    def _build_transaction(self, member, isbn):
        due_date = datetime.now() + timedelta(days=member.get_due_days())
        return {
            "member_id": member._member_id,
            "isbn": isbn,
            "borrow_date": datetime.now().strftime("%Y-%m-%d"),
            "due_date": due_date.strftime("%Y-%m-%d"),
            "returned": False,
        }