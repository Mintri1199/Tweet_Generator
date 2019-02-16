import random, sys
from histograms import clean_up_text

word_list = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']


class Markov:

    def __init__(self, list_of_words):
        self.word_list = list_of_words
        self.sentence = ""
        self.tokens = 0
        self.types = 0
        self.histograms = {}  # A dictionary of histogram {key: [word, counter]}

    def getting_types(self):
        """ This method will get all the types in the word list."""
        for word in self.word_list:
            if word not in self.histograms:
                self.histograms[word] = []
                self.types += 1

    def appending_value(self, key, next_word):
        """ This method will appending or increment the 'next word' in the type's histogram"""
        found = False

        for value in self.histograms[key]:
            if value[0] == next_word:
                value[1] += 1
                self.tokens += 1
                found = True
                break

        if not found:
            self.histograms[key].append([next_word, 1])
            self.tokens += 1

    def logic(self):
        """ This method will loop for the size of the word list and get the next word then call appending_value"""
        for count in range(len(self.word_list)):
            if (count + 1) >= len(self.word_list):          # Check if the loop is on it second last item
                self.tokens += 1
                break
            next_word = self.word_list[count + 1]
            self.appending_value(self.word_list[count], next_word)

    def counter(self, key):
        """This method will return the total sum of the type histogram"""
        count = 0
        for word_count in self.histograms[key]:
            count += word_count[1]

        return count

    def sample_word(self, key):
        """ This method will take a sample word from the type histogram"""
        total = self.counter(key)
        cum_prob = 0
        random_num = random.uniform(0, 1)
        for word_count in self.histograms[key]:
            cum_prob += word_count[1]/total
            if cum_prob >= random_num:
                self.sentence += word_count[0] + " "
                return word_count[0]

    def multiple_runs(self, num):

        initial = random.choice(self.word_list)

        key = initial
        for i in range(num):
            key = self.sample_word(key)

        print(self.sentence)

    def run(self):
        self.getting_types()
        self.logic()
        print(self.histograms)
        print("{} types".format(self.types))
        print("{} tokens".format(self.tokens))


if __name__ == "__main__":

    params = sys.argv[1:3]
    num = int(params[0])
    start = Markov(clean_up_text("queen_reign.txt"))
    start.getting_types()
    start.logic()
    start.multiple_runs(num)







