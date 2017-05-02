"""This is a Terminal-based program that allows a user to create and edit a to-do list.

The stub of each function has been provided. Read the docstrings for what each 
function should do and complete the body of the functions below.

You can run the script in your Terminal at any time using the command:

    >>> python todo_list.py

"""

def add_to_list(my_list):
    """Takes user input and adds it as a new item to the end of the list."""

    item = (raw_input("What would you like to add to the list? ")).lower()
    
    if len(my_list) == 0:
        my_list.append(item)
    else:
        for i in my_list:
            if i == item:
                print "This is already on the list."
                print i, item            # if item == i:
                # print "You already have that."
            else:
                my_list.append(item)

    print my_list

def view_list(my_list):
    """Print each item in the list."""

    for item in my_list:
        print item

    preference = (raw_input("Would you like to see the list in alphabetical order? ")).lower()
    if preference == "yes":
        for item in my_list:
            print item
    else:
        print "Ok."

    option = (raw_input("Would you like to see a certain number of items? ")).lower()
    if option == "yes":
        view_certain_number_in_list(my_list)
    else:
        print "Ok."

    another_option = (raw_input("Would you like to see a portion of the list? ")).lower()
    if another_option == "yes":
        view_slices_of_list(my_list)

def view_certain_number_in_list(my_list):
    number = int(raw_input("How many items do you want to see? "))
    for i in range(number):
        print my_list[i]

def view_slices_of_list(my_list):
    portion_start = int(raw_input("At which index do you want to start? "))
    portion_end = int(raw_input("At which index do you want to end? "))
    for i in range(portion_start, portion_end + 1):
        print my_list[i]

def delete_from_beginning_of_list(my_list):
    if len(my_list) == 0:
        print "There is nothing to delete. Add some items first."
    else:
        del my_list[0]

def add_to_list_at_an_index(my_list):
    item = raw_input("What would you like to add to the list? ")
    location = int(raw_input("At which index do you want to add your item? "))    
    my_list.insert(location, item)

def edit_an_item_at_an_index(my_list):
    location = int(raw_input("At which index do you want to edit? "))
    edit = raw_input("What is the edited version of the item? ")
    my_list[location] = edit
    
def display_main_menu(my_list):
    """Displays main options, takes in user input, and calls view or add function."""

    user_options = """
    \nWould you like to:
    A. Add a new item
    B. View list
    C. Delete from beginning of list
    D. Add to list at an index
    E. Edit an item at an index
    F. Quit the program
    >>> """

    

    while True:
        user_input = (raw_input(user_options)).upper()
        # Collect input and include your if/elif/else statements here.
        if user_input == "A":
            add_to_list(my_list)
        elif user_input == "B":
            view_list(my_list)
        elif user_input == "C":
            delete_from_beginning_of_list(my_list)
        elif user_input == "D":
            add_to_list_at_an_index(my_list)
        elif user_input == "E":
            edit_an_item_at_an_index(my_list)
        elif user_input == "F":
            break
        else:
            print "Sorry, you need to type in a valid option.  Try again."
#-------------------------------------------------

my_list = []
display_main_menu(my_list)

