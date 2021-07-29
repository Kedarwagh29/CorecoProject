class Book:
    def __init__(self,bid = 0,bname = "",status = 0,noofpages ="",publication = "",genreofbook =""):
        self.bid = bid
        self.bname = bname
        self.status = status
        self.noofpages = noofpages
        self.publication = publication
        self.genreofbook = genreofbook


    def acceptBook (self):
        self.bid = int(input("Entre the Book ID :"))
        self.bname = input("Entre the Book Name :") 
        self.status = (input("Entre the Book Status :"))
        self.noofpages = (input("enter the No of pages :"))
        self.publication = input("enter the name of publication :")
        self.genreofbook = input("Enter the Genre of book (History, Science, Arts, Science Fiction, etc) :" )

        # 1 = Book is available
        # 0 = Book is not available  

    def displayBook (self):
        print("Book ID = ",self.bid ) 
        print("Book Name = ",self.bname)
        print("Book Status = ",self.status)
        print("NO of pages = ",self.noofpages)
        print("Publication = ",self.publication)
        print("Genre of book = ",self.genreofbook)

    def __str__(self):
        data = str(self.bid)
        data += "," + (self.bname) 
        data += ","  + str(self.status)
        data += ","  + (self.noofpages)
        data +=","   + (self.publication)   
        data +=","   + (self.genreofbook)
        return data  
    

if (__name__ == "__main__"):
    b1 = Book(101,"Science","1","450","tiger","education")
    print(b1)          