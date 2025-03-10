from module import search

class Student:
    def __init__(self, name, surname, group, grades=None):
        if grades is None:
            grades = []
        self.name = name
        self.surname = surname
        self.group = group
        self.grades = grades
        self.isInUniversity = False

    def __str__(self):
        val = f"\n{'-' * 5}{self.name} {self.surname}{'-' * 5}\nГруппа: {self.group}\nОценки: {self.grades}\n"
        if len(self.grades) > 0:
            val += f"Средний балл: {self.get_average_grade():.2f}\n"
        val += "-" * (len(self.name) + len(self.surname) + 10)
        return val

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades) if len(self.grades) > 0 else None



class University:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if not student.isInUniversity:
            student.isInUniversity = True
            self.students.append(student)

    def remove_student(self, name, surname):
        res1 = search(name, self.students)[0]
        students = search(surname, res1, 'surname')
        if len(students[0]) == 0:
            print("Таких учеников не найдено")
            return
        for student in sorted(students[1], reverse=True):
            del self.students[student]

    def student_average_grade(self, name, surname):
        res1 = search(name, self.students)[0]
        students = search(surname, res1, 'surname')
        if len(students[0]) == 0:
            print("Таких учеников не найдено")
            return
        for student in sorted(students[0], reverse=True):
            ag = student.get_average_grade()
            if ag is not None:
                print(ag)
            else: print("Нет оценок")

    def get_top_students(self, n):
        stds = ""
        for i in sorted(self.students, key=lambda s: s.get_average_grade(), reverse=True)[:n]:
            stds += f"{i.name} {i.surname}\n"
            #здесь вылетает, если у ученика нету оценок
        return stds


bob = Student("Bob", "Bobik", "A", [2, 4, 5, 3, 5])
carl = Student("Carl", "Carlik", "B", )
un = University()
un.add_student(bob)
un.add_student(carl)
print(un.get_top_students(2))