

# Functions go here...
def yes_no(question):
    valid = False
    while not valid:
            response = input(question).lower()
    

            if response == "yes" or response == "y":
                response = "yes"
                return response

            elif response == "no" or response == "n":
                response = "yes"
                return response
            
            else:
                print("Please answer yes / no")


# Main Routine goes here...
played_before = yes_no("Have you played the game before? ")
if played_before == "no":
  print("Display Instructions")

elif played_before == "yes":
  print("Program continues")