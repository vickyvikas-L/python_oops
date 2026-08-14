class Biodata:
   def input(self):
      self.name=input("enter the name:")
      self.age=int(input("enter the age:"))
      self.course=input("enter the course:")
      self.mother_name=input("enter the mother_name:")
      self.father_name=input("enter the father_name:")
      self.mobile_number=int(input("enter the mobile_number:"))
   def display(self):
       print("\nBiodata")
       print(f"Name :{self.name}")
       print(f"age :{self.age}")
       print(f"course :{self.course}")
       print(f"mother_name :{self.mother_name}")
       print(f"father_name :{self.father_name}")
       print(f"mobile_number :{self.mobile_number}")
        
bio=Biodata()
bio.input()
bio.display()