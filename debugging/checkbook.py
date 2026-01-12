#!/usr/bin/python3

class Checkbook:
    """
    A simple Checkbook class to manage deposits, withdrawals, and balance checking.
    """

    def __init__(self):
        """
        Function Description:
            Initialize a Checkbook instance with a starting balance of 0.0.

        Parameters:
            None

        Returns:
            None
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function Description:
            Add the given amount to the account balance and print the updated balance.

        Parameters:
            amount (float): The amount of money to deposit.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function Description:
            Withdraw the given amount from the account balance if funds are sufficient.

        Parameters:
            amount (float): The amount of money to withdraw.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function Description:
            Display the current account balance.

        Parameters:
            None

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Function Description:
        Main interactive loop for the Checkbook program. Prompts the user
        to deposit, withdraw, check balance, or exit. Handles invalid inputs gracefully.

    Parameters:
        None

    Returns:
        None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Amount cannot be negative.")
                    continue
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Amount cannot be negative.")
                    continue
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
