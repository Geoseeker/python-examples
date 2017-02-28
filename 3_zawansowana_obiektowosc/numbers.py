class Numbers(object):

    counter = 0

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter >= 5:
            raise StopIteration 
        self.counter += 1
        return self.counter


numbers = Numbers()

print("1 iteracja")
for num in numbers:
    print(num)

print("2 iteracja")
for num in numbers:
    print(num)
