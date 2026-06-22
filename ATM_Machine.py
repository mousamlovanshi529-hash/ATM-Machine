# ****Program to create an ATM Machine ****

print("====Welcome to the ATM Machine====")

password = 1234
balance = 100000

# List to store transaction history
transection = []

# Variables for PIN attempts
attempt = 0
max_attempt = 3

# Loop for PIN verification
while attempt < max_attempt:
    pin = int(input("Enter the password: "))

    # Check if entered PIN is correct
    if pin == password:
        print("------Access Granted------")

        # ATM menu loop
        while True :
            print("Select an option to perform an operation: ")
            print("1. check balance")
            print("2. Deposit money ")
            print("3. Withdraw Mony")
            print("4. Mini Statement ")
            print("5. Exit")

            choice = int(input("enter an option between 1 to 5 : "))

            # Option 1: Check balance
            if choice == 1 :
                print("**Your current balance is** Rs. = " , balance)

            # Option 2: Deposit money
            elif choice == 2 :
                deposit = int(input("Enter the amount: "))
                balance = balance + deposit
                transection.append(f"Deposited : Rs. {balance}")
                print("**Deposit succesfully and the total balance** Rs. = ",balance)

           # Option 3: Withdraw money
            elif choice == 3 :
                Withdraw = int(input("Enter the amount to Withdraw Rs. : "))

                # Check if sufficient balance is available
                if Withdraw <= balance :
                    balance = balance - Withdraw
                    transection.append(f"Withdraw: Rs. {Withdraw}")
                    print(" congratulation Withdraw Rs. " , Withdraw, "succesfully  and the ramaining balance is Rs. ", balance)

                else :
                    print("Invelaid balance ! plesase try again ")

           # Option 4: Show mini statement
            elif choice == 4 :
                print("--------Mini Statement---------")

                # Check if any transaction exists
                if not transection :
                    print("No transection yett !")

                else :
                    # Display available balance
                    for t in transection:
                        print("Available balance is Rs. ", balance)

           # Option 5: Exit ATM
            elif choice == 5 :
                print("Thank you for using ATM Machine ! please visit again.")
                break

             # Invalid menu choice
            else :
                print("Invelaid input ! please Select between 1 to 5 ")
                break

     # Wrong PIN entered
    else :
        attempt = attempt  + 1 
        ramaining = max_attempt - attempt
        print("Incorrect pin ! Attempt left : ", ramaining) 

        # Block account after 3 wrong attempts
        if ramaining == 0 :
            print("Account blocked ! please try again after some time " )
            break