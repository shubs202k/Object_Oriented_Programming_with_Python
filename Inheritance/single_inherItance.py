class Apple:
    manufacturer = "Apple Inc"
    contactWebsite = "www.apple.com/contact"

    def contactDetails(self):
        print("To contact us, log on to", self.contactWebsite)

# Inherit Attributes and Methods from Apple Class (Base Class)
class MacBook(Apple):
    def __init__(self):
        self.yearOfManufacture = 2017

    def manufactureDetails(self):
        print("This MacBook was manufactured in the year {} by {}".format(self.yearOfManufacture, self.manufacturer))

# Create Object from Derived Class
macBook = MacBook()
macBook.manufactureDetails()
macBook.contactDetails()
