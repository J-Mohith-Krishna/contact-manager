class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def __str__(self):
        return f"Name: {self.name}, Phone Number: {self.phone_number}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact removed successfully.")
                return
        print("Contact not found.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print("Contact found:")
                print(contact)
                return
        print("Contact not found.")

    def view_contacts(self):
        if self.contacts:
            print("Contacts:")
            for contact in self.contacts:
                print(contact)
        else:
            print("No contacts available.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\n1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. View Contacts")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter contact phone number: ")
            contact = Contact(name, phone_number)
            contact_manager.add_contact(contact)
        elif choice == '2':
            name = input("Enter contact name to remove: ")
            contact_manager.remove_contact(name)
        elif choice == '3':
            name = input("Enter contact name to search: ")
            contact_manager.search_contact(name)
        elif choice == '4':
            contact_manager.view_contacts()
        elif choice == '5':
            print("Thank you for using Contact Manager!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
