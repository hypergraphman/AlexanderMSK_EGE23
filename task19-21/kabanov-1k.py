win = 29


def f(s, c, m):
    if s >= win:
        return c % 2 == m % 2
    # if s > 72: return c % 2 != m % 2 - с верхним ограничением
    if c == m:
        return False
    moves = [f(s + 1, c + 1, m), f(s * 2, c + 1, m)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)  # any, если первый ход пети был неудачный


for s in range(1, win):
    for m in range(1, 5):
        if f(s, 0, m):
            print(s, m)
            break

