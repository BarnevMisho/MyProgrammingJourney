def factoriel(num):
    result = 0
    if num == 0:
        return 1
    else:
        result = factoriel(num - 1) * num
        return result

def output(num1,num2):
    result1 = factoriel(num1)
    result2 = factoriel(num2)
    return f"{(result1/result2) :.2f}"

x = int(input())
y = int(input())
print(output(x,y))
