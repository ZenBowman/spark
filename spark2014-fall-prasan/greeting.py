
def greeting(time):
    if (time > 600) and (time < 1159):
        print("Good morning")
    elif (time > 1200) and (time < 1559):
        print("Good afternoon")
    elif (time > 1600) and (time < 1959):
        print ("Good evening")
    else:
        print("Good night")

def convert_to_screen_space(x, y):
    new_x = x * 100
    new_y = y * 100
    return new_x, new_y
