def main():
    print("\n--- Bulls and Cows Versus! ---")
    print(f"Each player picks a secret {DIGITS}-digit code with unique digits. Leading zeros allowed.")
    print("You and the computer will take turns guessing. First to guess opponent’s code wins (tie if same turn).")

    # Get difficulty
    while True:
        diff = input("Choose computer difficulty (easy/hard): ").strip().lower()
        if diff in ('easy', 'hard'):
            break
        print("Type 'easy' or 'hard'.")

    all_codes = all_possible_codes()
    # Player sets code
    player_secret = get_player_secret()
    # Computer sets code
    computer_secret = get_computer_secret(all_codes)
    # For computer guessing
    possible_codes = list(all_codes)  # For hard mode filtering
    computer_used = set()
    player_used = set()
    prev_computer_guess = None

    turn = 1
    player_won = False
    computer_won = False

    while True:
        print(f"\n--- Turn {turn} ---")
        # Player's turn
        print("\nYour turn to guess!")
        player_guess = get_player_guess(player_used)
        player_used.add(player_guess)
        pbulls, pcows = bulls_and_cows(computer_secret, player_guess)
        print(f"Bulls: {pbulls}, Cows: {pcows}")
        if pbulls == DIGITS:
            player_won = True

        # Computer's turn (only if player hasn't just won)
        print("\nComputer's turn to guess!")
        if diff == 'easy':
            comp_guess = computer_guess_easy(all_codes, computer_used, prev_computer_guess)
        else:
            comp_guess = computer_guess_hard(possible_codes, computer_used)
        if not comp_guess:
            print("Computer has no valid guesses left!")
            break
        print(f"Computer guesses: {comp_guess}")
        computer_used.add(comp_guess)
        cbulls, ccows = bulls_and_cows(player_secret, comp_guess)
        print(f"Computer Bulls: {cbulls}, Cows: {ccows}")
        prev_computer_guess = comp_guess
        if diff == 'hard':
            # Filter possible codes using feedback
            possible_codes = [
                code for code in possible_codes
                if bulls_and_cows(code, comp_guess) == (cbulls, ccows)
            ]
        if cbulls == DIGITS:
            computer_won = True

        # Endgame
        if player_won and computer_won:
            print("\nIt's a tie! Both guessed in the same round.")
            print(f"Secret was: {computer_secret}")
            break
        elif player_won:
            print("\nCongratulations! You guessed the computer’s secret code!")
            print(f"Computer's code: {computer_secret}")
            break
        elif computer_won:
            print("\nComputer guessed your secret code!")
            print(f"Your code was: {player_secret}")
            break

        turn += 1

if __name__ == "__main__":
    main()
