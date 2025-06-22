def get_computer_secret(possible_codes):
    return random.choice(possible_codes)

def mutate_code(prev_guess, all_codes, used_codes):
    # Mutate previous guess: swap two digits or change one digit to another (unique digits preserved)
    guess_list = list(prev_guess)
    if random.random() < 0.5:  # swap two digits
        i, j = random.sample(range(DIGITS), 2)
        guess_list[i], guess_list[j] = guess_list[j], guess_list[i]
    else:  # change one digit
        idx = random.randrange(DIGITS)
        available_digits = [d for d in '0123456789' if d not in guess_list or d == guess_list[idx]]
        available_digits.remove(guess_list[idx])
        if available_digits:
            guess_list[idx] = random.choice(available_digits)
    new_guess = ''.join(guess_list)
    # Ensure valid, unique, unused
    if len(set(new_guess)) == DIGITS and new_guess not in used_codes and new_guess in all_codes:
        return new_guess
    # Otherwise, fallback: random code not used
    options = [c for c in all_codes if c not in used_codes]
    return random.choice(options) if options else None

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
