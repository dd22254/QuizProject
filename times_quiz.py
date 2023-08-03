
name = input("What is your name?")
print("Welcome to the times table quiz {}".format(name))

times = int(input("Please enter the times table you want to get tested on:"))
max_num = int(input("Enter the max number: "))
score = 0

for i in range(1, max_num):

    answer = i * times
    guess = int(input("What is {} x {} = ".format(i, times)))
    if guess != answer:
        print("incorrect")
    else:
        print("Correct")
        score += 1

