import random
import sys
from datetime import datetime

"""
First attempt and unoptimized
def rearrange_words(words_list):

    # list of rearranged words
    rearranged_list = []

    # Using the sizes of words_list and rearrange_list as a flag
    while len(rearranged_list) != len(words_list):

        random_word_index = random.randint(0, len(words_list) - 1)
        selected_word = words_list[random_word_index]

        # This check for duplication words
        if rearranged_list.count(selected_word) < words_list.count(selected_word):
            rearranged_list.append(selected_word)

        # Checking if the random word is in the rearranged list already
        if selected_word not in rearranged_list:
            rearranged_list.append(selected_word)

    return " ".join(rearranged_list)
"""


# Yates' shuffle
def rearrange_redux(words_list):
    list_length = len(words_list)

    for i in range(list_length):
        rand_index = random.randint(i, list_length - 1)
        words_list[i], words_list[rand_index] = words_list[rand_index], words_list[i]

    return " ".join(words_list)


if __name__ == "__main__":
    start_time = datetime.now()
    list_of_words = sys.argv[1:]
    print(rearrange_redux(list_of_words))
    print(datetime.now() - start_time)
