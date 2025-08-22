# Book class with encapsulation and abstraction
class Book:
    def __init__(self, title, author, genre, availability=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.__availability = availability  # Private attribute for availability
        self.__issued_to = None  # Private attribute for the member who has borrowed the book

    # Method to check the availability of the book
    def is_available(self):
        return self.__availability

    # Method to borrow the book
    def borrow(self, member):
        if self.__availability:
            self.__availability = False
            self.__issued_to = member
            return self.title + " has been borrowed by " + member.name + "."
        else:
            return self.title + " is currently not available."

    # Method to return the book
    def return_book(self):
        if not self.__availability:
            self.__availability = True
            member_name = self.__issued_to.name
            self.__issued_to = None
            return self.title + " has been returned by " + member_name + "."
        else:
            return self.title + " was not borrowed."

    # Getter method for book status
    def get_status(self):
        status = "available" if self.__availability else "not available"
        return "Book '" + self.title + "' by " + self.author + " is currently " + status + "."

# Member class with encapsulation for membership and borrow limits
class Member:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type  # 'premium' or 'regular'
        self.__borrow_limit = 5 if membership_type == 'regular' else 10  # Default borrow limits
        self.__borrowed_books = []  # Private list to keep track of borrowed books

    # Method to borrow a book
    def borrow_book(self, book):
        if len(self.__borrowed_books) < self.__borrow_limit:
            result = book.borrow(self)
            if "borrowed" in result:
                self.__borrowed_books.append(book)
            return result
        else:
            return self.name + " has reached their borrow limit of " + str(self.__borrow_limit) + " books."

    # Method to return a book
    def return_book(self, book):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            return book.return_book()
        else:
            return self.name + " did not borrow " + book.title + "."

    # Getter method for borrow limit
    def get_borrow_limit(self):
        return self.__borrow_limit

# Example usage of the Library Management System

# Creating book instances
book1 = Book("The Catcher in the Rye", "J.D. Salinger", "Fiction")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
book3 = Book("1984", "George Orwell", "Dystopian")

# Creating member instances
member1 = Member("Alice", "regular")
member2 = Member("Bob", "premium")

# Member borrowing books
print(member1.borrow_book(book1))  # Alice borrowing book1
print(member2.borrow_book(book2))  # Bob borrowing book2
print(member1.borrow_book(book3))  # Alice borrowing book3 (Should succeed as Alice has borrow limit of 5)

# Checking book status
print(book1.get_status())  # Status of book1
print(book2.get_status())  # Status of book2

# Member returning books
print(member1.return_book(book1))  # Alice returning book1
print(member2.return_book(book2))  # Bob returning book2
