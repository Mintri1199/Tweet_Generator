import random
import sys
from datetime import datetime
from pathlib import Path


def random_word(num):
    """ This function will take number and return a string with random words from the dictionary file"""
    num = int(num)
    # Turn the argument into num

    data_folder = Path("/usr/share/dict/words")

    file_to_open = data_folder

    with open(file_to_open, 'r') as f:
        dict_list = f.readlines()
        word_list = []

        for i in range(0, num):
            word_list.append(dict_list[random.randrange(len(dict_list))].strip())

        print(" ".join(word_list))


if __name__ == "__main__":
    start_time = datetime.now()
    param = sys.argv[1:]
    random_word(param[0])
    print(datetime.now() - start_time)
