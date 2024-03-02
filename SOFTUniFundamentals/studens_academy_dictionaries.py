number = int(input())
students_dict = {}
new_dict = {}
for _ in range(number):
    student = input()
    grade = float(input())
    if student not in students_dict.keys():
        students_dict[student] = []
    students_dict[student].append(grade)

for key, value in students_dict.items():
    average = sum(value) / len(value)
    if average >= 4.50:
        new_dict[key] = average

for name, averageGrade in new_dict.items():
    print(f"{name} -> {averageGrade :.2f}")