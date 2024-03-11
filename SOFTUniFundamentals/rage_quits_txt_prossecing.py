text = input()
rage_text = ""
new_text = ""
for index in range(len(text)):
    if text[index:index+2].isdigit():
        rage_text += new_text * int(text[index:index+2])
        new_text = ""
    elif text[index].isdigit():
        rage_text += new_text * int(text[index])
        new_text = ""
    else:
        new_text += text[index].upper()

unique_symbols = len(set(rage_text))
print(f"Unique symbols used: {unique_symbols}")
print(rage_text)




