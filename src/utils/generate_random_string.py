from string import ascii_lowercase, digits
import random


def get_random_string(length=20) -> str:
    all_symbols = ascii_lowercase + digits
    generated_string = ''.join([
        random.choice(all_symbols) for _ in range(length)
    ])
    return generated_string
