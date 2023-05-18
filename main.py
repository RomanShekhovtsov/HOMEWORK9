contacts= {}

def parse_command(command):
    keywords = command.lower().split()
    return keywords

def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact '{name}' with phone '{phone}' has been added."
def change_phone(name, phone):
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for contact '{name}' has been changed to '{phone}'."
    else:
        raise KeyError(f"Contact ''{name} does not exist.")
def get_phone(name):
    if name in contacts:
        return f"Phone number for contact '{name}' is '{contacts[name]}'."
    else:
        raise KeyError(f"Contact '{name}' does not exist.")
def show_all_contacts():
    if contacts:
        result = "Contacts: \n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return  result.strip()
    else:
        return "No contacts found"
def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError as e:
            return str(e)
        except ValueError:
            return "Invalid input"
        except IndexError:
            return "Not enaugh arguments"
    return wrapper

@input_error
def main():
    print("Welcome to console Assisnant")
    while True:
        command = input("Enter a command: ")
        keywords = parse_command(command)
        if keywords[0] == "hello":
            print("How can I help you?")
        elif keywords[0] == "add":
            name = keywords[1]
            phone = keywords[2]
            print(add_contact(name, phone))
        elif keywords[0] == "change":
            name = keywords[1]
            phone = keywords[2]
            print(change_phone(name, phone))
        elif keywords[0] == "phone":
            name = keywords[1]
            print(get_phone(name))
        elif keywords[0] == "show" and keywords[1] == "all":
            print(show_all_contacts())
        elif keywords[0] == "good" and keywords[1] == "bye":
            print("Good bye!")
            break
        else:
            print("Unknown command.")
if __name__=="__main__":
    main()

