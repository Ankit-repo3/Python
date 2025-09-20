# ATM Project
Balance = 5000
atm_pin = 4321

pin = int(input("Enter your 4 digit ATM Pin: "))

if pin == atm_pin:
    print("Pin is correct \nWelcome to ATM")
    while True:
        print("\n----Menu----")
        print("1. Check Balance")
        print("2. Exit")
        choice = int(input("Enter your choice (1-2): "))
        if choice == 1:
            print("Your current balance is:", Balance)
        elif choice == 2:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print("Incorrect Pin. Please try again.")
