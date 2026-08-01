n=int(input("enter the digit:"))
for row in range (n,0,-1):
    for col in range (n-row):
        
        print(" ",end=" ")
        
    for col in range(row,0,-1):
        print(col,end=" ")
    print()