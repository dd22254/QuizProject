

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
  statement_generator("How to Play", "#")
  print()
  statement_generator("The rules of the game go here", "~")
  print()
  print("In every rounds yuo'll get 10IQ (it reminds as your points)")
  print()
  print("From each round you will get a donkey, a zebra, a horse and if you're lucky you will get a unicorn.")
  print()
  print("Here's the payout amounts...")
  print()
  print("Unicorn: $5.00, balance will increase by $4")
  print("Horse: $0.50, balance will decrease by $0.50 ")
  print("Zebra: $0.50, balance will decrease by $0.50")
  print("Donkey: $0.00, balance will decrease by $1.00")
  print()
  print("Hint: Try to avoid the donkey and try to get the unicorn so your balance will increse")
  return ""

def statement_generator(statement, decoration):

  sides = decoration * 3

  statement = "{} {} {}".format(sides, statement, sides)
  top_bottom = decoration * len(statement)

  print(top_bottom)
  print(statement)
  print(top_bottom)

  return ""

# Main routine goes here
statement_generator("Welcome to the Lucky Unicorn Game", "*")
print()

# Main Routine goes here...
played_before = yes_no("Have you played the game before? ")

if played_before == "yes":
  instructions()

# Main Routine goes here...
played_before = yes_no("Have you played any maths quiz before game before? ")
print("You chose {}".format(played_before))