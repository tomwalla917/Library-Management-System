"""Book model for the Library Management System capstone."""


class Book:
    def __init__(self, title, author, isbn, available=True):
        self._title = title
        self._author = author
        self._isbn = isbn
        # TODO 1: Store the availability value in a private-style attribute.
        self.available = available

    def matches_isbn(self, isbn):
        return self._isbn == isbn

    def is_available(self):
        # TODO 2: Return the current availability status.
        if self.is_available is True:
            return(f"{self.title} is available to be checked out")
        pass

    def checkout(self):
        # TODO 3: Mark the book unavailable.
        self.available is False
        pass

    def checkin(self):
        # TODO 4: Mark the book available.
        self.available is True
        pass

    def details(self):
        # TODO 5: Return a formatted string with title, author, ISBN, and status.
        # Example: "Dune by Frank Herbert | ISBN: 123 | Available"
        return(f"{self.title} | ISBN: {self.isbn} | {self.available}")
        pass

    def to_dict(self):
        # TODO 6: Return a serializable dictionary for JSON saving.
        pass

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["title"],
            data["author"],
            data["isbn"],
            data.get("available", True),
        )