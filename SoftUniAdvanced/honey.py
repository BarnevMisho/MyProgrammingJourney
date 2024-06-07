from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
operations = deque(input().split())
honey_made = 0

mapper = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: abs(a - b),
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}

while bees and nectar:
    if bees[0] > nectar[-1]:
        nectar.pop()
    else:
        bee = bees.popleft()
        collected_nectar = nectar.pop()
        if operations[0] == "/" and collected_nectar == 0:
            operations.popleft()
            continue
        honey_made += mapper[operations.popleft()](bee, collected_nectar)

print(f"Total honey made: {honey_made}")
if bees:
    output_bees = ", ".join([str(x) for x in bees])
    print(f"Bees left: {output_bees}")
if nectar:
    output_nectar = ", ".join([str(x) for x in nectar])
    print(f"Nectar left: {output_nectar}")