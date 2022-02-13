import time

water_tank_max_depth = 120


def check_tank(current_level):
    percent_depth = current_level / water_tank_max_depth
    message = "All is well (no pun intended)."
    if percent_depth < 0.2:
        message = "The tank needs to be filled out."
    if percent_depth >= 1:
        message = "The tank is full, please switch off the pump."
    return message


def monitor():
    for x in range(0, 130, 10):
        depth = float(input("What is the depth? "))
        print(check_tank(depth))
        time.sleep(10)
