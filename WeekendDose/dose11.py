
user_input = int(input("Enter a number: "))

is_prime = True
if user_input < 2:
    is_prime = False
else:
    for number in range(2, int(user_input ** 0.5) + 1):
        if user_input % number == 0:
            is_prime = False
            break

if is_prime:
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.")

print(f"\nPrime numbers between 1 and {user_input}:")
for number in range(2, user_input + 1):
    for prime_numbers in range(2, int(number**0.5) + 1):
        if number % prime_numbers == 0:
            break
    else:
        print(number, end="  ")
print()

