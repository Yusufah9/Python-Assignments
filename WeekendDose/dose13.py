balance = 1000

while True:
    print("\n--- ATM MENU ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print(f"Successfully deposited N{amount:.2f}")
        else:
            print("Invalid amount. Please enter an amount from 1 - 1_000_1000")
            
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        if amount > balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid amount.")
        else:
            balance -= amount
            print(f"Successfully withdrew N{amount:.2f}")
            
    elif choice == "3":
        print(f"Your current balance is: N{balance:.2f}")
        
    elif choice == "4":
        print("Thank you for using Yusuf's ATM. Goodbye! See you soon")
        break
        
    else:
        print("Invalid choice. Please select a valid option.")

