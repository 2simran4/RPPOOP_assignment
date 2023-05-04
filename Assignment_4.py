class BankAccount:
    def __init__(self, name, account_number, account_type, balance):
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")
        else:
            print("Insufficient balance.")

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Account number: {self.account_number}")
        print(f"Account type: {self.account_type}")
        print(f"Balance: {self.balance}")


# Example usage:
bank_account = BankAccount("John Doe", "123456789", "Savings", 1000)

while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display account details")
    print("4. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter amount to deposit: "))
        bank_account.deposit(amount)
    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        bank_account.withdraw(amount)
    elif choice == 3:
        bank_account.display_details()
    elif choice == 4:
        break
    else:
        print("Invalid choice. Try again.")
