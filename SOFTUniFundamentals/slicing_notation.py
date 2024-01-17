first_string = input()
second_string = input()
new_string = ""
previous_string = first_string

for i in range(len(second_string)):
    new_string = second_string[:i+1] + first_string[i+1:]
    if new_string != previous_string:
        print(new_string)

    previous_string = new_string