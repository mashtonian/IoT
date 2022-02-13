def celsius_to_fahrenheit(celsius):
    return float(celsius) * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (float(fahrenheit) - 32) * 5 / 9


def pounds_to_kilograms(pound):
    return float(pound) / 2.205


def kilograms_to_pounds(kg):
    return float(kg) * 2.205


def generic_conversion(form, units, forward_fn, backward_fn):
    measure = input("What is the " + form + " to be converted? ")
    unit = input("Is that in " + units[0][0] + " or " + units[1][0] + "  (" + units[0][1] + " / " + units[1][1] + ")? ")
    if unit not in [units[0][1], units[1][1]]:
        print("I'm sorry I don't understand that choice, exiting.")
    else:
        if unit == units[0][1]:
            print("That is", round(forward_fn(measure), 2), units[1][0] + ".")
        else:
            print("That is", round(backward_fn(measure), 2), units[0][0] + ".")


def convert():
    generic_conversion("temperature", [["Celsius", "c"], ["Fahrenheit", "f"]],
                       celsius_to_fahrenheit, fahrenheit_to_celsius)

    generic_conversion("weight", [["Pounds", "p"], ["Kilograms", "k"]],
                       pounds_to_kilograms, kilograms_to_pounds)




