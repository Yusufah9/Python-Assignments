
user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [int(list_numbers) for list_numbers in user_input.split()]

even_numbers = 0
odd_numbers = 0

for number in numbers:
    if number % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1


print(f"There are: {even_numbers} even numbers, and There are: {odd_numbers} odd numbers.")

