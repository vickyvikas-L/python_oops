class bank_acc:
    acc_count = 0

    def __init__(self, acno, acname, balance, accstatus):
        self.acno = acno
        self.acname = acname
        self.balance = balance
        self.accstatus = accstatus
        bank_acc.acc_count += 1
class savingsac(bank_acc):
    accstatus = "savingsac"

    def cal(self, interest):
        self.interest = interest
        self.total = self.balance * self.interest / 100
        self.balance += self.total
class premium(savingsac):
    accstatus = "premium"
    @classmethod
    def acc_no(cls):
        cls.acc_count += 1
    @staticmethod
    def int(rate):
        return 0 <= rate <= 10
    def display(self):
        print(f"{self.acno}, {self.acname}, {self.balance}, {self.accstatus}")


b = bank_acc(123, "vikas", 50000, "normal")
s = savingsac(124, "vikas", 50000, "savingsac")
s.cal(7.5)
print(s.balance)
p = premium(125, "vikas", 50000, "premium")
p.display()
print(bank_acc.acc_count)
print(premium.int(7.5)) 