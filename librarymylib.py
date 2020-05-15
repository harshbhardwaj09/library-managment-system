class Lib:
    def __init__(self,booklist,name):
        self.booklist=booklist
        self.name=name
        self.takedict={}


    def bookname(self):
        print(f"name of books arre")
        for book in self.booklist:
            print(book)

    def findbook(self,book):
        if book in self.booklist:
            print("yes we have that book ")
        else:
            print("no we don't have that book")


    def takebook(self , book,user):
        if book not in self.booklist:
            print("this book is not persent in our lib")
        else:
            if book not in self.takedict.keys():
                self.takedict.update({book:user})
                print("you have suuccessfullytaken the book")
            else:
                print(f"book is already taken by {self.takedict}")


    def takenbook(self):
        if len(self.takedict)==0:
            print("no book is taken")
        else:
            print("taken books are")
            for i in self.takedict:
                print(i)


    def addbook(self,book):
        print(f"{book} has been added to our lib")
        self.booklist.append(book)


    def returnbook(self,book):
        if book in self.takedict:
            self.takedict.pop(book)
            print("you have successfully return the book")
        elif book in self.booklist:
            print("this book is not taken")
        else:
            print("book is not in our lib....not a valid book name")


harsh=Lib(["C","C++","Java","Python","C-sharp"], "harsh's lib")
while(True):
    print("choose amy func")
    print("1-book name")
    print("2-find book")
    print("3-landbook")
    print("4-check taken books")
    print("5-to add book")
    print("6-to return the book")
    choice=input()
    if(choice not in ['1','2','3','4','5','6']):
        print("chose valid op")
        continue
    if choice=='1':
        harsh.bookname()
    elif choice=='2':
        book=input("enter the name of book")
        book=book.capitalize()
        harsh.findbook(book)
    elif choice=='3':
        book=input("enetr the name of book")
        user=input("name of user")
        book=book.capitalize()
        harsh.takebook(book,user)
    elif choice=='4':
        harsh.takenbook()
    elif choice =='5':
        book=input("name of book")
        book=book.capitalize()
        harsh.addbook(book)
    elif choice=='6':
        book=input("name of book to returmn")
        book=book.capitalize()
        harsh.returnbook(book)
    print("q to quite and c to conrtinie")
    choice2=input()
    if choice2 == "q":
        exit()
    elif choice2 == "c":
        continue
    else:
        print("choose a valid option")
        pass
