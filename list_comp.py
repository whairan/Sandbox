"""
These are some examples of list comprehension that you can make use of. Pretty cool and handy.
- It can go from simple to very complicated as with all things. 
- You can generate a list or lists or a list of lists or lists of lists or a list of dictionaries, etc

"""

# eg 1 
eg1 = [i for i in range(10)]
print(eg1)

#eg2
eg2 = [[] for i in range(10)]
print(eg2)

#eg3 
eg3 = [[i for i in range(10)] for i in range(10)]
print(eg3)

# eg4
eg4 = [{} for i in range(10)]
print(eg4)

#... You can play around with more examples 