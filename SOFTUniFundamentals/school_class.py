class Class:
    __students_count = 22
    def __init__(self, name: str):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)


    def get_average_grade(self):
        return f"{sum(self.grades)/len(self.students) :.2f}"

    def __repr__(self):
        students = ",".join(self.students)
        average_grade = Class.get_average_grade(self)
        return f"The students in {self.name}: {students}. Average grade: {average_grade}."

