def merge(words, start_index, end_index):
    new_string = ""
    if start_index < len(words):
        if start_index < 0:
            start_index = 0
        if end_index >= len(words):
            end_index = len(words) - 1
        for i in range(start_index, end_index + 1):
            new_string += words[i]
        words = words[:start_index] + [new_string] + words[end_index + 1:]
    return words


def divide(words, index, partitions):
    divided_string = []
    length = len(words[index]) // partitions
    for part in range(1, partitions):
        divided_string.append(words[index][(part - 1) * length: part * length])
    divided_string.append(words[index][(partitions - 1) * length:])
    words = words[:index] + divided_string + words[index + 1:]
    return words


strings = input().split()
command = input()

while command != "3:1":
    command_list = command.split()
    if command_list[0] == "merge":
        startIndex = int(command_list[1])
        endIndex = int(command_list[2])
        strings = merge(strings, startIndex, endIndex)

    elif command_list[0] == "divide":
        ind = int(command_list[1])
        parts = int(command_list[2])
        strings = divide(strings, ind, parts)

    command = input()

print(" ".join(strings))
