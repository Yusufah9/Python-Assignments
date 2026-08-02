number_n = 5
number_of_count = 0

for number in range(1, 101):
    if number % number_n == 0:
       number_of_count+= 1

print(f"There are {number_of_count} multiples of {number_n} in the range.")

