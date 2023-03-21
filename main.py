all_students = []
all_teachers = []
all_curator = []
all_lessons = []

class Human:
    def __init__(self, name: str, surname: str, email: str, age: int, tel: str):
        self.name = name
        self.surname = surname
        self.email = email
        self.age = age
        self.tel = tel


class Student(Human):
    def __init__(self, name: str, surname: str, email: str, age: int, tel: str):
        super().__init__(name, surname, email, age, tel)
        self.knowledge = []
        all_students.append(self)

    def __str__(self):
        return self

    @staticmethod
    def get_all_students():
        return all_students

    @staticmethod
    def check_student(student):
        if student in all_students:
            return True
        else:
            return False

    # def get_students(self):
    #     list_students = []
    #     for i in all_students:
    #         list_students.append(i)
    #     return list_students

    def get_knowledge(self, lesson):
        self.knowledge.append(lesson)
        return True

class Employee(Human):
    def __init__(self, lich_dan: str, dolznost: str, stag: int, stavka: int, vid_dogovora: str):
        # super().__init__(name, surname, email, age, tel)
        self.lich_dan = lich_dan
        self.dolznost = dolznost
        self.stag = stag
        self.stavka = stavka
        self.vid_dogovora = vid_dogovora


class Teacher(Employee):
    def __init__(self.name: str, surname: str, email: str, age: int, tel: str):
        super().__init__(name, surname, email, age, tel)
        all_teachers.append(self)

    @staticmethod
    def get_all_teachers():
        return all_teachers

    @staticmethod
    def check_teacher(teacher: "Teacher"):
        if teacher in all_teachers:
            return True
        else:
            print(f'Самозванец  {teacher.name}')
            return False

    def hold_lesson(self, lesson: "Lesson", students: list) -> bool:
        if self.check_teacher(self) and Lesson.check_teacher_by_lesson(lesson, self):
            student_names = []
            for student in students:
                student.get_knowledge(lesson)
                student_names.append(student.name)
            print(f'Преподаватель {self.surname} {self.name} провёл занятие \'{lesson.lesson_name}\'\n '
                  f'Для студентов: \n {student_names}')

class Curator(Employee):
    def __init__(self):
        super().__init__()



class Lesson:
    def __init__(self, lesson_name: str, theme: str, teachers: list):
        self.lesson_name = lesson_name
        self.theme = theme
        self.teachers = teachers
        all_lessons.append(self)

    def check_teacher_by_lesson(self, teacher: "Teacher"):
        if teacher in self.teachers:
            return True
        else:
            print(f'Преподавтель {teacher.surname} {teacher.name} не может преподать урок \'{self.lesson_name}\', '
                  f'так как не знает его')
            return False

    def get_teachers_by_lesson(self):
        return self.teachers


Teacher_Vladislav = Teacher('Владислав', 'Духовских', 'prizrak@mail.ru', 30, '+79220000000')
Teacher_Alexey = Teacher('Алексей', 'Гуров', 'gurov@mail.ru', 28, '+79220101010')

Stud_Vitya = Student('Витя', 'Витевских', 'vitya@mail.ru', 18, '+79220202020')
Stud_Dima = Student('Дима', 'Дмитриевских', 'dima@mail.ru', 77, '+79221212120')
Stud_Anna = Student('Анна', 'Анина', 'annaa@mail.ru', 18, '+79220202021')
Stud_Sasha = Student('Саша', 'Александрович', 'sasha@mail.ru', 25, '+79230202020')

Programming = Lesson('Программирование', 'Питон', [Teacher_Vladislav])
Music = Lesson('Музыка', 'Рок', [Teacher_Alexey])

Teacher_Vladislav.hold_lesson(Programming, [Stud_Sasha, Stud_Anna, Stud_Dima, Stud_Vitya])
Teacher_Alexey.hold_lesson(Programming, [Stud_Sasha, Stud_Anna])