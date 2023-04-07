val = True
while val == True:
    age = input("What is your age?")

    if age == 'quit':
        break
    elif int(age) < 3:
        print("Your ticket is free")
    elif int(age) < 12:
        print("Your ticket is $10")
    else:
        print("Your ticket is $15")