st=input("enter the string:")
a=set('abcdefghijklmnopqrstuvwxyz')

if a.issubset(st):
     print('string is pangram')
else:
    print('string is not pangram') 