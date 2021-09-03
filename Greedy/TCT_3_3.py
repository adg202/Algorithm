#숫자 카드 게임

N, M = map(int, input().split())

max_of_min = 0

for i in range(N):
    data = list(map(int, input().split()))
    max_of_min = max(max_of_min, min(data))

print(max_of_min)