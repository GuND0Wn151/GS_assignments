class Book:
    
    def __init__(self,title="",authors=[],subject="",date="",info="") :
        self.title=title
        self.authors=authors
        self.subject=subject
        self.date=date
        self.info=info

    def getAuthors(self):
        print("The authors are :")
        for i in self.authors:
            print(i)

    def addAuthor(self,newAuthor):
        self.authors.append(newAuthor)

    def getDate(self):
        print(f"The date of the book is {self.date}")

    def getTitle(self):
        print(f"The title of the book is {self.title}")

    def getSubject(self):
        print(f"The subject of the book is {self.subject}")
    
    def getInfo(self):
        print(f"The info about the book is {self.info}")



b=Book("Song of ice and fire",["R R Marting"],"Fantasy","25-08-2023","A story about the greatest and cruelest westroes king")
b.addAuthor("JK Rowling")
b.addAuthor("Steven")
print("The Title is ",b.getTitle())
print("The info is ",b.getInfo())
print("The subject is ",b.getSubject())
print("The date is ",b.getSubject())
print(b.getAuthors())
