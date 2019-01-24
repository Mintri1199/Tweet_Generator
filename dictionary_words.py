import random
import sys
from pathlib import Path


def random_word(num):
    # Turn the argument into num 
    wanted_word = int(num)

    data_folder = Path("/usr/share/dict/words")

    file_to_open = data_folder

    f = open(file_to_open)

    # The words file is not a list thus we need to split it in order to get a word for a index
    # If not we will get a letter for our index
    dict_list = f.read().split()
    
    words_list = []

    while len(words_list) != wanted_word:

        random_index = random.randint(0, len(dict_list) - 1)
        selected_word = dict_list[random_index]

        if selected_word not in words_list:
            words_list.append(selected_word)

    print(words_list)


if __name__ == "__main__":
    param = sys.argv[1:]
    random_word(param[0])
