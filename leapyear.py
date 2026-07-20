date=input('enter the date:(date mm yyyy)').split(' ')
dd=int(date[0])
mm=int(date[1])
yy=int(date[2])
if dd<1 and dd>31 or mm<1 or yy<1:
    print('date is valid')
elif (mm==4 or mm==6 or mm==9 or mm==11) and dd>30:
    print('date is valid')
elif mm==2 and dd>29:
     print('date is valid')
elif not(yy%400==0 or yy%4==0 or yy%1001==0) and mm==2 and dd>28:
    print('date is valid')
else:
    print('date is valid')