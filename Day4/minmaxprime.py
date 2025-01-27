def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
arr =[]
for i in range(1000):
    if isprime(i):
        arr.append(i)
        break
for i in range(1000,0,-1):
    if isprime(i):
        arr.append(i)
        break
print("The minimum prime number is: ",arr[0])
print("The maximum prime number is: ",arr[1])
