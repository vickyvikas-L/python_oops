class addition:
    def in_put(self):
        self.num1 = int(input("enter the num"))
        self.num2 = int(input("enter the num"))
    def calculate(self):
        self.num3=self.num1+self.num2
    def display(self):
       print(f"{self.num3}")
ad=addition()
ad.in_put()
ad.calculate()
ad.display()