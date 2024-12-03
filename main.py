# main.py
from contact_manager import add_contact, view_contacts, delete_contact, search_contacts
from file_handler import load_contacts, save_contacts
from utils import validate_name, validate_phone, validate_email

contacts = load_contacts()

def main():
    global contacts

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Search Contacts")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                name = input("Enter Name: ")
                validate_name(name)
                email = input("Enter Email: ")
                validate_email(email)
                phone = input("Enter Phone: ")
                validate_phone(phone)
                address = input("Enter Address: ")
                add_contact(name, email, phone, address)
                save_contacts(contacts)
                print("Contact added successfully!")
            except ValueError as ve:
                print(f"Error: {ve}")
            except Exception as e:
                print(f"Unexpected error: {e}")
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            phone = input("Enter phone number of the contact to delete: ")
            if delete_contact(phone):
                save_contacts(contacts)
                print("Contact deleted successfully!")
            else:
                print("Contact not found.")
        elif choice == "4":
            query = input("Enter name or part of the name to search: ")
            results = search_contacts(query)
            if results:
                for result in results:
                    print(result)
            else:
                print("No matching contacts found.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    contacts.update(load_contacts())
    main()
