p=int(input("enter phy marks"))
c=int(input("enter chm marks"))
m=int(input("enter math marks"))
b=int(input("enter bio marks"))

if p<35 or c<35 or m<35 or b<35:
    print('Fail')
else:
    print('Pass')
if p>=35 and c>=35 and m>=35 and b>=35:
    print('pass')
else:
    print('fail')