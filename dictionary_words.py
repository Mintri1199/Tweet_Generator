import random
import sys
from datetime import datetime
from pathlib import Path


def random_word(num):
    num = int(num)
    # Turn the argument into num

    data_folder = Path("/usr/share/dict/words")

    file_to_open = data_folder

    with open(file_to_open, 'r') as f:
        dict_list = f.readlines()

        words_list = random.choices(dict_list, k=num)
        for index, word in enumerate(words_list):
            words_list[index] = word.rstrip()
        print(" ".join(words_list))


if __name__ == "__main__":
    start_time = datetime.now()
    param = sys.argv[1:]
    random_word(param[0])
    print(datetime.now() - start_time)
