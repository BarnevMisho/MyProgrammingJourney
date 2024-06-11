matrix = [input().split() for _ in range(5)]
n = int(input())
targets_positions = []
targets = 0
targets_hit = 0

for row in matrix:
    if "A" in row:
        a_row, a_col = [matrix.index(row), row.index("A")]
    for element in row:
        if element == 'x':
            targets += 1

moving = {
    "right": lambda a, b, s: (a, b + s),
    "left": lambda a, b, s: (a, b - s),
    "down": lambda a, b, s: (a + s, b),
    "up": lambda a, b, s: (a - s, b)
}
shooting = {"right": (0, 1), "left": (0, -1), "down": (1, 0), "up": (-1, 0)}

for _ in range(n):
    command = input().split()
    if command[0] == "move":
        direction, steps = command[1], int(command[2])
        new_row, new_col = moving[direction](a_row, a_col, steps)
        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix) and matrix[new_row][new_col] == ".":
            matrix[a_row][a_col] = "."
            a_row, a_col = new_row, new_col
            matrix[a_row][a_col] = "A"
    elif command[0] == "shoot":
        direction = command[1]
        shoot_row, shoot_col = a_row + shooting[direction][0], a_col + shooting[direction][1]
        while True:
            if not(0 <= shoot_row < len(matrix)) or not(0 <= shoot_col < len(matrix)):
                break
            elif matrix[shoot_row][shoot_col] == "x":
                targets_positions.append([shoot_row, shoot_col])
                targets_hit += 1
                matrix[shoot_row][shoot_col] = "."
                break
            shoot_row, shoot_col = shoot_row + shooting[direction][0], shoot_col + shooting[direction][1]
        if targets == targets_hit:
            break

if targets == targets_hit:
    print(f"Training completed! All {targets} targets hit.")
else:
    print(f"Training not completed! {targets - targets_hit} targets left.")
for pos in targets_positions:
    print(pos)


