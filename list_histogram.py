import random

file = "queen_reign.txt"


# This function will clean up the text file of non alphabetic characters
def clean_up_text(file_name):
    with open(file_name) as f:

        # This line is from Zurich Okoren github
        punctuation_table = str.maketrans('\n-', '  ', '''1234567890~!@#$.,%^&*()_+?/`[];'":|♔''')

        mostly_filtered_text = f.read().translate(punctuation_table).replace('--', ' ')
        mostly_filtered_text = mostly_filtered_text.replace('\ufeff', '')
        text_list = mostly_filtered_text.lower().split()

        # This is how list comprehension work
        for index in range(len(text_list)):
            text_list[index] = text_list[index].strip()

        return text_list


# This function will takes a histogram argument return the total count of unique words in the histogram
def unique_words(words_list):
    list_of_unique_words = []
    for word in words_list:
        if word not in list_of_unique_words:
            list_of_unique_words.append(word)

    return list_of_unique_words


# This function will takes a word and histogram argument and returns the number of times that word appears in a text.
def frequency(keyword, list_of_words):
    times = 0
    for word in list_of_words:
        if word == keyword:
            times += 1
    return times


# Creating a histogram as a list of lists
def listogram(word_list):
    list_of_list = []

    # Inspired by Sam Harrison
    for word in word_list:
        found = False                       # Flag to signify duplication
        for value in list_of_list:
            if word in value[0]:
                found = True
                value[1] += 1

        if not found:
            list_of_list.append([word, 1])

    print(len(list_of_list))
    print(list_of_list)


# Creating a histogram as a dictionary
def dictogram(word_list):

    dict_of_histo = {}

    for word in word_list:
        if word not in dict_of_histo:
            dict_of_histo[word] = 1
        else:
            dict_of_histo[word] += 1

    print(dict_of_histo)


# Creating a histogram as a list of tuples
def tupogram(word_list):
    list_of_tuple = list()

    list_of_tuple.append((word_list[0], 1))
    for word in word_list:
        found = False
        for index, value in enumerate(list_of_tuple):
            if value[0] == word:                        # If the word equates to the tuple index 0
                found = True                            # Change the flag to True to prevent adding extra tuples
                num = value[1] + 1                      # Store the freq number incremented by 1
                list_of_tuple.pop(index)                # pop the current tuple
                list_of_tuple.append((word, num))       # Append a new one with same word and incremented num
                break                                   # Break to prevent the loop from going once it found the word
        if not found:
            list_of_tuple.append((word, 1))

    print(list_of_tuple)


fish = ["red", "fish", "yellow", "fish", "green", "fish"]

#listogram(clean_up_text(file))
#dictogram(clean_up_text(file))
tupogram(clean_up_text(file))

