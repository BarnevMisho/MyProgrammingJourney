message = input().split()
decipherd_message = []
for word in message:
    length = len(word)
    if length >= 5:
        if ord(word[2]) in range(48,58):
            new_word = chr(int(word[0:3])) + word[-1] + word[4:-1] + word[3]
        else:
            new_word = chr(int(word[0:2])) + word[-1] + word[3:-1] + word[2]
    elif length == 4:
        if ord(word[2]) in range(48,58):
            new_word = chr(int(word[0:3])) + word[-1]
        else:
            new_word = chr(int(word[0:2])) + word[-1] + word[2]
    else:
        new_word = chr(int(word[0:2])) + word[-1]

    decipherd_message.append(new_word)

print(" ".join(decipherd_message))


