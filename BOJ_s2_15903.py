n, m = map(int, input().split())

card = list(map(int, input().split()))

for _ in range(m):
    card.sort()
    new_card = card[0] + card[1]
    card[0] = new_card
    card[1] = new_card

print(sum(card))
