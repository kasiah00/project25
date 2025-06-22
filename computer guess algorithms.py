def get_computer_secret(possible_codes):
    return random.choice(possible_codes)

def easy_update_candidates(candidates, last_guess, bulls, cows):
    if bulls == 0 and cows == 0:
        bad_digits = set(last_guess)
        return [c for c in candidates if not any(d in bad_digits for d in c)]
    elif bulls + cows > 0:
        required_matches = bulls + cows
        return [c for c in candidates if len(set(c) & set(last_guess)) >= required_matches and c != last_guess]
    else:
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
