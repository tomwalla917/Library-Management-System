# Capstone Starter: Library Management System

## Objective
Build a CLI-based Library Management System using object-oriented Python. You will finish the core class layer by adding missing attributes, implementing methods, and connecting inheritance, encapsulation, and persistence.

## What You Will Build
A terminal app that lets a librarian:
- add and view books
- add and view members
- borrow and return books
- review overdue checkouts
- save all data to JSON between runs

## Project Structure
- `app.py` handles the command-line menu
- `classes/book.py` models each book
- `classes/member.py` models members and borrowing rules
- `classes/library.py` coordinates the whole system
- `data/library_data.json` stores saved data

## Estimated Time
45-75 minutes

## Getting Started
1. Open this `Starter` folder.
2. Start with the files in `classes/`.
3. Complete the TODO sections in order.
4. Run `python app.py` after each major step.

## Instructions

### Step 1: Complete the `Book` class
Work in `classes/book.py`.

Your tasks:
- add the missing private availability attribute
- implement `checkout` and `checkin`
- return a readable string from `details`
- return a dictionary from `to_dict`

Expected result:
- each book tracks title, author, ISBN, and availability

### Step 2: Complete the member hierarchy
Work in `classes/member.py`.

Your tasks:
- finish the `Member` base class methods
- enforce borrowing limits in `can_borrow`
- update the borrowed list in `borrow_book` and `return_book`
- set custom limits and due dates in `StudentMember` and `FacultyMember`

Expected result:
- students and faculty follow different borrowing rules

### Step 3: Complete the `Library` manager
Work in `classes/library.py`.

Your tasks:
- implement add and lookup helpers
- wire book checkout and return behavior
- save and load data with JSON
- generate the overdue report from transaction records

Expected result:
- the `Library` object becomes the single source of truth for books, members, and transactions

### Step 4: Run the CLI
Work in `app.py` only if you want optional enhancements.

Your tasks:
- run the menu
- add at least two books and two members
- borrow and return at least one book
- confirm that data persists in `data/library_data.json`

Expected result:
- the menu should work end to end without editing the menu loop itself

## Quick Checks
- `Book` uses private-style attributes with `_`
- `StudentMember` and `FacultyMember` inherit from `Member`
- borrowing a checked-out book is blocked
- returning a book marks it available again
- the JSON file updates after each change

## Troubleshooting
Problem: Books never become unavailable.
Solution: Check that `borrow_book` calls `book.checkout()` after member validation succeeds.

Problem: Loaded members lose their type.
Solution: Save a `member_type` field, then rebuild either `StudentMember` or `FacultyMember` during `load_data`.

Problem: Overdue report is always empty.
Solution: Compare `due_date` strings by converting them with `datetime.strptime`.

## Extension Challenges

### Challenge 1: Search tools
Add methods to search books by title or author.

### Challenge 2: Update operations
Allow the librarian to update book titles or member names from the menu.

### Challenge 3: Richer reports
Show all books currently borrowed by each member.

## What's Next
This capstone pulls together class design, inheritance, encapsulation, composition, and file persistence. The next step is testing and refactoring this project like a small production codebase.