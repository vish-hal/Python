question ="Where do you live now a Days?"
#strings are technically object in python
print(question.upper())
print(question.lower())
#.upper method returns upper case string of our string object named question. 
#.lower method returns lower case string of our string object named question.
print(question.find('you'))
# we can use .find method to find out index of particular string in our string.
# Index number strart from 0 like and array in python.
print(question.find('You'))
# -1 will be rerurned if it's not part of our object string.
print(question.find('e'))
# find method look for start to match the string form left and return only index num of first occurance .
print(question.replace('e','a'))
# replace work diffrently then find , it will change all occurance of that particular string.
print(question.replace('sad','happy'))
# it's will return orignal string if string to replace is not part of object string.

#How do we check if our object string have some character or sequence of characters?
# we can use find to know if it does but it returns index nuber in return.
# ideal choice would be to use 'in' keyword let's see an example below.

print("now" in question ,"wow" in question)
# question have 'now' so it  returns 'True' for that.
# whereas we don't have any string 'wow' in question so that it returns 'False'.
