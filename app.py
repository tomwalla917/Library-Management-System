"""
Capstone starter: Library Management System
The menu is ready. Finish the class layer in classes/ to make the app work.
"""

from classes.library import Library


def print_menu():
    print("\n=== Library Management System ===")
    print("1. Add book")
    print("2. View books")
    print("3. Add member")
    print("4. View members")
    print("5. Borrow book")
    print("6. Return book")
    print("7. View overdue books")
    print("8. Exit")


def add_book_flow(library):
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    isbn = input("ISBN: ").strip()
    print(library.add_book(title, author, isbn))


def add_member_flow(library):
    member_type = input("Member type (student/faculty): ").strip().lower()
    member_id = input("Member ID: ").strip()
    name = input("Name: ").strip()
    print(library.add_member(member_type, member_id, name))


def borrow_flow(library):
    member_id = input("Member ID: ").strip()
    isbn = input("ISBN: ").strip()
    print(library.borrow_book(member_id, isbn))


def return_flow(library):
    isbn = input("ISBN: ").strip()
    print(library.return_book(isbn))


def display_list(title, items):
    print(f"\n{title}")
    print("-" * len(title))
    if not items:
        print("No records found.")
        return
    for item in items:
        print(item)


def main():
    library = Library()

    actions = {
        "1": lambda: add_book_flow(library),
        "2": lambda: display_list("Books", library.view_books()),
        "3": lambda: add_member_flow(library),
        "4": lambda: display_list("Members", library.view_members()),
        "5": lambda: borrow_flow(library),
        "6": lambda: return_flow(library),
        "7": lambda: display_list("Overdue Books", library.view_overdue_books()),
    }

    while True:
        print_menu()
        choice = input("Choose an option (1-8): ").strip()

        if choice == "8":
            print("Goodbye.")
            break

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()