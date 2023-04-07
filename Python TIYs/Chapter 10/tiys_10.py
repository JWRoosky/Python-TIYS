"""
# 10-1
filename = "Chapter 10/txt_files/learning_python.txt"

with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
    
with open(filename) as file_object:
        lines = file_object.readlines()

for i in lines:
     print(i.rstrip())

# 10-2
filename = "Chapter 10/txt_files/learning_python.txt"

with open(filename) as file_object:
    contents = file_object.read()
    print(contents.replace('Python', 'Java').rstrip())



with open(filename) as file_object:
    for line in file_object:
        print(line.replace('Python', 'Java').rstrip())
    


with open(filename) as file_object:
        lines = file_object.readlines()
        

for i in lines:
    i.replace('Python', 'C')
    print(i.replace('Python', 'Java').rstrip())

# 10-3
filename = "Chapter 10/txt_files/guest.txt"
name = str(input("What is your name?"))
with open(filename, 'w') as file_object:
    file_object.write(name)

# 10-4
filename = "Chapter 10/txt_files/guest_book.txt"
print("Press q to exit")
while True:
    name = str(input("What is your name?"))
    if name == 'q':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{name} \n")
        print("Welcome")

# 10-5
filename = "Chapter 10/txt_files/programming_opinions.txt"
print("Press q to exit")
while True:
    opinion = str(input("Why do you like Python programming"))
    if opinion == "q":
        break
    else: 
        with open(filename, 'a') as file_object:
            file_object.write(f"{opinion} \n")

# 10-6
print("Press q to quit")
while True:
    print("Give me two numbers to add together")
    num1 = input("First number: ")
    num2 = input("Second number: ")
    if num1 == 'q' | num2 == 'q':
        break
    try:
        val = int(num1) + int(num2)
    except ValueError:
        print("Please enter 2 integers")
    else:
        print(val)
"""
# 10-7
"""
print("Press q to quit")
while True:
    print("Give me two numbers to add together")
    num1 = input("First number: ")
    num2 = input("Second number: ")
    if num1 == 'q' | num2 == 'q':
        break
    try:
        val = int(num1) + int(num2)
    except ValueError:
        print("Please enter 2 integers")
    else:
        print(val)

# 10-8
def read_file(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else: 
        print(contents)

filenames = ["Chapter 10/txt_files/cats.txt", "Chapter 10/txt_files/dogs.txt"]
for filename in filenames:
    read_file(filename)

# 10-9
def read_file(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else: 
        print(contents)

filenames = ["Chapter 10/txt_files/cats.txt", "Chapter 10/txt_files/dogs.txt"]
for filename in filenames:
    read_file(filename)

# 10-10
def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        num_words = contents.count(' the ')
        print(num_words)

filenames = ["Chapter 10/books/hamlet.txt", "Chapter 10/books/macbeth.txt", "Chapter 10/books/the_tempest.txt"]
for filename in filenames:
    count_words(filename)

# 10-11
fav_number = int(input("Enter your favorite number"))
import json
filename = 'Chapter 10/json/fav_num.json'
with open(filename, 'w') as f:
    num = json.dump(fav_number, f)

# 10-12
import json

filename = "Chapter 10/json/username.json"
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    print(f"We will remember you next you return, {username}")
else:
    print(f"Welcome back, {username}")

# 10-13
import json

filename = "Chapter 10/json/username.json"
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    print(f"We will remember you next you return, {username}")
else:
    bool = input(f"is {username} the correct username?")
    if bool == "yes":
        print(f"Welcome back, {username}")
    else:
        username = input("Apologies, what is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
        print(f"We will remember you next you return, {username}")
"""