def password_validator(password):
    output = ""
    is_valid = True

    if not 6 <= len(password) <= 10:
        output += "Password must be between 6 and 10 characters\n"
        is_valid = False

    for char in password.lower():
        if not(ord(char) in range(97,123) or ord(char) in range(48,58)):
            output += "Password must consist only of letters and digits\n"
            is_valid = False
            break

    count_of_digits = 0
    for char in password.lower():
        if ord(char) in range(48,58):
            count_of_digits += 1

    if count_of_digits < 2:
        output += "Password must have at least 2 digits\n"
        is_valid = False

    if is_valid:
        output = "Password is valid"

    return output

string = input()
print(password_validator(string))