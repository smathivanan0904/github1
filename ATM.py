# ATM.py
# Non-interactive version for Jenkins CI

def login():
    # Predefined credentials (for CI execution)
    account_number = "123456"
    pin = "1234"

    print("=== ATM LOGIN ===")
    print("Account Number:", account_number)

    if pin == "1234":
        print("Login successful")
        return True
    else:
        print("Invalid PIN")
        return False


def check_balance():
    balance = 5000
    print("Current Balance: ", balance)


def withdraw():
    balance = 5000
    withdraw_amount = 1000
    print("Withdraw Amount: ", withdraw_amount)

    if withdraw_amount <= balance:
        balance -= withdraw_amount
        print("Withdrawal successful")
        print("Remaining Balance: ", balance)
    else:
        print("Insufficient balance")


def main():
    print("=== ATM SYSTEM STARTED ===")

    if login():
        check_balance()
        withdraw()

    print("=== ATM SYSTEM COMPLETED ===")


# Program execution starts here
if __name__ == "__main__":
    main()
