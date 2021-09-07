#왕실의 나이트

Knight = input()
answer = 0

col = ord(Knight[0]) #a
row = int(Knight[1]) #1

col_min = ord('a')
col_max = ord('h')

col_move = [-2, -2, 2, 2, 1, -1, 1, -1]
row_move = [1, -1, 1, -1, -2, -2, 2, 2]

for i in range(8):
    col_check = col + col_move[i]
    row_check = row + row_move[i]

    if (col_check >= col_min and col_check <= col_max) and (row_check >= 1 and row_check <= 8):
        answer += 1

print(answer)