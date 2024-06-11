rows = int(input())
matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(rows)]

for row in matrix:
    if "B" in row:
        index_bunny = (matrix.index(row), row.index("B"))

# path up
path_up = []
egs_up = 0
if index_bunny[0] > 0:
    for i in range(index_bunny[0] - 1, -1, -1):
        if matrix[i][index_bunny[1]] == "X":
            break
        else:
            egs_up += matrix[i][index_bunny[1]]
            path_up.append([i, index_bunny[1]])

# path down
path_down = []
egs_down = 0
if index_bunny[0] < len(matrix) - 1:
    for i in range(index_bunny[0] + 1, len(matrix)):
        if matrix[i][index_bunny[1]] == "X":
            break
        else:
            egs_down += matrix[i][index_bunny[1]]
            path_down.append([i, index_bunny[1]])

# path left
path_left = []
egs_left = 0
if index_bunny[1] > 0:
    for j in range(index_bunny[1] - 1, -1, -1):
        if matrix[index_bunny[0]][j] == "X":
            break
        else:
            egs_left += matrix[index_bunny[0]][j]
            path_left.append([index_bunny[0], j])

# path right
path_right = []
egs_right = 0
if index_bunny[1] < len(matrix) - 1:
    for j in range(index_bunny[1] + 1, len(matrix)):
        if matrix[index_bunny[0]][j] == "X":
            break
        else:
            egs_right += matrix[index_bunny[0]][j]
            path_right.append([index_bunny[0], j])

result = {egs_up: (path_up, "up"), egs_down: (path_down, "down"),
          egs_left: (path_left, "left"), egs_right: (path_right, "right")}

egs = max(result)
path, direction = result[max(result)]

print(direction)
for r in path:
    print(r)
print(egs)

