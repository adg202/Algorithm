#1이 될 때 까지

N, K = map(int, input().split())
count = 0

while N != 1:
    if N%K != 0:
        N -= 1
    else:
        N //= K
    count += 1

print(count)