
word = input("Enter a particular word of your choice: ")

if word[0].islower():
    print("This is a lowercase")
elif word[0].isupper():
    print("This is an Uppercase")
else:
    print("The first character is not a letter")

