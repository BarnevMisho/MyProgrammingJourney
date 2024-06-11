rows = int(input())
matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(rows)]
tea = 0

for row in matrix:
    if "A" in row:
        a_row, a_col = [matrix.index(row), row.index("A")]

directions = {
    "right": lambda a, b: (a, b + 1),
    "left": lambda a, b: (a, b - 1),
    "down": lambda a, b: (a + 1, b),
    "up": lambda a, b: (a - 1, b)
}

while True:
    matrix[a_row][a_col] = "*"
    if tea >= 10:
        break
    command = input()
    a_row, a_col = directions[command](a_row, a_col)
    if not (0 <= a_row < len(matrix)) or not (0 <= a_col < len(matrix)):
        break
    elif matrix[a_row][a_col] == "R":
        matrix[a_row][a_col] = "*"
        break
    elif str(matrix[a_row][a_col]).isdigit():
        tea += matrix[a_row][a_col]

if tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(*row)
