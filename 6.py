#tuples and sets
# genders = ("male","female","others")
# print(type(genders))
# print(genders[1:3])

# print(genders.index("female"))

# s = {25,225,3}  #sets are unordered and unindexed 
# s2 = list((1,2,3))
# print(type(s2))


# s1 = {1,2,3,4,5}
# s2 = {1,2,6,7,8}
# s3 = s1|s2              #  | = union operator
# print(s3)
# print(s1 & s2)          # & = intersection operator
# print(s1 - s2)          # - = difference operator
# print(s1 ^ s2)          # ^ = symmetric difference operator

# # s = {1,2,3}

# # s.add(4)
# # s.remove(10)
# # s.discard(10)    #discard is used to remove the element but it does not give the error if the element is not present in the set
# # s.pop()          #pop is used for removing the random element from the set
# # s.clear()        #clear is used for removing all the elements from the set


# s = {1,2,3}
# a = s.pop()
# print(a)

# s = {1,2,3}
# a = s.clear()
# print(a)

# l = [] #this [] is used for list
# t = () #this () is used for tuple
# s = {} #this is used for dictionary

#PROBLEM QUESTIONS(1)
a = (1,2,3,4,5)
a2 = a .index(6,7,8,9,10)
print(type(a2))

