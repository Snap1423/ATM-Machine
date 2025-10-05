# Initalize 
balance = 50000 
pin = 2008

# Login
print('='*40)
print("Welcome to ATM")
print('='* 40)

# Enter your pin
while True:
    enter = int(input("Please Enter your pin: "))

    if enter == pin:
        print("Sucessful!✅")
        break
    else:
        print("Incorrect pin ❌, try again")

# Menu
while True:
    print("--------MENU-----------\n")
    print("1.Check Balance")
    print("2.Deposite Money💵")
    print("3.Withdraw Money💰")
    print("4.Exit")
    
    choice = int(input("Enter a choice: "))
    match choice:
        case 1:
            print(f"\nYour balance is {balance}")
        case 2:
            amount = int(input("Enter the Amount: "))
            balance+= amount
            print(f"\nYou have sucessfully deposited {amount} New balance: {balance}")
        case 3:
            amount = int(input("Enter the Amount: "))
            if balance<amount:
                print("❌Insufficient Balance")
            else:
                balance-=amount
                print(f"\nYou have sucessfuly withdrawed the amount{amount} Current balance: {balance}")
        case 4:
            print("\nThank you for using the ATM...Goodbye!")
            break
        case _:
            print("Invalid Choice ⚠️, try again")


