# we know whatever input we take from user is considered string in python3 
# Now it's really important to learn how to convert this taken string input to other typer of variable.
# I must say learn type conversion in python.

age = input("what is your age ?")
# if we directly move to the next step without converion of this string vlaue we will face error in our terminal.
# as we can't perform arthmatical operation on string in python.
# so let's change age to integer

age=int(age) #here we have changed value of age variable to int type
# we have stored it to variable name age. now our variable age is integer type
#Now we can perform  arthmatical opraion on it.

Old_age= age-2

#Now that we have performed our arthmatical operation . we will required to change it to string as otherwise we will not be able to concatenate with string.

Old_age=str(Old_age) 

# we change old_age to string and stored it in Old_age variable.

print("you were "+Old_age +" years old 2 years back.")

#Note:- we can use bool() for boolean and float() for float type variable conversion.
