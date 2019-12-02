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
