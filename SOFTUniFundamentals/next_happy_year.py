year = int(input())

while True:
    year += 1
    year_in_string = str(year)
    if len(year_in_string) == len(set(year_in_string)):
        print(year)
        break

