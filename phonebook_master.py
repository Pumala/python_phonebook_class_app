import pickle
from os.path import exists

file_name = "phonebook_master.pickle"

class Phonebook_Dict(object):
    def __init__(self, phonebook_name):
        self.contact = []

    def lookup_entry(self):
        name = raw_input("\nName? ")
        for index in range(0, len(self.contact)):
            is_found = False
            if self.contact[index]["name"] == name:
                print "\nFound entry for %s" % self.contact[index]["name"]
                print "Email: %s" % self.contact[index]["email"]
                print "Work Number: %s" % self.contact[index]["phone"]["work"]
                print "Home Number: %s" % self.contact[index]["phone"]["home"]
                print "Cell Number: %s" % self.contact[index]["phone"]["cell"]
                is_found = True
                break
        if is_found == False:
            print "%s does not exist." % name
        else:
            pass

    def add_entry(self):
        name = raw_input("\nName? ")
        email = raw_input("Email? ")
        work_number = raw_input("Work number? ")
        home_number = raw_input("Home number? ")
        cell_number = raw_input("Cell number? ")
        self.contact.append({"name": name, "email": email, "phone" : {"work": work_number, "home": home_number, "cell": cell_number}})
        print "Entry stored for %s." % name

    def delete_entry(self):
        name = raw_input("\nName? ")
        for index in range(0, len(self.contact)):
            is_found = False
            # print index
            if self.contact[index]["name"] == name:
                del self.contact[index]
                print "Deleted entry for %s" % name
                is_found = True
                break
        if is_found == False:
            print "%s does not exist." % name
        else:
            pass

    def print_all_entries(self):
        for index in range(0, len(self.contact)):
            print "\nFound entry for %s: " % self.contact[index]["name"]
            print "Email: %s" % self.contact[index]["email"]
            print "Work Number: %s" % self.contact[index]["phone"]["work"]
            print "Home Number: %s" % self.contact[index]["phone"]["home"]
            print "Cell Number: %s \n" % self.contact[index]["phone"]["cell"]

    def save_entry(self, phonebook_name):
        phonebook_file = open(file_name, "w")
        pickle.dump(phonebook_name, phonebook_file)
        phonebook_file.close()
        print "Saving entries..."

    def __repr__(self):
        return "%s" % self.name

if exists(file_name):
    phonebook_file = open(file_name, "r")
    master_phonebook = pickle.load(phonebook_file)
    phonebook_file.close()
    print "Loading file..."
else:
    master_phonebook = Phonebook_Dict("Master Phonebook")
    print "Creating new file..."

while True:
    print "\nElectronic Phone Book"
    print "====================="

    print "1. Look up an entry"
    print "2. Set an entry"
    print "3. Delete an entry"
    print "4. List all entries"
    print "5. Save"
    print "6. Quit"

    choice = int(raw_input("\nWhat do you want to do? "))

    if choice == 1:
        master_phonebook.lookup_entry()
    elif choice == 2:
        master_phonebook.add_entry()
    elif choice == 3:
        master_phonebook.delete_entry()
    elif choice == 4:
        master_phonebook.print_all_entries()
    elif choice == 5:
        master_phonebook.save_entry(master_phonebook)
    elif choice == 6:
        print "Bye"
        break
    else:
        # Prompt user to select from the menu or exit the session
        print "Please choose a list from the following or pick 6 to quit."


# sarah = Phonebook_Dict("Sarah's Phone Book")
# sarah.add_entry()
# sarah.add_entry()
# sarah.lookup_entry()
# print sarah.contact
# sarah.print_all_entries()
# sarah.delete_entry()
# sarah.print_all_entries()

# master_phonebook = Phonebook_Dict("Master Phonebook")
