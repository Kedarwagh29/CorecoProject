from bookmain import LibraryMgmt 
from book import Book

def user():
#if(__name__ == "__main__"):
    choice = 0
    bookmgn = LibraryMgmt()
    
    while(choice != 6):
        print("\t\t1.Issue Book")
        print("\t\t2.Search Book")
        print("\t\t3.Submit Book")
        print("\t\t4.Exit")

        choice = int(input("Entre the your choice"))

        if(choice == 1):
            bid = int(input("Entre the book ID"))
            bookmgn.issueBook(bid)
        elif(choice == 2):
            bid = int(input("Entre the Book ID"))
            bookmgn.SearchBook(bid)
        elif(choice == 3):
            bid = input("Entre the Book ID you want to return")
            bookmgn.submitBook(bid)

                       
        elif(choice == 4):
            print("Exit")

               