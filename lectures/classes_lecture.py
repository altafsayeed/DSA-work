class Cookie:
    def __init__(self, color): # This is a contructor, all constructors need __init__ which means initialize.
        self.color = color # self means it's a method part of a class

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

# We create a new cookie like this

cookie_one = Cookie('green')
cookie_two = Cookie('blue')

cookie_one.set_color('yellow')

print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())
