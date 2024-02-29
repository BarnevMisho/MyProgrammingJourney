student_info = input().split(":")
students_data = {}
students_data["name"] = []
students_data["ID"] = []
students_data["course"] = []

while len(student_info) == 3:
    name = student_info[0]
    id = student_info[1]
    course = student_info[2]
    students_data["name"].append(name)
    students_data["ID"].append(id)
    students_data["course"].append(course)
    student_info = input().split(":")

index = -1
for current_course in students_data["course"]:
    if len(student_info[0].split("_")) == 2:
        if " ".join(student_info[0].split("_")) == current_course:
            index = students_data["course"].index(current_course, index + 1)
            name_output = students_data["name"][index]
            id_output = students_data["ID"][index]
            print(f"{name_output} - {id_output}")
    elif len(student_info[0].split("_")) == 1:
        if student_info[0] == current_course:
            index = students_data["course"].index(current_course, index + 1)
            name_output = students_data["name"][index]
            id_output = students_data["ID"][index]
            print(f"{name_output} - {id_output}")






"""
Peter:123:programming basics
John:5622:fundamentals
Lilly:633:fundamentals
fundamentals
"""