#거스름돈

N = int(input())
total = 0
token = [500, 100, 50, 10]

for t in token:
    tmp = N // t
    total += tmp
    N %= t

print(total)

