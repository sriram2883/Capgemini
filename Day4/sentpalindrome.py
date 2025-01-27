sentence = "hey this is    sis"
lis = []
space = False
for i in sentence:
    if  i == ' ' and space == False:
        space = True
        lis.append(i)
    elif i != ' ':
        space = False
        lis.append(i)
print("".join(lis))