"""
# 8-1
def display_message():
    print("In this chapter we learned about how to make a function.")

display_message()

# 8-2
def favorite_book(title):
    print(f"My favorite book is {title}")

favorite_book("Alice in Wonderland")

# 8-3
def make_shirt(size, text):
    print(f"The shirt is size {size} and has text which reads {text}")

make_shirt('large', 'world peace')
make_shirt('small','this shirt is tiny')

# 8-4
def make_shirt(size='large', text='i love python'):
    print(f"The shirt is size {size} and has text which reads {text}")

# 8-5
def describe_city(city, country="Germany"):
    print(f'{city} is in {country}')

describe_city('Cologne')
describe_city('Dresden')
describe_city('Prague', 'Czechia')

# 8-6
def city_country(city, country):
    name = f"{city}, {country}"
    return name.title()

print(city_country('dresden', 'germany'))
print(city_country('brno', 'czechia'))
print(city_country('berlin', 'germany'))

# 8-7
def make_album(title, name, num_songs=''):
    album = {'album title':title, 'artist name':name}
    if num_songs != '':
        album['num_songs'] = num_songs
    return album

print(make_album("Svetlo ve Tme", "Jelen", 10))
print(make_album("Zeit", "Rammstein"))

# 8-8
def make_album(title, name, num_songs=''):
    album = {'album title':title, 'artist name':name}
    if num_songs != '':
        album['num_songs'] = num_songs
    return album

while True:
    print("enter an album title and artist name")
    print("press enter to quit")
    aname = input("artist's name: ")
    atitle = input("album title: ")
    if aname.__eq__('q') | atitle.__eq__('q'):
        break
    else:
        print(make_album(aname, atitle))

# 8-9
lst = ['Hallo', 'Guten Tag', 'Wie heisen sie?']
def show_messages(txt):
    for text in txt:
        print(text)

show_messages(lst)

# 8-10
list = ['Hallo', 'Guten Tag', 'Wie heisen sie?']
lst = list
lst2 = []
def send_messages(txt):
    for text in txt:
        lst2.append(text)
        txt.remove(text)
    lst2.append(txt[0])
    del txt[0]
    
send_messages(lst)
print(lst)
print(lst2)

# 8-11
print(list)

# 8-12
def sandwich_summary(*ingredients):
    return ingredients

print(sandwich_summary('cheese', 'chicken', 'mayo'))
print(sandwich_summary('queso', 'pollo', 'mayo', 'lechuga'))
print(sandwich_summary('kase', 'huhn', 'mayo', 'kopfsalat', 'speck'))

#8-13
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('jack', 'rueschhoff', height='tall', hobby='musician', 
                            occupation='wt compsci student')
print(user_profile)

# 8-14
def make_car(brand, model, **info):
    info['car_brand'] = brand
    info['car_model'] = model
    return info

car = make_car('honda','cr-v', color='white', year=2015)
print(car)

# 8-15
import printing_models

# 8-16
import make_car
from make_car import make_car
from make_car import make_car as mc
import make_car as mc
from make_car import *
"""
# 8-17