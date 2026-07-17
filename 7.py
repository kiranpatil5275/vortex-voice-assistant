# skill = {
#     "varun" : "mechanical skill",
#     "kiran" : "coding skill",
#     "suraj" : "driving skill",
#     "mallu mama": "maneger of karnataka bank"
# }

# print(skill["varun"])
# print(type(skill))

# print(skill.get("kiran","sorry not found"))

# print(skill.get("ronaldo","sorry not found"))      #get method is used for getting the value of the key if the key is not present then it will return the default value which we have given in the get method


# print (skill)

# print("i am  adding the mallu mama skill here" )

# skill["mallu mama"] = "maneger"

# print(skill)

# print(skill)

# print("skill updating...")

# skill["suraj"] = "driving skill and over acting skill"

# print(skill)


# print(skill)

# skill.pop("suraj")  #pop ia used for removing the key value pair from the dictionary
# print(skill)

# del skill["varun"]  #del is used for removing the key value pair from the dictionary but it gives the error if the key is not present in the dictionary
# print (skill)


# birthday = {
#     "kiran" : "30-11-2006",
#     "varun" : "8-1-2010",
#     "suraj" : "29-2-2008",
    
# }


# print(birthday.keys())
# print(birthday.values())
# print(birthday.items())


# item1 = {
#     "milk" : "2ltr",
#     "weight" : 2,
#     "price":35
    
# }

# item2= {
#     "sugar" : "2kg",
#     "weight" : "2kg",
#     "price" : 50
# }
    
# items = [item1, item2]

# print(f"total price of items : {item1['price'] + item2['price']}")