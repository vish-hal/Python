#lists are used to represent list of variables.
friends =["harsh","mrrootsec","akash","ayush","rahul"]
print(friends[0])
# index number of first element would be 0 as an array
# we can refer to variale by their right to left sequence but numbering would start from 1 instead of 0
print(friends[-3])
# we can change value of list as well like below
friends[-1]='manash'
print(friends)
# As we can see it clearly rahul has been replaced with manash suceesfully.
print(friends[1:])
# it's printing element from index num 1
print(friends[0:-2])