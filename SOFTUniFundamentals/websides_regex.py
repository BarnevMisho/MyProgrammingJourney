import re

text = input()
regex = r'(www.[a-zA-Z0-9]+(\-[a-zA-Z0-9]+)*(\.[a-zA-Z]+)+)'
while text:
    valid_webs = re.findall(regex, text)
    if valid_webs:
        print(valid_webs[0][0])
    text = input()

