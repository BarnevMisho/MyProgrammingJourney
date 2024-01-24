n = int(input())
full_list = []
new_list = []

for _ in range(n):
    number = int(input())
    full_list.append(number)


command = input()
if command == "even":
    for i in range(len(full_list)):
        if full_list[i] % 2 == 0:
            new_list.append(full_list[i])
elif command == "odd":
    for i in range(len(full_list)):
        if full_list[i] % 2 == 1:
            new_list.append(full_list[i])
elif command == "positive":
    for i in range(len(full_list)):
        if full_list[i] >= 0:
            new_list.append(full_list[i])
elif command == "negative":
    for i in range(len(full_list)):
        if full_list[i] < 0:
            new_list.append(full_list[i])

print(new_list)


