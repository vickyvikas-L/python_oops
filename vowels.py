st=input('enter the string')
st=st.lower()
vc=0
for x in st:
    if x=='a' or x=='e' or x=='i'or x=='o'or x=='u':
        vc=vc+1
        print('number of vowles: ',vc)


st=input('enter the string:')
vc=0
for ch in st:
    if ch in 'AEIOUaeiou':
        vc=vc+1
        print('number of vowles: ',vc)