number = int(input("Enter any number: "))
steps = 0

while number > 1:
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1
    steps += 1
print(f"Total steps: {steps}")
