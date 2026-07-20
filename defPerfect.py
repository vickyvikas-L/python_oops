def is_perfect(n):
    total = 0

    for i in range(1, n // 2 + 1):
        if n % i == 0:
            total += i

    return n == total


n = int(input("Enter the number: "))
res = is_perfect(n)

if res:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")