#Bug - accepts blank input


print("Please enter the pickup information.")

#customer name
valid = False
while not valid:
    name = input("Please enter your name: ")
    if name != "":
        print (name)
        break

    else:
        print ("Sorry, this cannot be blank.")

#customer phone number
valid = False
while not valid:
    phone = input("Please enter your phone number: ")
    if phone != "":
        print (phone)
        break
    else:
        print ("Sorry, this cannot be blank.")