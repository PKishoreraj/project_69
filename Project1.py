class BookShelf:
    def _init_(self,book,author,price,dop):
        self.bookshelf_book=book
        self.bookshelf_author=author
        self.bookshelf_price=price
        self.bookshelf_dop=dop
    def add_bookshelf(self):
        print("Book Name:"+self.bookshelf_book)
        print("Author:"+str(self.bookshelf_author)
        print("Price"+self.bookshelf_price)
        print("Date of publish"+self.bookshelf_dop)
        print("Book Added")
book1=BookShelf("Harry Potter","J.K.Rowling",1928,1997)
book1.add_bookshelf()
book2=BookShelf("Diary of a Wimpy Kid","Jeff Knney",700,2017)
book2.add_bookshelf()