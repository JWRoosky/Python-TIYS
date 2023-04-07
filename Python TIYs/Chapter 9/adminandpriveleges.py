from onlyuser import User

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