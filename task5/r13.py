def f(n):
    s1 = f'{n:b}'
    s2a = s1 + str(sum(map(int, s1)) % 2)
    s2b = s2a + str(sum(map(int, s2a)) % 2)
    return int(s2b, 2)


print(f(28))

i = 1
while f(i) <= 77:
    i += 1
print(i)