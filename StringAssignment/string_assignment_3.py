
word = input("Enter a Three Letter word of your choice: ")

word = word.lower()

if len(word) != 3:
    print("Error: The word must be exactly 3 letters long.")

reverse = ""

for letter in word:
    reverse = letter + reverse

if word == reverse:

    print("This is a palindrome")
else:
    print("This is not a palindrome")




//Write a method for sum of factor of a number that is a perfect number true or false

