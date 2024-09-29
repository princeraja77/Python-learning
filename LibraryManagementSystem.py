class Book:
    def __init__(self,name,author,copies):
        self.name=name
        self.author=author
        self.copies=copies
    def borrow(self,numbers=1):
        if self.copies==0:
            print("No copies available to borrow")
            return False
        else:
            self.copies-=1
            print("Borrow successful")
            return True
    def return_book(self,numbers=1):
            self.copies+=1
    def __str__(self):
         return f"Name - {self.name} | Author - {self.author} | Copies available - {self.copies}"


class Library:
     def __init__(self):
          self.book_list={}
          self.book_borrow_list={}
     def borrow(self,book_name,person_name):
          if book_name in self.book_list:
               if self.book_list[book_name].borrow():
                    self.book_borrow_list[book_name].append(person_name)
          else:
               print("Book not available in library")
     def view_all_books(self):
        #   print(self.book_list)
          for book in self.book_list:
               print(self.book_list[book])
        #   pass

     def return_book(self,book_name,person_name):
          if book_name in self.book_list:
               self.book_list[book_name].return_book()
               self.book_borrow_list[book_name].remove(person_name)
          else:
               print("Book doesn't belong to the library")
     def borrower_list(self,book_name):
          print(self.book_borrow_list[book_name])
        #   pass

     def add_book(self,name,author,copies):
          newbook=Book(name,author,copies)
          self.book_list[name]=newbook
          self.book_borrow_list[name]=[]
def main():
    system=Library()
    while 1:
        print("Library Management System")
        print("1. Add new book")
        print("2. borrow a book")
        print("3. Return a book")
        print("4. view all the books")
        print("5. list of borrowers for a book")
        print("6. exit")
        choice=int(input("enter your choice: \n"))
        if choice==1:
            name=input("enter name of the book")
            author=input("enter the author of the book")
            copies=int(input("enter no of copies of book"))
            system.add_book(name,author,copies)
            #   pass
        elif choice==2:
            name=input("enter name of the book")
            person_name=input("enter the name of the borrower")
            system.borrow(name,person_name)
            #   pass
        elif choice==3:
            name=input("enter name of the book")
            person_name=input("enter the name of the borrower")
            system.return_book(name,person_name)
            #   pass
        elif choice==4:
            system.view_all_books()
            #   pass
        elif choice==5:
            name=input("enter name of the book")
            system.book_borrow_list(name)
            #   pass
        elif choice==6:
            break
if __name__=="__main__":
    main()