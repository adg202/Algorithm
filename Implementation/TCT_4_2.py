#시각

N = int(input())
count = 0

for hh in range(N+1):
    for mm in range(60):
        for ss in range(60):
            if "3" in str(hh) + str(mm) + str(ss):
                count += 1

print(count)