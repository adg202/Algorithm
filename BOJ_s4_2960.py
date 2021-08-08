N, K = map(int, input().split())

prime = []
count = 0

for i in range(N+1):
    if i == 0 or i == 1:
        prime.append(0)
    else:
        prime.append(1)

#print(prime)
for j in range(2, N+1):
    for k in range(j, N+1, j):
        #print(k)
        if prime[k] != 0:
            prime[k] = 0
            #print(prime)
            count += 1
            if count == K:
                print(k)
                break
    break


