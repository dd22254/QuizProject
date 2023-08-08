
def statement_generator(statement, decoration):

  sides = decoration * 3

  statement = "{} {} {}".format(sides, statement, sides)
  top_bottom = decoration * len(statement)

  print(top_bottom)
  print(statement)
  print(top_bottom)

  return ""
  
name = input("What is your name?")
print("Hi nice to meet you {}".format(name))

times = int(input("Please enter the times table you want to get tested on:"))
max_num = int(input("Enter the max number: "))
score = 1

for i in range(1, max_num):

    answer = i * times
    guess = int(input("What is {} x {} = ".format(i, times)))
    prize_decoration = "?"
    if guess != answer:
        statement_generator("Incorrect", "X")
        score -= 1

    else:
        statement_generator("Correct", "!")
        score += 1
