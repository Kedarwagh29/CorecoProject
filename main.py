from Admin import admin
from User import user

if(__name__ == "__main__"):
    choice = 0
    while (choice != 6):
        print("\t\t1.Admin")
        print("\t\t2.User")
        print("\t\t3.Exit")
        choice = int(input("Entre the choice"))

        if(choice == 1):
            admin()
        elif(choice == 2):
            user()
        elif(choice == 3):
            break    
