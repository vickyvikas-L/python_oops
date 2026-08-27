class Bank:
    def bank_details(self):
        print("Bank: ABC Bank")


class Account(Bank):
    def account_details(self):
        print("Account Number: 12345")


class SavingsAccount(Account):
    def savings_details(self):
        print("Account Type: Savings")
        print("Interest Rate: 5%")


s = SavingsAccount()

s.bank_details()
s.account_details()
s.savings_details()