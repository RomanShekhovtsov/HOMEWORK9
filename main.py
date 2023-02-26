CONTACTS = {}

def add_change_comand(comand):
    comand = comand.split(" ")
    CONTACTS[comand[1].capitalize()] = comand[2]


def phone_comand(comand):
    comand = comand.split(" ")
    phone = CONTACTS[comand[1].capitalize()]
    return phone


def show_all_comand(CONTACTS):
    str_dict = ""
    for key, value in CONTACTS.items():
        str_dict += f"{key}: {value} \n"
    str_dict = str_dict[:-2]
    return str_dict


def input_error(func):
    try:
        func()
    except KeyError:
        print("Enter user name ")
    except ValueError:
        print("Give me name and phone please ")
    except IndexError:
        print("Give me name and phone please ")

    return func()


@input_error
def main():
    while True:
        comand = input(" ")

        if comand.casefold() == "hello":
            print("How can I help you?")

        elif "add" in comand.casefold() or "change" in comand.casefold():
            add_change_comand(comand)
            print("Contact saved")

        elif "phone" in comand.casefold():
            print(f"phone {phone_comand(comand)}")

        elif "show all" in comand.casefold():
            print(f"Your contacts:\n {show_all_comand(CONTACTS)} ")

        if comand.casefold() == "good bye" or comand.casefold() == "close" or comand.casefold() == "exit":
            print("Good bye!")
            break


if __name__ == "__main__":
    main
