from bookmain import LibraryMgmt
from book import Book

def admin():
#if(__name__ == "__main__"):
    
    choice = 0
    bookmgn = LibraryMgmt()
    
    while(choice != 6):
        print("\t\t1.Add Book")
        print("\t\t2.Display Book")
        print("\t\t3.Search Book")
        print("\t\t4.Edit Book")
        print("\t\t5.Delete Book")
        print("\t\t6.Exit")

        choice = int(input("Entre the your choice"))

        if(choice == 1):
            b1 = Book()
            b1.acceptBook()
            bookmgn.AddBook(b1)

        elif(choice == 2):
            bookmgn.DisplayBook()

        elif(choice == 3):
            bid = int(input("Entre the Book ID"))
            bookmgn.SearchBook(bid)

        elif(choice == 4):
            bid = int(input("Entre the Book ID"))
            bookmgn.EditBook(bid)

        elif(choice == 5):
            bid = int(input("Entre the Book ID"))
            bookmgn.DeleteBook(bid)

        elif(choice == 6):
            print("Exit") 
