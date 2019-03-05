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
        self.starter_histogram = {}  # Separate the start token from the stop token
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
        if key in self.starter_histogram:  # Found the key for in starter histogram
            self.starter_histogram[key] += 1
        else:
            self.starter_histogram[key] = 1

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
            # sentence = sentence.lower()

            list_of_words = sentence.split()
            list_of_words[-1] = list_of_words[-1].replace(".", "")

            if len(list_of_words) <= 2:  # Pass all sentences that are 2 words or less
                print(list_of_words)
                pass
            else:
                # Add the first pair into the dictionary of start token
                first_pair = (list_of_words[0], list_of_words[1])
                self.append_start_token(first_pair)
                # Add last pair with stop token
                last_pair = (list_of_words[-2], list_of_words[-1])
                self.append_stop_token(last_pair)
                for i in range(len(list_of_words) - 2):
                    word_pair = (list_of_words[i], list_of_words[i + 1])
                    self.append_to_dict_histogram(word_pair, list_of_words[i + 2])

    def run(self):
        """ This function will run the necessary functions to generate a Second Order Markov Chain sentence"""
        self.clean_up_text()
        self.creating_histograms(self.sentences_splitting())

        self.generate_sentence(self.start_the_sentence())

    def start_the_sentence(self):
        """ This function will return a word pair to that start the sentence """
        total_count = 0
        cum_prob = 0.0
        for key in self.starter_histogram.keys():
            total_count += self.starter_histogram[key]  # Get the counter value with the start token

        random_num = random.uniform(0, 1)
        for key in self.starter_histogram.keys():
            value = self.starter_histogram[key]  # Get the value with the key in the starter histogram
            cum_prob += value/total_count

            if cum_prob >= random_num:
                return key

    def sampling(self, key):
        """ This function will take a tuple of words, sample the next word and return a new tuple word pair"""
        total_count = 0
        cum_prob = 0
        random_num = random.uniform(0, 1)
        found_histogram = self.dictionary_of_histogram[key]

        for inner_key in found_histogram.keys():
            total_count += found_histogram[inner_key]

        for inner_key in found_histogram.keys():
            value = found_histogram[inner_key]

            cum_prob += value/total_count
            if cum_prob >= random_num:
                if inner_key == self.end_token:
                    print("Stop token was chosen")
                    return None
                else:
                    new_word_pair = (key[1], inner_key)
                    print(new_word_pair)
                    return new_word_pair

        print("Went through the list of keys")
        print(found_histogram)

    def generate_sentence(self, start_pair):
        """ This function will use start pair and then generate a sentence with it."""
        first_cap = start_pair[0].capitalize()  # Capitalize the first letter of the first word
        gen_sentence = "{} {}".format(first_cap, start_pair[1])
        ended = False
        new_word_pair = start_pair
        while ended is not True:
            new_word_pair = self.sampling(new_word_pair)
            if new_word_pair is None:
                ended = True
            else:
                gen_sentence += " " + new_word_pair[1]

        print(gen_sentence + ".")


markov = SecondOrderMarkov("queen_reign.txt")

markov.run()
