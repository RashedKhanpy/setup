# contact_manager.py
contacts = {}
def add_contact(name, email, phone, address):
        """
        Add a new contact to the contacts dictionary.
        Raises an error if the phone number already exists.
        """
        if phone in contacts:
            existing_name = contacts[phone]["Name"]
            raise ValueError(f"The phone number {phone} is already assigned to {existing_name}.")
        contacts[phone] = {"Name": name, "Email": email, "Phone": phone, "Address": address}

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\n--- Contact List ---")
        for phone, details in contacts.items():
            print(f"Name: {details['Name']}, Email: {details['Email']}, Phone: {details['Phone']}, Address: {details['Address']}")

def delete_contact(phone):
    if phone in contacts:
        del contacts[phone]
        return True
    return False

def search_contacts(query):
    results = [details for details in contacts.values() if query.lower() in details['Name'].lower()]
    return results
