import random
total =0

my_number = random.randint(4, 150)

name = input("Enter your name: ")
print("Hi " ,name, ",Guess a number, any number, Can you guess the number? It’s between 4 and 151.")

while total < 10:
    guess = int(input("Enter your guess: ", ))

    total = total + 1

    if guess < my_number:
    print("The number I’m thinking of is higher.")

    if guess > my_number:
    print("The number I’m thinking of is lower.")

    if guess == my_number:
    total = str(total)
    print("Great job, " + name+ " you guessed my number in, " + total+ " attempts.")
    break
