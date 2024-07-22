def main():
    # Taking input {word}
    word = input("Input: ")
    # print word without vowels
    print("Output:", shorten(word))

 # function to return modified version of inputted word by removing vowels
def shorten(word):
    # variable to store modified version of inputted word with only consonant
    mod_word = ""
    # looping through each character to identify consonant
    i = 0
    while i < len(word):
        # store consonant in mod_word varible
        if not word[i] in ["a", "A", "e","E", "i", "I", "o", "O", "u", "U"]:
           mod_word += word[i]
        i += 1
    # return modified version of inputted word
    return mod_word

if __name__ == "__main__":
    main()
