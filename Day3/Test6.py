def check_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    else:
        return False
start  = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
for i in range(start, end+1):
    if check_prime(i):
        print(i, end=" ")
