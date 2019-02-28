import random
import nltk
nltk.download('punkt')


class ActualMarkovChain:

    def __init__(self, file_name):
        self.file_name = file_name
        self.large_text = ""
        self.types = 0
        self.tokens = 0
        self.list_of_starter_words = []  # This is will the list of words that start a sentence [(key, value)]
        self.list_of_histograms = []    # This will be an array of tuples [[key,(types, value)]]

    def run(self):
        """ This function will run the necessary functions to generate a Markov Chain sentence"""
        self.clean_up_text()
        self.sentences_splitting()

        for sentence in self.sentences_splitting():
            self.histogram(sentence)

        print(len(self.list_of_starter_words))
        for histogram in self.list_of_histograms:
            print(histogram)
        # print(self.list_of_histograms[5])

    def clean_up_text(self):
        """ This function will open the text file and clean it then assign the cleaned text to a stored value"""
        with open(self.file_name) as f:

            # This line is from Zurich Okoren github
            punctuation_table = str.maketrans('\n-', '  ', '''1234567890~!@#$,%^&*()_+?/`[];'":|♔''')

            mostly_filtered_text = f.read().translate(punctuation_table).replace('--', ' ')
            mostly_filtered_text = mostly_filtered_text.replace('\ufeff', '')
            self.large_text = mostly_filtered_text

    def getting_types(self):
        """ This function will get the types of the text"""

    def sentences_splitting(self):
        """ This function will split the text into an array of sentences
            TODO: Call this function AFTER the text has been cleanse"""

        sentences = nltk.sent_tokenize(self.large_text)  # This will give an array with all the sentences
        for sentence in sentences:
            sentence = sentence.replace(".", "")

        return sentences

    def appending_to_starting_word_list(self, starting_word):
        """ This function will handle of appending to the starting_words histogram"""
        found_start_word = False
        for key_value in self.list_of_starter_words:
            # key_value = (type, counter)
            if key_value[0] == starting_word:
                found_start_word = True
                counter = key_value[1]
                self.list_of_starter_words.remove(key_value)
                self.list_of_starter_words.append((starting_word, counter + 1))
                break

        if not found_start_word:
            self.list_of_starter_words.append((starting_word, 1))

    def appending_to_list_of_histograms(self, key, next_word):
        """ This function will handle appending to the list of histogram"""
        found_hist_key = False

        for outer_key_value in self.list_of_histograms:
            # outer_key_value = [key, [histogram that is in tuples]
            if outer_key_value[0] == key:   # The corresponded histogram has been found
                found_hist_key = True
                found_type = False
                for inner_key_value in outer_key_value[1]:
                    # inner_key_value = (type, counter)
                    if inner_key_value[0] == next_word:  # Found an existing type
                        found_type = True
                        counter = inner_key_value[1]
                        outer_key_value[1].remove(inner_key_value)
                        outer_key_value[1].append((next_word, counter + 1))
                        break
                if not found_type:  # Did not found type
                    outer_key_value[1].append((next_word, 1))

        if not found_hist_key:  # Starting new histogram
            self.list_of_histograms.append([key, [(next_word, 1)]])

    def counting_stops(self, key):
        """ This function will handle counting the stop token"""
        stop_key = "#STOP#"
        found_histogram = False
        found_stop = False

        for outer_key_value in self.list_of_histograms:  # Loop through the list if histograms
            if outer_key_value[0] == key:   # Finding the correct histogram
                found_histogram = True
                for inner_key_value in outer_key_value[1]:  # Loops through the array of key value pairs
                    if inner_key_value[0] == stop_key:      # Found a stop token
                        found_stop = True
                        counter = inner_key_value[1]
                        outer_key_value[1].remove(inner_key_value)
                        outer_key_value.append((stop_key, counter + 1))
                        break

                if not found_stop:  # Create the first stop token
                    outer_key_value[1].append((stop_key, 1))

        if not found_histogram:  # Creating the histogram that the stop token is it first token
            self.list_of_histograms.append([key, [(stop_key, 1)]])

    def histogram(self, one_sentence):
        """ This function will take one sentence and make a histogram
            If there are duplicate then it would append to the existing histogram """
        split_sentence = one_sentence.split()   # Split the sentence into an array of words with the first word

        self.appending_to_starting_word_list(split_sentence[0])  # Take care of the first word of the sentence

        last_index = len(split_sentence) - 1

        self.counting_stops(split_sentence[last_index])     # Take care of the last word in the sentence

        for count in range(len(split_sentence)):
            if (count + 1) >= len(split_sentence):
                break
            current_word = split_sentence[count]
            next_word = split_sentence[count + 1]
            self.appending_to_list_of_histograms(current_word, next_word)


markov = ActualMarkovChain("smaller_text.txt")

markov.run()

