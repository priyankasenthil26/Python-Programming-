def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

num = 6
print(f"{num} is a perfect number" if is_perfect(num) else f"{num} is not a perfect number\n")
