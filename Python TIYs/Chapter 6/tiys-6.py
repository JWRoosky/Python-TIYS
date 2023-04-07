"""
PROGRAM NAME: tiys_6
PROGRAM PURPOSE: e-book tiys for chapter 6
DATE WRITTEN: 10/25/22
PROGRAMMER: Jack Rueschhoff
"""


6-1
person = {'first_name': 'devon', 'last_name': 'garls', 'age': 17, 'city': 'denver'}
print(person['first_name'], person['last_name'], person['age'], person['city'])


6-2
fav_nums = {'devon': 64, 'ben': 7, 'ruby': 18, 'coulter': 28, 'athena': 2}
print(fav_nums)


# 6-3

glossary = {'for': 'statement that allows for looping in python',
            'if': 'statement that allows for the use of conditionals in python',
            'while': 'another looping tool that remains true while a condition exists',
            'System.out.print': 'java syntax equivalent to the python print function. wordy, yet endearing',
            'in': 'searches for a value in a string/array'}

print(f"for: {glossary['for']}", end='\n'
      f"if: {glossary['if']} \n"
      f"while: {glossary['while']}\n"
      f"System.out.print: {glossary['System.out.print']}\n"
      f"in: {glossary['in']}")


# 6-4

for key, value in glossary.items():
    print(f"{key}: {value}")

glossary = {'for': 'statement that allows for looping in python',
            'if': 'statement that allows for the use of conditionals in python',
            'while': 'another looping tool that remains true while a condition exists',
            'System.out.print': 'java syntax equivalent to the python print function. wordy, yet endearing',
            'in': 'searches for a value in a string/array',
            'print': 'function that displays data into a console',
            'not': 'checks to see if a value is not in an array',
            'dictionary': 'similar to an array, but stores data in key value pairs',
            'array': 'stores multiple variables in the same object',
            'float': 'non-whole integer data type'}

for key, value in glossary.items():
    print(f"{key}: {value}")


# 6-5

rivers = {'nile': 'egypt',
          'amazon': 'brazil',
          'vltava': 'czechia'}

for key in rivers.keys():
    print(f"This river is called the {key.title()} river")
for value in rivers.values():
    print(f"This country is called {value.title()}")


# 6-6

favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python'}

take_poll = {'jen', 'tyrion', 'edward', 'bob'}
for name in take_poll:
    if name in favorite_languages.keys():
        print(f"Thank you {name.title()} for taking this poll")
    else:
        print(f"Hello {name.title()}, would you like to take our poll?")


# 6-7
person1 = {'first_name': 'devon', 'last_name': 'garls', 'age': 17, 'city': 'denver'}
person2 = {'first_name': 'coulter', 'last_name': 'stutz', 'age': 17, 'city': 'chatfield'}
person3 = {'first_name': 'ben', 'last_name': 'hensley', 'age': 17, 'city': 'lakewood'}

people = [person1, person2, person3]
for i in range(len(people)):
    print(people[i])


# 6-8
dog = {'animal':'dog', 'owner':'bill'}
cat = {'animal':'cat', 'owner':'mary'}
bird = {'animal':'bird', 'owner':'jenny'}

pets = [dog, cat, bird]

for i in range(len(pets)):
    print(f"This animal is a {pets[i]['animal']} that is owned by {pets[i]['owner']}")


# 6-9
fav_places = {'jack':'cesky krumlav', 'devon':'chipotle', 'coulter':'qdoba'}

for key, value in fav_places.items():
    print(f"{key.title()}'s favorite place is {value.title()}")



# 6-10
fav_nums = {'devon': [1, 2, 3], 'ben': [7], 'ruby': [1, 4, 5], 'coulter': [28], 'athena': [3, 6, 9]}

for key, values in fav_nums.items():
    print(f"{key.title()}'s favorite number's' is/are ")
    for i in values:
        print(i)


# 6-11
rivers = {'nile': 'egypt', 'amazon':'brazil', 'vltava':'czechia', 'danube':'hungary'}

for key, value in rivers.items():
    print(f"The {key.title()} river is found in {value.title()}")
