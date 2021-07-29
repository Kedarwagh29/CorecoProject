from book import Book
from os import path
from datetime import datetime

class LibraryMgmt:
    
    def AddBook(self,b1):
        data = str(b1)
        with open ("bookData.txt","a") as fp:
            fp.write(data)
            fp.write("\n")

     
    def DisplayBook(self):
        if(path.exists("bookData.txt")):
            with open("bookData.txt","r") as fp:
                print(fp.read())
        else:
            print("No data to print")        
        
        
        
    def DeleteBook(self,bid):
        if(path.exists("bookData.txt")):
            with open ("bookData.txt","r") as fp :
                allBook = []
                found = False
                for line in fp:
                    try:
                        line.index(str(bid),0,10)
                        found = True
                    except:
                        allBook.append(line) 
                #print(allBook)
            if(found):
                with open ("bookData.txt","w") as fp:
                    for e in allBook:
                        fp.write(e)
            else:
                print("This Book ID is not Present")
        else:
            print(" Data is not Avaliable")     
        
    def SearchBook(self,bid):
        if(path.exists("bookData.txt")):
            with open("bookData.txt","r") as fp:
                for line in fp:
                    #if(str(bid) in line):
                    try:
                        line.index((bid),0,10)
                        print("Record is found")
                        print(line)
                        break
                    except:
                        pass
                else:
                    print("This book is not available")    
                        
        else:
            print("No data is available")            
        
        
    def EditBook(self,bid):
        if(path.exists("bookData.txt")):
            with open ("bookData.txt","r") as fp :
                allBook = []
                found = False
                for line in fp:
                    try:
                        line.index(str(bid),0,10)
                        data = line.split(",")
                        found = True
                        ans = input("Do you change the Book Name(y/n)?")
                        if(ans.lower() == "y"):
                            data[1] = input("Entre the Book Name")
                        ans = input("Do you change Book Satus(y/n)?")
                        if(ans.lower() == "y"):
                            data[2] = input("Entre the Status Book")
                        line = "," .join(data)
                        line += "\n"             
                    except:
                        pass
                    allBook.append(line)

                #print(allBook)
            if(found):
                with open ("bookData.txt","w") as fp:
                    for e in allBook:
                        fp.write(e)
        else:
            print(" Data is not Avaliable") 

    def issueBook (self,bid):
        if(path.exists("bookData.txt")):
            with open("bookData.txt","r") as fp:
                allBook = []
                found = False
                for line in fp :
                    try :
                        line.index(str(bid),0,10)
                        found = True
                        data = line.split(",")
                        if(int(data[2]) == 0):
                            print("Book is not available")
                            return
                        data[2] = "0\n" 
                        line = ",".join(data)
                        print(line)
                        #line += ("\n") 
                    except:
                        pass
                    allBook.append(line)
                #print(allBook)     

                if(found):
            
                    with open("bookData.txt","w") as fp:
                        #print("book issue Successfully")
                        for e in allBook :
                            fp.write(e)    
                    
                    issue_date = input("Enter the date of issue dd-mm-yyyy")
                    data[2] = issue_date
                    sname = input("Enter the student name")
                    #data.append(sname)
                    data.insert(2,sname)
                    with open ("issueBook.txt","a") as fp :
                        #dt = datetime(int(issue_date[2]),int(issue_date[1]),int(issue_date[0])) 
                        #print(data,dt)
                        data = ",".join(data)
                        data += "\n"
                        fp.write(data)

                else:
                    print("Record is not found")

    def submitBook (self,bid):
        if(path.exists("issuebook.txt")):
            allBook = []
            with open ("issuebook.txt","r") as fp :
                for line in fp :
                    try:
                        line.index(str(bid),0,10)
                        line = line.split(",")
                        dt_issue = line[3].split("-")
                        dt_issue = datetime(int(dt_issue[2]),int(dt_issue[1]),int(dt_issue[0])) 
                        dt_submit = input("Enter the submit date (dd-mm-yy)")
                        dt_submit = dt_submit.split("-")
                        dt_submit = datetime(int(dt_submit[2]),int(dt_submit[1]),int(dt_submit[0]))  
                        diff =  dt_submit - dt_issue
                        #print(diff.days)
                        diff = diff.days
                        diff = diff - 5
                        if(diff > 0):
                            fine = diff * 20
                            print("Please pay fine of RS.{0}".format(fine))
                    except:
                        # non-matching data
                        allBook.append(line) 

            with open ("issuebook.txt","w") as fp:
                for book in allBook:
                    fp.write(book) 

            with open ("bookData.txt","r") as fp:
                allBook =[]
                for line in fp : 
                    try: 
                        line.index(bid,0,10)
                        line = line.split(",")
                        line[2] = "1\n"
                        line = ",".join(line)  
                        print(line)
                    except:
                        pass
                    finally:
                        allBook.append(line) 

            with open ("bookData.txt","w") as fp:
                for book in allBook:
                    fp.write(book)             

