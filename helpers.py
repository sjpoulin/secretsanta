import random

# Credit: https://stackoverflow.com/questions/15512058/python-shuffle-such-that-position-will-never-repeat

def shuffle_list(some_list):
    randomized_list = some_list[:]
    while True:
        random.shuffle(randomized_list)
        for a, b in zip(some_list, randomized_list):
            if a == b:
                break
        else:
            return randomized_list
