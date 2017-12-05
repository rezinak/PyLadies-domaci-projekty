import random
from obrazky import pictures

alphabet = "abcdefghijklmnopqrsteuvwxyz"
words = ["guitar", "phone", "pencil", "moustache"]

def get_input():
    while True:
        user_input = input("Try a letter: ").lower()
        if user_input in alphabet:
            return user_input
        else:
            print("Not in the alphabet, dummy")

def display_board(field, wrong_count, pictures):
    print(pictures[wrong_count])
    print(field)

def turn(field, letter, secret):
    pos = 0
    result = field

    for i in range(secret.count(letter)):
        pos = secret.index(letter, pos)
        result = result[0:pos] + letter + result[pos + 1:]
        pos += 1

    return result

secret_word = random.choice(words)
field = "." * len(secret_word)
wrong_count = 0

while True:
    display_board(field, wrong_count, pictures)

    if field == secret_word:
        print("Yay!")
        break

    if wrong_count == len(pictures) - 2:
        print("Ses mrtvej!")
        break

    letter = get_input()

    if letter in secret_word:
        field = turn(field, letter, secret_word)
    else:
        wrong_count += 1
