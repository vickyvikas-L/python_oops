
class father():
    def property(self,fname,land):
        self.fname=fname
        self.land=land
    def display(self):
        print(self.fname,self.land)
class son(father):
    def son_property(self,sname,sland):
        self.sname=sname
        self.sland=sland
    def sdisplay(self):
        self.total_land=self.land+self.sland
        print(self.sname,self.fname,self.total_land)
s=son()
s.son_property("vikas",30)
s.property("lakshman",40)
s.sdisplay()