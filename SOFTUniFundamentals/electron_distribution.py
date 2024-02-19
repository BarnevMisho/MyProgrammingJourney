electrons = int(input())
current_shell = 1
filled_shells = []
while electrons >= 2 * current_shell ** 2:
    filled_shells.append(2 * current_shell ** 2)
    electrons -= 2 * current_shell ** 2
    current_shell += 1

if electrons != 0:
    filled_shells.append(electrons)

print(filled_shells)