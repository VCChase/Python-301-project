from pathlib import Path

#* Change file name/path for recording transactions if you wish
file = "python_301_project.txt"

class Bank:
    def __init__(self, file):
        self.file = file
        self.balance = self._get_balance()
    
    def _get_balance(self):
        path = Path(self.file)
        if path.is_file():
            with open(file, "rb") as f:
                f.seek(-10, 2)
                chars = f.read().decode("utf-8").split()
                return float(chars[-1])
        else:
            return 0

    def _check_input(self, user_input):
        user_input = user_input.strip("$ ")
        if user_input[0] == "-" or user_input == "0":
            print(f"{user_input} is not a valid amount.")
            return False
        
        try:
            user_input = float(user_input)
            return round(user_input, 2)
        except:
            print(f"{user_input} is not a valid number")
            return False

    def _record_transaction(self, transaction, amount):
        f = open(self.file, "a")
        f.write(f"{amount} {transaction}. New balance: {self.balance}\n")
        f.close()


    def menu(self):
        while True:
            user = input("What would you like to do? You can type balance, deposit, withdraw, or exit. ").strip().lower()

            match user:
                case "balance":
                    self._check_balance()
                case "deposit":
                    self._deposit()
                case "withdraw":
                    self._withdraw()
                case "exit":
                    print("Goodbye.")
                    break
                case _:
                    print(f"Sorry, {user} is not a valid response.")

    def _check_balance(self):
        print(f"Your acount balance is ${self.balance:.2f}")
    
    def _deposit(self):
        for x in range(2, -1, -1): 
            amount = input("How much would you like to deposit? ")
            amount = self._check_input(amount)

            if amount:
                self.balance += amount
                self._record_transaction("deposited", amount)
                print(f"You have deposited ${amount:.2f}. Your new balance is ${self.balance:.2f}")
                break
            else:
                print(f"{x} attempt(s) remaining.")

        else:
            print("Returning to menu.")
    
    def _withdraw(self):
        for x in range(2, -1, -1):
            amount = input("How much would you like to withdraw? Whole dollar amounts only. ")
            amount = self._check_input(amount)
            attempts = f"{x} attempt(s) remaining."

            if not amount:
                print(attempts)
            elif amount < 1:
                print(f"Withdrawal amount cannot be less than $1. {attempts}")
            elif amount > self.balance:
                print(f"You do not have sufficient funds for that transaction. {attempts}")
            else:
                amount = int(amount)
                self.balance -= amount
                self._record_transaction("withdrawn", amount)
                print(f"You have withdrawn ${amount:.2f}. Your new balance is ${self.balance:.2f}")
                break

        else:
            print("Returning to menu.")

new_bank = Bank(file)
new_bank.menu()
