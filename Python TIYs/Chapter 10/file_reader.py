filename = 'Chapter 10/pi_digits.txt'

"""
with open('Chapter 10/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        """

with open(filename) as file_object:
    lines = file_object.readlines()

for i in lines:
    print(i.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))