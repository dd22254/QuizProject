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

def instructions():
  print()
  print("How to Play")
  print()
  print("The rules of the quiz go here")
  print()
  return ""

# Functions go here...
def num_check(question, low, high):
  error = "Please enter an whole number between 1 and 10\n"

  valid = False
  while not valid:
    try:
      # ask the question
      response = int(input(question))

      # if the amount is too low / too high give
      if low < response <= high:
        return response

      # output an error
      else:
        print(error)

    except ValueError:
      print(error)

# Main Routine goes here...
played_before = yes_no("Have you played the game before? ")

if played_before == "yes":
  instructions()
print()
print("Quiz Continues")

# Main routine goe here
print()
how_much = num_check("How much would you like to play with? ", 0, 10)
print()
print("You will be spending ${}".format(how_much))
