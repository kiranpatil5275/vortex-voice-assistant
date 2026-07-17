#lists    #indexing positive and negative  AND "APPEND" AND ALSO "POP"
# items = ["cofiee","sugar","milk","tea"]
# print(items[2])
# items = ["cofiee","sugar","milk","tea"]
# print(items[-3])
# items = ["cofiee","sugar","milk","tea"]
# print(items)
# items.pop(0)    #POP means it remove  the elements from the string(it means eliminating from the right)
# print(items)
# items.pop(-1)   #POP means it remove  the elements from the string (it means eliminating from the left)
# print(items)


fruits = ["apple","banana","mango","chikku"]
print(fruits[0:4])
print(fruits[1:4])
# fruits.pop(2)
# print(fruits)

fruits.append("peru")    #this is useful for adding the elements
print(fruits)

fruits.insert(2,"pineapple")   #this is useful for adding the element in between the line
print(fruits)

fruits[1] ="cocoumber"
print(fruits)

A = ["100","200","300","400","500","600"]
B = A[1::2]       #it skips the one by one element
print(B)

fruits = ["apple","banana","mango","chikku"]
print(len(fruits))    #it shows the length of the variable

num = [43,54,87,67,12,42,56,89]    #it engages the numbers into a assending order
num.sort()
print(num)

print(fruits.index("apple"))   #out put =0  #INDEX

num = [1,2,3,4,2,3,1,5,6,4,]
print(num.count(3))   #it counts the repeated numbers #output = 2

num = [43,54,87,67,12,42,56,89]    #it engages the numbers into a desrnding  order
num.reverse()
print(num)
                      

 
