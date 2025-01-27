D1= {}#empty dictionary
D2= {'food':2,'clothes':3,'shelter':4}
D3 = {'food':{'has':2,'needs':3}}
D4 = dict(food=2,clothes=3,shelter=4)
names = ['food','clothes','shelter']
values = [2,3,4]
D5 = dict(zip(names,values))
D6 = dict.fromkeys(names)
print("D1: ",D1)
print("D2: ",D2)
print("D3: ",D3)
print("D4: ",D4)
print("D5: ",D5)
print("D6: ",D6)
D2['food'] = 5