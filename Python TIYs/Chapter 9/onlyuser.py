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