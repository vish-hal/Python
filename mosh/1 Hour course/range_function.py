numbers= range(10)
# it will have 10 numbers but indexing start from 0 so 10 will be excluded
print(numbers)
# as we see it didn't print number but shows the range 0 to 10 .
for number in numbers:
    print(number)
# now we got element printed as in keyword help us found elements of range function.
#we can directly print our range elements without worring about storing range funtion in variable like below
for number in range(5,9):
# here we have given 2 value in range function first indicate starting element last element till our range will have elements.
    print(number)

# If we have 3 value as and input in our range funciton then 3rd one will indicate steps between our range element.
for number in range(1,11,2) :
    print(number)