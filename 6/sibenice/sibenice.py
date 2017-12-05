import random

alphabet = "abcdefghijklmnopqrsteuvwxyz"
words = ["guitar", "phone", "pencil", "moustache"]
random_word = random.choice(words)

missed_Letters = []
guessed_Letters = []


playing_field = "_ " * len(random_word)

def display_playing_board(playing_field, players_guess):
    if players_guess in random_word:
        playing_field = playing_field[0:random_word.index(players_guess)] + players_guess + playing_field[random_word.index(players_guess)]
    return playing_field

def get_players_guess():
    players_guess = input("Try a letter!").lower()
    return players_guess

players_guess = get_players_guess()

def evaluate_players_guess(players_guess):
    if players_guess not in alphabet:
        print("Not in the alphabet, dummy")
    elif players_guess in random_word:
        guessed_Letters.append(players_guess)
    elif players_guess not in random_word:
        missed_Letters.append(players_guess)
    elif players_guess in guessed_Letters or players_guess in missed_Letters:
        print("You already tried", players_guess.upper())

def turn(playing_field, position, players_guess):
    return playing_field[:position - 1] + players_guess + playing_field[position:]

def playing_the_game():
     while "_" in playing_field:
         letter = get_players_guess()
         evaluate_players_guess(letter)
         turn(playing_field, index.playing_field(players_guess), players_guess)

playing_the_game()
