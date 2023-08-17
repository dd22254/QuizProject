import random


# main routine goes here
answer = ["correct", "incorrect"]
STARTING_BALANCE = 1

balance = STARTING_BALANCE
# Testing loop to generate 20 tokens
for item in range(0,100):
    chosen = random.choice(answer)

    # Adjust balance
    if chosen == "correct":
      balance += 4
    elif chosen == "incorrect":
      balance -= 1
    else:
      balance -= 0.5
    

print()
print("Starting Balance: $ {}".format(STARTING_BALANCE))
print("Fnal Balance: {}".format(balance))