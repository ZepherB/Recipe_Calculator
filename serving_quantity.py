# function goes below

def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("Please enter a valid number")


# Main routine goes below

name = not_blank("Serving Quantity: ")
name = not_blank("Portion Size: ")
