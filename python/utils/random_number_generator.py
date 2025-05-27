import random

def random_number_generator_7digits():
    number = random.randint(1000000, 9999999)
    return number

def random_number_generator_3digits():
    number = random.randint(100, 999)
    return number

def random_number_generator_12digits() -> int:
    return random.randint(10**11, 10**12 - 1)