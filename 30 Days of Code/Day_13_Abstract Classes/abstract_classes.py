from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(self): pass

#Write MyBook class
class MyBook(Book):

    def __init__(self, title, author, price):
        self._title = title
        self._author = author
        self._price = price

    
    def display(self):

        print(f"Title: {self._title}" )
        print(f"Author: {self._author}" )
        print(f"Price: {self._price}" )


title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()