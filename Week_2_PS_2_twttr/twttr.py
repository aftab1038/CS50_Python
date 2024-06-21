# Taking input {text}
text = input("Input: ")

# looping through each character of inputted text to checking either each character is vowel or not
i = 0
while i < len(text):
    # Replacing vowel with "*"
    if text[i] in ["a", "A", "e","E", "i", "I", "o", "O", "u", "U"]:
       text = text.replace(text[i], "*")
    i += 1

# Remove * from the text and print the text without vowels
print("Output:", text.replace("*", ""))
