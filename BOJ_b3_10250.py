#ACM 호텔

T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    floor = N%H
    loc = N//H+1

    #나누어 떨어져버리는 경우
    if floor == 0:
        floor = H
        loc -= 1

    print(floor * 100 + loc)