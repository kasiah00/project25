import random

DIGITS = 4

def all_possible_codes():
    # Generate all 4-digit numbers with unique digits (allow leading zeros)
    codes = []
    for i in range(10**DIGITS):
        s = f"{i:0{DIGITS}d}"
        if len(set(s)) == DIGITS:
            codes.append(s)
    return codes

def valid_code(code):
    return (len(code) == DIGITS and code.isdigit() and len(set(code)) == DIGITS)

def bulls_and_cows(secret, guess):
    bulls = sum(a == b for a, b in zip(secret, guess))
    cows = sum((min(secret.count(x), guess.count(x)) for x in set(guess))) - bulls
    return bulls, cows

def get_player_secret():
    while True:
        code = input(f"Enter your secret {DIGITS}-digit code (unique digits, leading zeros allowed): ")
        if valid_code(code):
            return code
        print("Invalid code. Please ensure 4 digits, all unique, leading zero allowed.")

def get_player_guess(prev_guesses):
    while True:
        code = input(f"Your guess: ")
        if valid_code(code) and code not in prev_guesses:
            return code
        print("Invalid or already guessed. Please try again.")
