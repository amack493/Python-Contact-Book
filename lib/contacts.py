print("Welcome to your contact list.")  

UI = """
[1] Add Contact
[2]View Contacts
[3]Search Contacts
[4]Exit
"""

class Contact:
    def __init__(self, name=None, phone=None, email=None, address=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    
class App:
    def __init__(self, database):
            self.database = database
            self.contacts= {}

    def add(self):
        name, phone, email, address = self.getinfo()
        if name not in self.contacts:
            self.contacts[name] = Contact(name, phone, email, address)
        else:
            print("Contact already exists.")

    def viewall(self):
        if self.contacts:
            print(f"{self.name}, {self.phone}, {self.email}, {self.address}")
            for contact in self.contacts.values():
                print(contact)
        else:
            print("No contacts in database.")

    def getinfo(self):
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        address = input("Address: ")
        return name, phone, email, address