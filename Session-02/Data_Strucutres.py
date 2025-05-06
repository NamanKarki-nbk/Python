list1=["mercedes", "bmw", "tesla", "porshe"]
print(len(list1))
print(type(list1))
print(list1[-1:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])
thislist[1]="peach"
print(thislist)

thislist[4:7]=["coconut", "tomato", "gauva"]
print(thislist)

thislist.insert(2,"paasion")
print(thislist)

#append itesm or add list items
thislist.append("potato")
print(thislist)

#extending the list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#remove list items
##remove,pop,del,clear
thislist.remove("cherry")
print(thislist)

thislist.pop(1)
print(thislist)

del thislist[0]

thislist.clear()
print(thislist)

#loop through the list
list2=["apple", "banana", "cherry"]

for i in range(len(list2)):
    print(list2[i])
    
list3=["bmw", "tesla", "porsha"]
for x in list3:
    print(x)


##----List Comprrehension---##
##It provides the shortest sysntax for looping through lists
[print(x) for x in list3]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)