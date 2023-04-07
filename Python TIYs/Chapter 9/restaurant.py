class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.numserved = 0

    def describe_restaurant(self):
        print(f"{self.name.title()} is a {self.cuisine} restaurant")
    
    def open(self):
        print(f"{self.name} is now open!")

    def set_num_served(self, val):
        self.numserved = val
    
    def inc_num_served(self):
        self.numserved += 1