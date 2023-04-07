"""
# 9-1
class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"{self.name} is a {self.cuisine} restaurant")
    
    def open(self):
        print(f"{self.name} is now open!")

rat = Restaurant("Ratatouille", "French")
print(rat.name)
print(rat.cuisine)
rat.describe_restaurant()
rat.open()

# 9-2
rat = Restaurant("Ratatouille", "French")
buc = Restaurant("Bucca di Beppo", "Italian")
cas = Restaurant("Casa Bonita", "Mexican")

rat.describe_restaurant()
buc.describe_restaurant()
cas.describe_restaurant()

# 9-3
class User:
    def __init__(self, fname, lname, location, occupation):
        self.fname = fname
        self.lname = lname
        self.location = location
        self.occupation = occupation
    
    def describe_user(self):
        print(f"{self.fname} {self.lname} is a(n) {self.occupation} who lives in {self.location}")
    
    def greet_user(self):
        print(f"Hello there {self.fname}!")

coulter = User("Coulter", "Stutz", "Chatfield", "CS Student")
rock = User("Dwayne", "Johnson", "Hollywood", "Actor")
ras = User("Grigory", "Rasputin", "St. Petersburg", "Lover of the Russian Queen")

coulter.greet_user()
coulter.describe_user()

rock.greet_user()
rock.describe_user()

ras.greet_user()
ras.describe_user()

# 9-4
class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.numserved = 0

    def describe_restaurant(self):
        print(f"{self.name} is a {self.cuisine} restaurant")
    
    def open(self):
        print(f"{self.name} is now open!")

    def set_num_served(self, val):
        self.numserved = val
    
    def inc_num_served(self):
        self.numserved += 1

restaurant = Restaurant("Ratatouille", "French")

restaurant.numserved = 5
print(restaurant.numserved)

restaurant.set_num_served(10)
print(restaurant.numserved)

restaurant.inc_num_served()
print(restaurant.numserved)

# 9-5
class User:
    def __init__(self, fname, lname, location, occupation):
        self.fname = fname
        self.lname = lname
        self.location = location
        self.occupation = occupation
        self.logattempts = 0
    
    def describe_user(self):
        print(f"{self.fname} {self.lname} is a(n) {self.occupation} who lives in {self.location}")
    
    def greet_user(self):
        print(f"Hello there {self.fname}!")
    
    def inc_logattempts(self):
        self.logattempts += 1
    
    def reset_logattempts(self):
        self.logattempts = 0

coulter = User("Coulter", "Stutz", "Chatfield", "CS Student")

coulter.inc_logattempts()
coulter.inc_logattempts()
coulter.inc_logattempts()
coulter.inc_logattempts()
coulter.inc_logattempts()
coulter.inc_logattempts()
coulter.inc_logattempts()
coulter.inc_logattempts()
coulter.inc_logattempts()
coulter.inc_logattempts()
coulter.inc_logattempts()
print(coulter.logattempts)

coulter.reset_logattempts()
print(coulter.logattempts)

# 9-6
class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.numserved = 0

    def describe_restaurant(self):
        print(f"{self.name} is a {self.cuisine} restaurant")
    
    def open(self):
        print(f"{self.name} is now open!")

    def set_num_served(self, val):
        self.numserved = val
    
    def inc_num_served(self):
        self.numserved += 1


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ["vanilla", "chocolate", "strawberry", "coconut"]

    def display_flavors(self):
        print(self.flavors)

stand = IceCreamStand("The Best Stand", "Ice Cream")
stand.display_flavors()

# 9-7
class User:
    def __init__(self, fname, lname, location, occupation):
        self.fname = fname
        self.lname = lname
        self.location = location
        self.occupation = occupation
        self.logattempts = 0
    
    def describe_user(self):
        print(f"{self.fname} {self.lname} is a(n) {self.occupation} who lives in {self.location}")
    
    def greet_user(self):
        print(f"Hello there {self.fname}!")
    
    def inc_logattempts(self):
        self.logattempts += 1
    
    def reset_logattempts(self):
        self.logattempts = 0


class Admin(User):
    def __init__(self, fname, lname, location, occupation):
        super().__init__(fname, lname, location, occupation)
        self.priveleges = ("r", "w", "x")

    def show_priveleges(self):
        print(self.priveleges)


jeff = Admin('jeff', 'ornstein', 'new jersey', 'it administrator')
jeff.show_priveleges()

# 9-8
class User:
    def __init__(self, fname, lname, location, occupation):
        self.fname = fname
        self.lname = lname
        self.location = location
        self.occupation = occupation
        self.logattempts = 0
    
    def describe_user(self):
        print(f"{self.fname} {self.lname} is a(n) {self.occupation} who lives in {self.location}")
    
    def greet_user(self):
        print(f"Hello there {self.fname}!")
    
    def inc_logattempts(self):
        self.logattempts += 1
    
    def reset_logattempts(self):
        self.logattempts = 0


class Admin(User):
    def __init__(self, fname, lname, location, occupation):
        super().__init__(fname, lname, location, occupation)
        self.priveleges = Priveleges("r", "w", "x")



class Priveleges:
    def __init__(self, r, w, x):
        self.r = r
        self.w = w
        self.x = x

    def show_priveleges(self):
        print(f'{self.r} {self.w} {self.x}')

jeff = Admin('jeff', 'ornstein', 'new jersey', 'it administrator')
jeff.priveleges.show_priveleges()

# 9-9
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh battery.')

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f'This car can go about {range} miles on a full charge')
    
    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
            print("Battery successfully upgraded")
        else: 
            print("Your battery is already upgraded to the maximum level")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


car = ElectricCar("tesla", "roadster", "2015")
car.battery.get_range()
car.battery.upgrade_battery()
car.battery.get_range()

# 9-10
from restaurant import Restaurant

chilis = Restaurant("chilis", "comfort food")
chilis.describe_restaurant()

# 9-11
from user import Admin
till = Admin('till','lindemann','munich','vocalist')

# 9-12
from adminandpriveleges import Admin
till = Admin('till','lindemann','munich','vocalist')

# 9-13
from random import randint
class Die:
    def __init__(self, numsides, numrolls):
        self.numsides = numsides
        self.numrolls = numrolls
    
    def roll_dice(self):
        for i in range(self.numrolls):
            print(randint(1, self.numsides), end=" ")

sixer = Die(6, 10)
sixer.roll_dice()
print("\n")
tenner = Die(10, 10)
tenner.roll_dice()
print("\n")
twenter = Die(20, 10)
twenter.roll_dice()

# 9-14
from random import randint
from random import choice

lst = ['a', 'c', 'k', 'y', 'd']

for i in range(10):
    lst.append(randint(1, 20))

newlst = []

for i in range(4):
    newlst.append(choice(lst))

print(f'If your numbers match these four: {newlst}, then you win the lottery!')

# 9-15
from random import randint
winning_ticket = [15, 3, 8, 19]
my_ticket = []
flag = True
while flag == True:
    for i in range(4):
        my_ticket.append(randint(1, 20))
    if my_ticket == winning_ticket:
        print('you win!!!')
        flag = False
    else:
        print("wah wah")
        my_ticket = []

# 9-16
"""