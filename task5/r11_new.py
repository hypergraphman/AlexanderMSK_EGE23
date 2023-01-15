def f(n):
    return 2**(len(f'{n:b}') - 1)


print(f(11))
a = set()
for i in range(500, 5000):
    a.add(f(i))
print(len(a))
print(a)