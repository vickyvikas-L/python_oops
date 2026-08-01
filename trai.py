n=int(input("Enter a number: "))
for row in range(n):
   for col in range (n-row-1):
       print(" ",end="")
   for col in range (row+1):
       if(row==n-1 or col==row or row==0 or col==0):
           print("*",end="")
       else:
           print(" ",end="")
   print()