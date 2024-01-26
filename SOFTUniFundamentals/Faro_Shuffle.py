cards = input().split()
shuffles = int(input())

for _ in range(shuffles):
    index_second_half = 1
    index_insert = 1
    while index_second_half < len(cards) / 2:
        cards.insert(index_insert, cards[int(len(cards)/2) + index_second_half - 1])
        cards.pop(int(len(cards)/2) + index_second_half)
        index_second_half += 1
        index_insert += 2

print(cards)