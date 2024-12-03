# file_handler.py
import csv

FILE_PATH = "data/contacts.csv"

def load_contacts():
    contacts = {}
    try:
        with open(FILE_PATH, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts[row["Phone"]] = row
    except FileNotFoundError:
        pass
    return contacts

def save_contacts(contacts):
    with open(FILE_PATH, mode="w", newline="") as file:
        fieldnames = ["Name", "Email", "Phone", "Address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts.values())
