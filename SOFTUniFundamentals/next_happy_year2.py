year = int(input())


while True:
    year += 1
    happy_year = True
    year_as_string = str(year)
    different_digits = ""
    for current_digit in year_as_string:
        if current_digit not in different_digits:
            different_digits += current_digit
        else:
            happy_year = False
            break
    if happy_year:
        print(year)
        break



