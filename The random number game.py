# This game consist in guessing a random
# number in less that determinate number
# of attemps.

import random
import time


def need_a_number(user_input):
    while not user_input.isnumeric():
        time.sleep(.4)
        print("\nThat's not a number. 😒")
        time.sleep(1)
        user_input = input("\nYou'd better try again: ")
    return int(user_input)


print("Hey!")
time.sleep(1)
input("( You are supposed to hit ENTER each time I talk. 😊 )")
time.sleep(.2)
input("That's it 😁")
time.sleep(.6)

input("\nI'm the COMPUTER! HO-HO-HO!")
time.sleep(.6)
input("\nWell... not really. I'm basically just a bunch of code...")
time.sleep(.6)
input("\nBut stop talking and lets play the game :D")
time.sleep(.6)


player_name = input("\nFirst. What's your name? ").capitalize()
while player_name == "":

    for i in range(3):
        time.sleep(.6)
        print(". ")

    time.sleep(3)
    print("If you don't want to use your name you can fake one...")
    time.sleep(3)
    player_name = input("Aaaaaand your name is... ^^u\n").capitalize()


time.sleep(.6)
input(f"\nHello {player_name}. I'm gonna choose a number between 0 and 20.")
time.sleep(.6)
input("\nWhat you have to do is guess it in the minimum number of attemps.")
time.sleep(.6)
is_the_player_ready = input("\nAre you ready? ")
while is_the_player_ready.lower() != "yes":
    time.sleep(.5)
    print('\nYou were supposed to say "Yes". Is not that difficult.\n')
    time.sleep(.5)
    is_the_player_ready = input("Are you ready? ")

random_number = random.randint(0, 20)
time.sleep(.5)
guessed_number = input("\nThen what's your first guess? ")
guessed_number = need_a_number(guessed_number)

attemps = 1

while guessed_number != random_number:
    if guessed_number > random_number:

        time.sleep(.5)

        guessed_number = input("\nSeems too hight. Guess again: ")

        guessed_number = need_a_number(guessed_number)

    else:
        time.sleep(.5)
        guessed_number = input("\nSeems too low. Guess again: ")
        guessed_number = need_a_number(guessed_number)

    attemps += 1

time.sleep(2)
print(f"\nCongrats, {player_name}. You guessed it in {attemps} attemps.")
