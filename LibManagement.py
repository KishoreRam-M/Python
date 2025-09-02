print("Zen Lib ")

bookList = [];
borrowList = [];


def addBook(book):
    bookList.append(book)
    print("Book Added", book)


def veiwBook():
    print(bookList)


def searchBook(book):
    if book in bookList:
        print("Book is Found ")
    else:
        print("Book is not found ")


def updateBook(book, newbook):
    for i in range(len(bookList)):
        if (bookList[i] == book):
            bookList[i] = newbook
            print("Book Updated", book)
    else:
        print("Book is not found ")


def deleteBook(book):
    bookList.remove(book)


def borrowBook(book):
    borrowList.append(book)

    print("Book Borrowed", book)


def returnBook(book):
    borrowList.remove(book)


def report():
    print("Total No of Books:", len(bookList))
    print("Total No of Borrowed:", len(borrowList))
    print("")

while True:

 print("Enter the Choice ")
 print("1. Add Book")
 print("2. Veiw Book")
 print("3. Search Book")
 print("4. Update Book")
 print("5. Delete Book")
 print("6. Borrow Book")
 print("7. Return Book")
 print("8. Report")
 print("9. Exit")

 choice = int(input())

 if choice == 1:

    book = input("Enter Book Name:")

    addBook(book)

 elif choice == 2:

    veiwBook()

 elif choice == 3:

    search = input("Enter Book Name:")

    searchBook(search)

 elif choice == 4:

    existingBook = input("Enter Book Name:")

    newBook = input("Enter New Book Name:")

    updateBook(existingBook, newBook)

 elif choice == 5:

    deleteBook(input("Enter Book Name:"))

 elif choice == 6:

    borrowBook(input("Enter Book Name:"))

 elif choice == 7:

    returnBook(input("Enter Book Name:"))

 elif choice == 8:

    report()
 elif choice == 9:
    exit()
 else:
    print("Invalid Choice")

