
word = str(input("Enter a particular word of your choice: "))

word_length = len(word)

if word_length < 5:
    print("Short string")

elif 5 <= word_length <= 10:
    print("Medium string")
else:
    print("Long string")

