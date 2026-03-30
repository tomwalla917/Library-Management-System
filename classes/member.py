"""Member models for the Library Management System capstone."""


class Member:
    def __init__(self, member_id, name, borrowed_books=None):
        self._member_id = member_id
        self._name = name
        self._borrowed_books = borrowed_books or []

    def get_member_type(self):
        return "member"

    def get_borrow_limit(self):
        # TODO 1: Return the default borrow limit for a base member.
        return 2
        pass

    def get_due_days(self):
        # TODO 2: Return the default checkout length in days.
        return 14
        pass

    def can_borrow(self):
        # TODO 3: Return True when borrowed books is below the borrow limit.
        if len._borrowed_books < len.get_borrow_limit:
            return True
        pass

    def borrow_book(self, isbn):
        # TODO 4: Enforce can_borrow, append ISBN, and return True or False.
        pass

    def return_book(self, isbn):
        # TODO 5: Remove the ISBN if present and return True or False.
        pass

    def details(self):
        # TODO 6: Return a formatted member summary string.
        pass

    def to_dict(self):
        return {
            "member_id": self._member_id,
            "name": self._name,
            "borrowed_books": self._borrowed_books,
            "member_type": self.get_member_type(),
        }


class StudentMember(Member):
    def get_member_type(self):
        return "student"

    def get_borrow_limit(self):
        # TODO 7: Students can borrow up to 2 books.
        return 2
        pass

    def get_due_days(self):
        # TODO 8: Students keep books for 14 days.
        return 14
        pass


class FacultyMember(Member):
    def get_member_type(self):
        return "faculty"

    def get_borrow_limit(self):
        # TODO 9: Faculty can borrow up to 5 books.
        return 5
        pass

    def get_due_days(self):
        # TODO 10: Faculty keep books for 28 days.
        return 28
        pass