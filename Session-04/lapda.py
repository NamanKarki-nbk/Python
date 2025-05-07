#lambda

add = lambda x:x+1
print(add(5))

#map(): Change every item in a list
numners=[2,4,6,8]

result = list(map(lambda x:x*2, numners))
print(result)

#filter(): Keep only what you want

numbers=[1,2,3,4]

result= list(filter(lambda x:x%2==0, numbers))
print(result)

#reduce(): Smach everythiing into one value
from functools import reduce
numbers=[1,2,3,4]

result=reduce(lambda x,y:x+y,numbers)
print(result)