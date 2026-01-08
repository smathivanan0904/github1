class ATM:
    def __init__(self):
        self.users = {
            "1001": {"pin": "1234", "name": "Arun", "balance": 5000, "history": []},
            "1002": {"pin": "5678", "name": "Bala", "balance": 8000, "history": []}
        }

    def login(self):
        acc = input("Enter Account Number: ")
        pin = input("Enter PIN: ")

        if acc in self.users and self.users[acc]["pin"] == pin:
            print(f"\nWelcome {self.users[acc]['name']} 👋")
            self.menu(acc)
        else:
            print("❌ Invalid Account or PIN")

    def menu(self, acc):
        while True:
            print("\n----- ATM MENU -----")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Mini Statement")
            print("6. Exit")

            choice = input("Choose option: ")

            if choice == "1":
                self.check_balance(acc)
            elif choice == "2":
                self.deposit(acc)
            elif choice == "3":
                self.withdraw(acc)
            elif choice == "4":
                self.transfer(acc)
            elif choice == "5":
                self.mini_statement(acc)
            elif choice == "6":
                print("Thank you! Visit again.")
                break
            else:
                print("Invalid option!")

    def check_balance(self, acc):
        bal = self.users[acc]["balance"]
        print(f"Your Balance: ₹{bal}")

    def deposit(self, acc):
        amt = int(input("Enter amount to deposit: "))
        self.users[acc]["balance"] += amt
        self.users[acc]["history"].append(f"Deposited ₹{amt}")
        print(f"₹{amt} deposited successfully")

    def withdraw(self, acc):
        amt = int(input("Enter amount to withdraw: "))
        if amt <= self.users[acc]["balance"]:
            self.users[acc]["balance"] -= amt
            self.users[acc]["history"].append(f"Withdrawn ₹{amt}")
            print(f"₹{amt} withdrawn successfully")
        else:
            print("❌ Insufficient balance")

    def transfer(self, acc):
        to_acc = input("Enter receiver account number: ")
        amt = int(input("Enter amount to transfer: "))

        if to_acc in self.users:
            if amt <= self.users[acc]["balance"]:
                self.users[acc]["balance"] -= amt
                self.users[to_acc]["balance"] += amt
                self.users[acc]["history"].append(f"Transferred ₹{amt} to {to_acc}")
                self.users[to_acc]["history"].append(f"Received ₹{amt} from {acc}")
                print("Transfer successful ")
            else:
                print("❌ Insufficient balance")
        else:
            print("❌ Receiver account not found")

    def mini_statement(self, acc):
        print("\n--- Mini Statement ---")
        if not self.users[acc]["history"]:
            print("No transactions yet")
        else:
            for i in self.users[acc]["history"][-5:]:
                print(i)
atm = ATM()
atm.login()
