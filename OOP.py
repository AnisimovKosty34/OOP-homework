def courses_average(person_list, course):
    for person in person_list:
        for cours_name, average in person.grades.items():
            if course == cours_name:
                sum_average = sum(average) / len(average)
                return (f"{person.name} {person.surname}\n"
                       f"{cours_name}\n"
                       f"Cредняя оценка: {round(sum_average, 0)}\n")


def comparison_grades(pers1, pers2):
    if pers1.grades_average() > pers2.grades_average():
        return(f'Средняя оценка {pers1.name} {pers1.surname} больше, чем средняя оценка {pers2.name} {pers2.surname}')
    elif pers1.grades_average() < pers2.grades_average():
        return(f'Средняя оценка {pers1.name} {pers1.surname} меньше, чем средняя оценка {pers2.name} {pers2.surname}')
    else:
        return(f'Средняя оценка {pers1.name} {pers1.surname}  равна средней оценке {pers2.name} {pers2.surname}')
        
class Student:
    student_list = []
    def __init__(self, name, surname, faculty):
        self.name = name
        self.surname = surname
        self.faculty = faculty
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)
        
    def __gt__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Сравниваются объекты разных классов')
        return self.grades_average() > other.grades_average()
    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Сравниваются объекты разных классов')
        return self.grades_average() < other.grades_average()
    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Сравниваются объекты разных классов')
        return self.grades_average() == other.grades_average()

    def rate_hw_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def grades_average(self):
        gr_count = 0
        gr_sum = 0
        for i in self.grades:
            gr_count += len(self.grades[i])
            gr_sum += sum(self.grades[i])
        return gr_sum / gr_count

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Факультет: {self.faculty}\n"
                f"Средняя оценка за домашние задания: {round(self.grades_average(), 0)}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}\n")

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError('Сравниваются объекты разных классов')
        return self.grades_average() > other.grades_average()
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError('Сравниваются объекты разных классов')
        return self.grades_average() < other.grades_average()
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError('Сравниваются объекты разных классов')
        return self.grades_average() == other.grades_average()

class Lecturer(Mentor):
    lecturer_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.lecturer_list.append(self)

    def grades_average(self):
        gr_count = 0
        gr_sum = 0
        for i in self.grades:
            gr_count += len(self.grades[i])
            gr_sum += sum(self.grades[i])
        return gr_sum / gr_count

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {round(self.grades_average(), 0)}\n")

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")

student_1 = Student('Гарри', 'Поттер', 'Гриффиндор')
student_1.courses_in_progress += ['Защита от Тёмных искусств']
student_1.courses_in_progress += ['Зельеварение']
student_1.courses_in_progress += ['Трансфигурация']
student_1.finished_courses += ['Полёты на мётлах']

student_2 = Student('Драко', 'Малфой', 'Слизерин')
student_2.courses_in_progress += ['Защита от Тёмных искусств']
student_2.courses_in_progress += ['Зельеварение']
student_2.courses_in_progress += ['Трансфигурация']
student_2.finished_courses += ['Полёты на мётлах']

reviewer_1 = Reviewer('Рубеус', 'Хагрид')
reviewer_1.courses_attached += ['Защита от Тёмных искусств']
reviewer_1.courses_attached += ['Зельеварение']
reviewer_1.courses_attached += ['Трансфигурация']

reviewer_2 = Reviewer('Минерва', 'Макгонагалл')
reviewer_2.courses_attached += ['Защита от Тёмных искусств']
reviewer_2.courses_attached += ['Зельеварение']
reviewer_2.courses_attached += ['Трансфигурация']

lecturer_1 = Lecturer('Северус', 'Снейп')
lecturer_1.courses_attached += ['Защита от Тёмных искусств']
lecturer_1.courses_attached += ['Зельеварение']
lecturer_1.courses_attached += ['Трансфигурация']

lecturer_2 = Lecturer('Альбус', 'Дамблдор')
lecturer_2.courses_attached += ['Защита от Тёмных искусств']
lecturer_2.courses_attached += ['Зельеварение']
lecturer_2.courses_attached += ['Трансфигурация']

reviewer_1.rate_hw_student(student_1, 'Защита от Тёмных искусств', 8)
reviewer_1.rate_hw_student(student_1, 'Защита от Тёмных искусств', 9)
reviewer_1.rate_hw_student(student_1, 'Зельеварение', 8)
reviewer_1.rate_hw_student(student_1, 'Трансфигурация', 10)

reviewer_1.rate_hw_student(student_2, 'Защита от Тёмных искусств', 5)
reviewer_1.rate_hw_student(student_2, 'Защита от Тёмных искусств', 6)
reviewer_1.rate_hw_student(student_2, 'Зельеварение', 2)
reviewer_1.rate_hw_student(student_2, 'Трансфигурация', 4)

student_1.rate_hw_lecturer(lecturer_1, 'Защита от Тёмных искусств', 7)
student_1.rate_hw_lecturer(lecturer_1, 'Защита от Тёмных искусств', 7)
student_1.rate_hw_lecturer(lecturer_1, 'Зельеварение', 8)

student_2.rate_hw_lecturer(lecturer_2, 'Защита от Тёмных искусств', 10)
student_2.rate_hw_lecturer(lecturer_2, 'Защита от Тёмных искусств', 10)
student_2.rate_hw_lecturer(lecturer_2, 'Зельеварение', 8)

print(reviewer_1)
print(reviewer_2)
print(lecturer_1)
print(lecturer_2)
print(student_1)
print(student_2)

print(courses_average(Student.student_list, 'Защита от Тёмных искусств'))
print(courses_average(Lecturer.lecturer_list, 'Защита от Тёмных искусств'))

print(comparison_grades(lecturer_1, lecturer_2))
print(comparison_grades(student_1, student_2))