#상하좌우

x, y = 1, 1

size = int(input())
cmd = input().split()

for c in cmd:
    if c == "R" and x < size:
        x += 1
    elif c == "L" and x > 1:
        x -= 1
    elif c == "D" and y < size:
        y += 1
    elif c == "U" and y > 1:
        y -= 1

print(y, x)