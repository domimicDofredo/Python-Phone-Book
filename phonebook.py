from pickle import dump
from pickle import load

class Contact:
    def __init__(self, name, num):
        self.name = name
        self.num = num

class Phonebook:
    def __init__(self):
        self.contacts = list()
 
    def add(self, name, num):
        contact = Contact(name, num)
        self.contacts.append(contact)

    def display(self):
        for contact in self.contacts:
            print('Name:', contact.name)
            print('#:', contact.num, end='\n\n')
    
    def display_this(self, name):
        for contact in self.contacts:
            if name == contact.name:
                print('Name:', contact.name)
                print('#:', contact.num)
    
    def edit(self, name):
        for contact in self.contacts:
            if name == contact.name:
                new_name = input('New name: ')
                new_num = input('New #: ')

                contact.name = new_name
                contact.num = new_num
    
    def delete(self, name):
        for contact in self.contacts:
            if name == contact.name:
                self.contacts.remove(contact)
    
    def sort(self):
        self.contacts.sort(key=lambda con: con.name)

class WrongCommand(Exception):
    def __init__(self, command):
        Exception.__init__(self)
        self.command = command

def display_menu():
    print('''
    Available commands:
    
        display - Dsiplay contacts
        display [name] - Display specific contact
        add - Add contact
        edit [name] - Edit existing contacts
        delete [name] - Delete contact
        sort - Sort the contacts
        exit - Exit
    ''')


def execute(args):
    try:
        command = args[0]
        name = ''

        if len(args) == 2:
            name = args[1]
        
        if 'add' == command:
            name = input('Name: ')
            num = input('#: ')
            phonebook.add(name, num)

        elif 'display' == command:
            phonebook.display()
        
        elif 'display' == command:
            phonebook.display_this(name)

        elif 'edit' == command:
            phonebook.edit(name)
        
        elif 'delete' == command:
            phonebook.delete(name)
        
        elif 'sort' == command:
            phonebook.sort()
        
        else:
            raise WrongCommand(args)
    except WrongCommand as e:
        print("Wrong command: '{}'".format(' '.join(e.command)))


f = None
phonebook = Phonebook()

try:
    f = open('phonebook.bin', 'rb')
    phonebook = load(f)
    f.close()

except FileNotFoundError:
    pass

while True:
    display_menu()
    args = tuple(input('>> ').split())

    if args[0] == 'exit':
        break

    execute(args)

f = open('phonebook.bin', 'wb')
dump(phonebook, f)
f.close()


