employees_happiness = input().split()
factor = int(input())
actuall_happiness = list(map(lambda x: int(x) * factor, employees_happiness))
avarage = sum(actuall_happiness) / len(actuall_happiness)
#filterd_happiness = [score for score in actuall_happiness if score >= avarage]
filterd_happiness = list(filter(lambda x: x >= avarage, actuall_happiness))
happy_count = len(filterd_happiness)
total_count = len(actuall_happiness)
if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")