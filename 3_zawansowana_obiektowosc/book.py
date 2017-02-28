class Book(object):
    name = None
    price = None 
    author = None
    pages = ["a", "b", "c"]
    i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i == len(self.pages):
            raise StopIteration
        page = self.pages[self.i]
        self.i += 1
        return page


book = Book()

for page in book:
    print(page)

