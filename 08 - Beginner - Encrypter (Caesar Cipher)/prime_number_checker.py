n = int(input("Type a number to check if it's a prime number: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n}, is not a prime number.")
            break
        else:
            print(f"{n}, is a prime number.")
            break
else:
    print("1 is not a prime number.")
