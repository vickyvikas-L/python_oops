n=int(input("Enter a number: "))
for i in range(n):
    for col in range (i+1):
        if (col==0 or col==i or i==n-1):
            print("*",end=" ")
        else:   
            print(" ",end=" ") 
    print()