def replace(index, items):
    replacement = input("What should replace the item? ")
    items[int(index)] = replacement


def validate_input(index):
    if index not in ["0", "1", "2"]:
        print("Not a valid index")
        exit()


def should_we_carry_on():
    carry_on_choice = input("Would you like to carry on (y / n) ? ")
    if carry_on_choice not in ["y", "n"]:
        print("I'm sorry, I don't understand your selection. Exiting.")
    if carry_on_choice == "y":
        return True
    else:
        return False


def play():
    things = ["First", "Second", "Third"]
    carry_on = True
    while carry_on:
        print("The items are:", things)
        choice = input("Choose an index of a item to replace (0, 1 or 2) ? ")
        validate_input(choice)
        replace(choice, things)
        print("The new items are:", things)
        carry_on = should_we_carry_on()