# String reversals: reverse words, sentences
def string_reversal(string):
    reverse_string = ""
    length_of_string = len(string)

    for i in range(1, length_of_string + 1):
        reverse_string += string[-i]
    print(reverse_string)


string_reversal("Hello World")
