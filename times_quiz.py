



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
  print("How to Play", "#")
  print()
  print("The rules of the Maths Quiz go here", "~")
  print()
  return ""

#Main routine goes here...
name = input("Hi what is your name?")
print("Nice to meet you {}!".format(name))

# Main Routine goes here...
played_before = yes_no("Have you played any Maths Quiz before? ")

if played_before == "no":
  instructions()

times = int(input("Please enter the times table you wan to get tested on:"))
max_num = int(input("Enter the max number: "))
score = 0

for i in range(1, max_num):

    answer = i * times
    guess = int(input("What is {} x {} = ".format(i, times)))
    if guess != answer:
        score -= 1
        print("Incorrect you got {} points".format(score))

    else:
        score += 1
        print("Correct you got {} points".format(score))

print("Final Score: {}".format(score))
