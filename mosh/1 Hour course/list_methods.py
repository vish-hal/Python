#list are object in python so they do have methods like list have.
numbers =[0,1,2,3,4,5,6,7,8,9]
numbers.append(10)
print(numbers)
# we have added numer 10 at end of our list using append method
numbers.insert(0,-1)
# Insert method will add our variable as per index number given.
#like in above example we added -1 at index number 0
print(numbers)
numbers.remove(-1)
# it will remove element of list you have given like -1 is removed
print(numbers)
#we cam rprint expression as well
print(8 in numbers)
print(len(numbers))
#len function will give us number of elements our list have in our case it's 11
numbers.clear()
print(numbers)