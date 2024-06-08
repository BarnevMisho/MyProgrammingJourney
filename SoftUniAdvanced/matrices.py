rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
max_sum = 0
max_matrix = []

for i in range(rows - 2):
    for j in range(cols - 2):
        submatrix = [row[j:j+3] for row in matrix[i:i+3]]
        current_sum = sum([element for row in submatrix for element in row])
        if current_sum > max_sum:
            max_matrix = submatrix
            max_sum = current_sum

print(f"Sum = {max_sum}")
for row in max_matrix:
    print(*row)
