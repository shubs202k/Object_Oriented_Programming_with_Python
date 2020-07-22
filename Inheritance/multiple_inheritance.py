class OperatingSystem:
    multitasking = True
    name = 'Mac OS'

class Apple:
    website = "www.apple.com"
    name = "Apple"

class Macbook(OperatingSystem, Apple):
    def __init__(self):
        if self.multitasking is True:
            print('This is a multitasking system. Visit {} for more details'.format(self.website))
            print('Name :', self.name)

# If attribute is present for both parent classes, derived class inherits
# based on the order of classes provided in derived class.
macbook = Macbook()
