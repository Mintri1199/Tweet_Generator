import random
import sys


def rearrange_words(words_list):

    # list of rearranged words
    rearranged_list = []

    # Using the sizes of words_list and rearrange_list as a flag
    while len(rearranged_list) != len(words_list):

        random_word_index = random.randint(0, len(words_list) - 1)
        selected_word = words_list[random_word_index]

        # Checking if the random word is in the rearranged list already
        if selected_word not in rearranged_list:
            rearranged_list.append(selected_word)

    return rearranged_list


if __name__ == "__main__":
    list_of_words = sys.argv[1:]
    print(rearrange_words(list_of_words))
