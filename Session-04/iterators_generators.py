# An iterator is an object that you can loop through (like a list). It must have two things:

# __iter__() → returns the iterator object

# __next__() → returns the next item each time it's called


class CountUpToThree():
    def __init__(self):
        self.num=1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num > 3:
            raise StopIteration
        value = self.num
        self.num +=1
        return value
    
#using it
counter = CountUpToThree()
for num in counter:
    print(num)

def count_up_to_three():
    for i in range(1,4):
        yield i

#using it
for num in count_up_to_three():
    print(num)