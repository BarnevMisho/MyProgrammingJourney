def palindrome(numbers):
    result = ""
    numbers_list = numbers.split(", ")
    for current_integer in numbers_list:
        if current_integer[::-1] == current_integer:
             result += "True\n"
        else:
             result += "False\n"

    return result

number = input()
print(palindrome(number))
