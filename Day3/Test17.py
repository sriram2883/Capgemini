inp = input("Enter the sentence").split()
set1 = set(inp)
for i in set1:
    print(i, ":", inp.count(i))
