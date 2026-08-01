n=int(input("Enter a number: "))
for i in range(n,0,-1):
    for col in range (1,i+1):
        if (col==1 or col==i or i==n):
            print("*",end=" ")
        else:   
            print(" ",end=" ") 
    print()