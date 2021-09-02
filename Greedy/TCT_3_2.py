#큰 수의 법칙

N, M, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

answer = 0

answer += data[-1] * (M // K) * K
data.pop()
answer += data[-1] * (M % K)

print(answer)