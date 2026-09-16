class BankCustomer:

    def __init__(self, name, account_number, balance):
        self.__name = name
        self.__account_number = account_number
        self.__balance = balance

    # Getter for name
    def get_name(self):
        return self.__name

    # Getter for account number
    def get_account_number(self):
        return self.__account_number

    # Getter for balance
    def get_balance(self):
        return self.__balance

    # Withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return 0


class Bank:

    def __init__(self):
        self.customers = []

    # Add customer
    def add_customer(self, customer):
        self.customers.append(customer)

    # Find customer by account number
    def find_customer_by_account(self, account_number):
        for customer in self.customers:
            if customer.get_account_number() == account_number:
                return customer
        return None


# Driver program
customer1 = BankCustomer("Geetha", "ACC1001", 50000)
customer2 = BankCustomer("Mohitha", "ACC1002", 30000)

bank = Bank()

# Add customers
bank.add_customer(customer1)
bank.add_customer(customer2)

# Find customer
customer = bank.find_customer_by_account("ACC1001")

if customer:
    print("Customer Name:", customer.get_name())
    print("Account Number:", customer.get_account_number())
    print("Current Balance:", customer.get_balance())

    # Successful withdrawal
    amount = customer.withdraw(10000)

    if amount > 0:
        print("Withdrawn Amount:", amount)
        print("Balance After Withdrawal:", customer.get_balance())

    # Withdrawal exceeding balance
    amount = customer.withdraw(50000)

    if amount == 0:
        print("Withdrawal failed: Insufficient balance")
    else:
        print("Withdrawn Amount:", amount)