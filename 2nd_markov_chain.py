import random, sys
from histograms import clean_up_text
import nltk
nltk.download('punkt')


class SecondOrderMarkov:

    def __init__(self, file_name):
        self.file_name = file_name
        self.start_token = '#####'
        self.end_token = '/////'
        self.large_text = ""
        self.types = 0
        self.tokens = 0
        self.list_of_tuple = []  # This list will keep reference of all the starting word pairs
        # Initialized a dictionary of histogram along with a empty Starting histogram
        self.dictionary_of_histogram = {}

    def clean_up_text(self):
        """ This function will open the text file and clean it then assign the cleaned text to a stored value"""
        with open(self.file_name) as f:

            # This line is from Zurich Okoren github
            punctuation_table = str.maketrans('\n-', '  ', '''1234567890~!@#$,%^&*()_+?/`[];'":|♔''')

            mostly_filtered_text = f.read().translate(punctuation_table).replace('--', ' ')
            mostly_filtered_text = mostly_filtered_text.replace('\ufeff', '')
            self.large_text = mostly_filtered_text

    def sentences_splitting(self):
        """ This function will split the text into an array of sentences
            TODO: Call this function AFTER the text has been cleanse"""

        sentences = nltk.sent_tokenize(self.large_text)  # This will give an array with all the sentences
        for sentence in sentences:
            sentence = sentence.replace(".", "")

        # Return a list of sentences without the period
        return sentences

    def append_start_token(self, key):
        # key = (str, str)
        # Checking if the word pairs already exist
        if key in self.dictionary_of_histogram:  # Found the key for histogram
            found_histogram = self.dictionary_of_histogram[key]
            # found_histogram = { str : num }
            if self.start_token in found_histogram:    # Found the start token in the found histogram
                found_histogram[self.start_token] += 1
            else:   # Create a new dictionary
                found_histogram[self.start_token] = 1
                self.list_of_tuple.append(key)
        else:
            self.dictionary_of_histogram[key] = {self.start_token: 1}
            self.list_of_tuple.append(key)

    def append_to_dict_histogram(self, key, next_word):
        # key = (str, str)
        if key in self.dictionary_of_histogram:  # Found the key for histogram
            found_histogram = self.dictionary_of_histogram[key]
            if next_word in found_histogram:    # Found the next_word in the found histogram
                found_histogram[next_word] += 1
            else:   # Create a new dictionary
                found_histogram[next_word] = 1
        else:
            self.dictionary_of_histogram[key] = {next_word: 1}

    def append_stop_token(self, key):
        # key = (str, str)
        # Checking if the word pairs already exist
        if key in self.dictionary_of_histogram:  # Found the key for histogram
            found_histogram = self.dictionary_of_histogram[key]
            # found_histogram = { str : num }
            if self.end_token in found_histogram:    # Found the start token in the found histogram
                found_histogram[self.end_token] += 1
            else:   # Create a new dictionary
                found_histogram[self.end_token] = 1
        else:
            self.dictionary_of_histogram[key] = {self.end_token: 1}

    def creating_histograms(self, list_of_sentences):
        # list_of_sentences = [str]
        for sentence in list_of_sentences:
            sentence.lower()
            list_of_words = sentence.split()
            if len(list_of_words) == 1:
                print(list_of_words)
                pass
            else:
                first_pair = (list_of_words[0], list_of_words[1])
                self.append_start_token(first_pair)

                for i in range(len(list_of_words) - 2):
                    word_pair = (list_of_words[i], list_of_words[i + 1])
                    self.append_to_dict_histogram(word_pair, list_of_words[i + 2])

                # After the loop end
                last_pair = (list_of_words[-2], list_of_words[-1])
                self.append_stop_token(last_pair)

    def run(self):
        """ This function will run the necessary functions to generate a Markov Chain sentence"""
        self.clean_up_text()
        self.creating_histograms(self.sentences_splitting())

        print(self.dictionary_of_histogram)


markov = SecondOrderMarkov("smaller_text.txt")

markov.run()
