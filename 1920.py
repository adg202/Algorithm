N = int(input())
nData = list(map(int, input().split()))
nData.sort()
M = int(input())
mData = list(map(int, input().split()))


for m in mData:
    left = 0
    right = N-1
    mid = (left + right) // 2


    while left < right:
        print(left, mid, right)
        print(m)

        if m > right or m < left:
            print(0)
            break

        if nData[mid] > m:
            right = mid - 1
            mid = right - 1
        elif nData[mid] < m:
            left = mid + 1
            mid = left + 1
        else:
            print(1)
            break