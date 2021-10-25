EXPECTED_BAKE_TIME = 40


def bake_time_remaining(minutes):
    if minutes > 40 or minutes < 0:
        print("The lasagna is overcooked! Get it out of the oven immediately!")

    else:
        time_left = EXPECTED_BAKE_TIME - minutes
        return time_left
       # print(f"The lasagna should be left in the oven for {time_left} more minutes!")



# bake_time_remaining(27)


def preparation_time_in_minutes(num):
    val = num * 2
    return val

# preparation_time_in_minutes(4)

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    layers = preparation_time_in_minutes(number_of_layers)
    elapsed_time = layers + elapsed_bake_time
    return elapsed_time

print(f"You have spent {elapsed_time_in_minutes(1, 3)} minutes making your lasagna!")
