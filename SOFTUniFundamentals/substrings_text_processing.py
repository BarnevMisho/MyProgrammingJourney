splitting_word = input()
word = input()
"""
splited_word = word.split(splitting_word)
for _ in range(len(splited_word)):
    splited_word = "".join(splited_word)
    splited_word = splited_word.split(splitting_word)

print("".join(splited_word))
"""
while splitting_word in word:
    word = word.replace(splitting_word, "")

print(word)

