def get_computer_secret(possible_codes):
    return random.choice(possible_codes)

def easy_update_candidates(candidates, last_guess, bulls, cows):
    # If last guess had 0 bulls and 0 cows, eliminate any code with any digit in last guess
    if bulls == 0 and cows == 0:
        bad_digits = set(last_guess)
        new_candidates = [c for c in candidates if not any(d in bad_digits for d in c)]
        return new_candidates
    # If last guess is correct, filter will not matter (handled elsewhere)
    # Otherwise, just remove the last guess to prevent repeats (sloppy filter)
    return [c for c in candidates if c != last_guess]

def computer_guess_easy(candidates, used_codes):
    # Pick random guess from unused candidates
    unused = [c for c in candidates if c not in used_codes]
    if not unused:
        return None
    return random.choice(unused)

def computer_guess_hard(candidates, used_codes):
    unused = [c for c in candidates if c not in used_codes]
    if not unused:
        return None
    return random.choice(unused)
