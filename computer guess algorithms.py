def computer_guess_easy(all_codes, used_codes, prev_guess):
    # 70% chance random, 30% mutate previous guess (never repeat, not using feedback)
    unused_codes = [c for c in all_codes if c not in used_codes]
    if not unused_codes:
        return None
    if prev_guess and random.random() < 0.3:
        guess = mutate_code(prev_guess, all_codes, used_codes)
        if guess: return guess
    return random.choice(unused_codes)

def computer_guess_hard(possible_codes, used_codes):
    # Always pick from remaining consistent codes
    unused_codes = [c for c in possible_codes if c not in used_codes]
    if not unused_codes:
        return None
    return random.choice(unused_codes)
