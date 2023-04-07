"""
# 7-1
car = input("What kind of rental car would you like?")
print(f"Let's see if we can get you a {car}")

# 7-2
people = int(input("How many people are there in your party?"))
if people > 8:
    print("You will have to wait for a table")
else:
    print("Your table is ready")

# 7-3
num = int(input("What is your number?"))
if num % 10 == 0:
    print("Is a multiple of 10")
else:
    print("Is not a multiple of 10")

# 7-4
val = True
while val == True:
    topping = input("What toppings would you like to add to the pizza")
    if topping == 'quit':
        break
    print("Ok, I'll add that topping to the pizza")

# 7-5
val = True
while val == True:
    age = int(input("What is your age?"))
    if int(age) < 3:
        print("Your ticket is free")
    elif int(age) < 12:
        print("Your ticket is $10")
    else:
        print("Your ticket is $15")


# 7-6
val = True
while val == True:
    age = input("What is your age?")
    
    if age == 'quit':
        break

    if int(age) < 3:
        print("Your ticket is free")
    elif int(age) < 12:
        print("Your ticket is $10")
    else:
        print("Your ticket is $15")

# 7-7 
while True:
    print(5)

# 7-8
sandwich_orders = ['pastrami', 'reuben', 'blt']
finished_orders = []

for i in sandwich_orders:
    finished_orders.append(i)
print(finished_orders)

# 7-9
sandwich_orders = ['pastrami', 'reuben', 'pastrami', 'blt', 'pastrami', 'blt']
finished_orders = []

print("We are very sorry but we have run out of pastrami")

for i in sandwich_orders:
    if i == 'pastrami':
        continue
    finished_orders.append(i)

print(f"Here are the finished orders: {finished_orders}")

# 7-10
locations = []
print("Press q to end the survey")
while True:
    inp = str(input("If you could go anywhere in the world, where would you go?"))
    if inp == 'q':
        break
    if inp == '':
        continue
    locations.append(inp)
print(f"Overall, people wanted to go to {locations}")
"""