class GF:
    def __init__(self,gname,gproperty):
        self.gname=gname
        self.gproperty=gproperty
    def display(self):
        print(f"{self.gname}{self.gproperty}")
class Father(GF):
    def __init__(self, gname, gproperty,fname,fproperty):
        super().__init__(gname, gproperty)
        self.fname=fname
        self.fproperty=fproperty
    def display(self):
        self.ftotal=self.fproperty+self.gproperty
        print(f"{self.ftotal}")
class son(Father):
    def __init__(self, gname, gproperty, fname, fproperty,sname,sproperty):
        super().__init__(gname, gproperty, fname, fproperty)
        self.sname=sname
        self.sproperty=sproperty
    def total(self):
        self.stotal=self.gproperty+self.fproperty+self.sproperty
    def display(self):
        print(f"Grand father name:{self.gname}, Property{self.gproperty},\nFather name:{self.fname},Property{self.fproperty},\nSon name:{self.sname},Property:{self.sproperty},\nTotal property of Son:{self.stotal}")

s=son("raja",50000,"ravi",30000,"raghu",10000)
s.total()
s.display()