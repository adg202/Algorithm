#게임 개발

w, h = map(int, input().split())
row, col, view = map(int, input().split())

world = []
for _ in range(h):
    world.append(list(map(int, input().split())))

user = world[row][col]
world[row][col] = 1

#1. 왼쪽으로 회전
if view != 0:
    view -= 1
else:
    view = 3

#2. 전진
move_row = [-1, 0, 0, 1]
move_col = [0, 1, -1, 0]

if world[row + move_row[view]][col + move_col[view]] == 0:
    user = world[row + move_row[view]][col + move_col[view]]
    world[row + move_row[view]][col + move_col[view]] = 1
