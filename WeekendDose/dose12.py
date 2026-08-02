secret_number = 100

while True:
    choice = input("\nEnter a number: ")
    
    
    guess = int(choice)
    
    if guess < secret_number:
        print("Too low, try again!")
    elif guess > secret_number:
        print("Too high, try again!")
    else:
        print("Congratulations! You have won!")
        break 

