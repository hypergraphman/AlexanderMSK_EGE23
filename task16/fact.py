# n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1
x = 999  # 720
f = 1
for i in range(1, x + 1):
    f = f * i
print(f)


def fact(n):
    if n < 2:
        return 1
    if n >= 2:
        return n * fact(n - 1)
print(fact(x))