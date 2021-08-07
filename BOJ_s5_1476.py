#날짜 계산

E, S, M = map(int, input().split())

n = 1
while True:
    a = n % 15
    if a == 0:
        a = 15

    b = n % 28
    if b == 0:
        b = 28

    c = n % 19
    if c == 0:
        c = 19

    if a == E and b == S and c == M:
        print(n)
        break
    else:
        n += 1
