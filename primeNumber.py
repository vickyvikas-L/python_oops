n=int(input('enter the value of n'))
count=1
for i in range(1,n//2+1):
    if n%i==0:
        count=count+1

if count==2:
    print(n,' is a prime number')
else:
    print(n,' is not a prime number')