user_input = int(input("Enter a number: "))
reversed_numbers = 0


while user_input > 0:
    digit = user_input % 10
    reversed_numbers = reversed_numbers * 10 + digit
    user_input = user_input // 10

print(reversed_numbers)

