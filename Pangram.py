st=input("enter the string:")
st=st.upper()
alph=set()
for ch in st:
     if ch.isalpha():
          alph.add(ch)

if len(alph)==26:
     print('string is pangram')
else:
     print('string is not pangram')
