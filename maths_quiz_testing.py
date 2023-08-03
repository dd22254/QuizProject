


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
  statement_generator("The rules of the game go here", "~")
  print()
  statement_generator("How to Play", "#")
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

def statement_generator(statement, decoration):

  sides = decoration * 3

  statement = "{} {} {}".format(sides, statement, sides)
  top_bottom = decoration * len(statement)

  print(top_bottom)
  print(statement)
  print(top_bottom)

  return ""

# Main routine goes here
statement_generator("Welcome to the Maths Quiz", "*")
print()
name = input("Hi what is your name? ")
print()
print("Hi nice to meet you {}".format(name))

# Main Routine goes here...
print()
played_before = yes_no("Have you played any maths quiz before? ")
print()
print("You chose {}".format(played_before))

if played_before == "yes":
  instructions()
print()
print("Maths Quiz Continues")
print()
statement_generator("Let's get started", "^")

# Main routine goe here
print()
how_much = num_check("How much would you like to play with? ", 0, 10)
print()
print("You will be spending ${}".format(how_much))

