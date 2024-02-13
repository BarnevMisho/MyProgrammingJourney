def loading_bar(num):
    result = ""
    pr = "%"
    dot = "."
    if num == 100:
        result = f"{num}% Complete!\n[{pr * int(num/10)}]"
    else:
        result = f"{num}% [{pr * int(num / 10) + dot * int(10 - num / 10) }]\nStill loading..."

    print(result)

number = int(input())
loading_bar(number)

