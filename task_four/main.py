'''
Task 4: Create a simple assistant bot that can do the following:
- Greet you when you start the program
- Say hello and ask how it can help you
- Add your name and phone number to a dictionary
- Change your phone number in the dictionary
- Get your phone number from the dictionary
- Get all the contacts in the dictionary
- Say goodbye and end the program
'''

def input_error(func):
    '''
    Decorator to handle input errors.
    '''
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Please enter a name and phone number."

    return inner

@input_error
def parse_input(user_input):
    '''
    Parse the user input and return the command and arguments.
    '''
    cmd, *args = user_input.split() # Split the input into command and arguments
    cmd = cmd.strip().lower() # Convert the command to lowercase
    args = [arg.lower() for arg in args] # Convert the arguments to lowercase
    return cmd, *args # Return the command and arguments

@input_error
def add_contact(args, contacts):
    '''
    Add a contact to the dictionary.
    '''
    name, phone = args # Unpack the arguments
    contacts[name] = phone # Add the contact to the dictionary
    return "Contact added." # Return a message

@input_error
def change_contact(args, contacts):
    '''
    Change the phone number of a contact in the dictionary.
    '''
    if len(args) != 2:
        return "Please enter a name and phone number." # Return a message
    name, phone = args # Unpack the arguments
    if name not in contacts: # Check if the contact is not in the dictionary
        return "Contact not found." # Return a message
    contacts[name] = phone # Change the phone number of the contact
    return "Contact changed." # Return a message

@input_error
def get_contact(name, contacts):
    '''
    Get the phone number of a contact from the dictionary.
    '''
    return contacts.get(name, "Contact not found.") # Return the phone number or a message

@input_error
def get_all_contacts(contacts):
    '''
    Get all the contacts from the dictionary.
    '''
    return contacts # Return the contacts

def main():
    '''
    Main function to run the assistant bot.
    '''
    contacts = {} # Create an empty dictionary to store contacts
    print("Welcome to the assistant bot!") # Greet the user
    while True: # Run the assistant bot in a loop
        user_input = input("Enter a command: ") # Get the user input
        command, *args = parse_input(user_input) # Parse the user input
        # print(f"Command: {command}, Arguments: {args}")
        # Print the command and arguments (for debugging)

        if command in ["close", "exit"]: # Check if the user wants to close the program
            print("Good bye!") # Say goodbye
            break # Exit the loop
        elif command == "hello": # Check if the user wants to be greeted
            print("How can I help you?") # Greet the user
        elif command == "add": # Check if the user wants to add a contact
            print(add_contact(args, contacts)) # Add the contact
        elif command == "change": # Check if the user wants to change a contact
            print(change_contact(args, contacts)) # Change the contact
        elif command == "phone": # Check if the user wants to get a contact's phone number
            print(get_contact(*args, contacts)) # Get the contact's phone number
        elif command == "all": # Check if the user wants to get all contacts
            print(get_all_contacts(contacts)) # Get all contacts
        else: # If the command is invalid
            print("Invalid command.") # Print an error message

if __name__ == "__main__":
    main()
# Run the assistant bot if the script is executed
