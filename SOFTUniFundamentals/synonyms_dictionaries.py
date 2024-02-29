count_of_word = int(input())
synonyms = {}
words_input = [input() for _ in range(count_of_word * 2)]

for index in range(0, len(words_input), 2):
    if words_input[index] not in synonyms.keys():
        synonyms[words_input[index]] = []
        synonyms[words_input[index]].append(words_input[index + 1])
    else:
        synonyms[words_input[index]].append(words_input[index + 1])

for key, value in synonyms.items():
    strings = ", ".join(value)
    print(f"{key} - {strings}")

