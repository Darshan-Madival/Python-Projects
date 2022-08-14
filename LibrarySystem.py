#Library Management System For Students:
class library:
    def __init__(self,books):
        self.books=books
    def availablebooks(self):
        print("The Books in Library are as Follow")
        for books in self.books:
            print(" *"+books)
    def borrowbook(self,book):
        if book in self.books:
            print(f"you have issued the book {book}.kindly keep it safe")
            self.books.remove(book)
            return True
        else:
            print("The book is not available in The Library")
            return False
    def returnbook(self,books):
        self.books.append(books)
        print("Thanks for returning the book")


class student:
    def requestbook(self):
        self.books=input("Enter The name of The book you want: ")
        if any(char.isdigit() for char in self.books):
            print("Please do not include digits in your item.")
        else:
            return self.books
    def returnbook(self):
        self.books=input("Enter The name of The book you want to return: ")
        return self.books


if __name__ == '__main__':
    mainlibrary=library(["python","Java","C","php"])
    student=student()
    while(True):
        message='''\n**********WELCOME TO THE LIBRARY OF DARSHAN**********
        PLEASE SELECT THE MENU BELOW.
        1.list of books
        2.To borrow a book
        3.Add/Return a book
        4.exit'''
        print(message)
        a=int(input("Enter The choice::"))
        if a==1:
            mainlibrary.availablebooks()
        elif a==2:
            mainlibrary.borrowbook(student.requestbook())
        elif a==3:
            mainlibrary.returnbook(student.returnbook())
        elif a==4:
            print("Thanks for using my Library")
            exit()
        else:
            print("Invalid choice")
