class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}                    


    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def give_marks(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
 
                
    def __str__(self):
        all_grades = []
        for course in self.grades:
            all_grades.extend(self.grades[course])
        if len(all_grades) > 0:
            average_grade = round(sum(all_grades) / len(all_grades), 1)
        else:
            average_grade = 0
        return f'Студент:\nИмя:{self.name}\nФамилия:{self.surname}\nКурсы в процессе изучения:{self.courses_in_progress}\nЗавершенные курсы:{self.finished_courses}\nСредняя оценка за ДЗ:{average_grade}'

        
    def __gt__(self,other):
        if isinstance(other, Student):
            self_grades = []
            other_grades = []

            for course in self.grades:
                self_grades.extend(self.grades[course])

            for course in other.grades:
                other_grades.extend(other.grades[course])

            if len(self_grades) > 0:
                self_average_grade = sum(self_grades) / len(self_grades)
            else:
                self_average_grade = 0

            if len(other_grades) > 0:
                other_average_grade = sum(other_grades) / len(other_grades)
            else:
                other_average_grade = 0

            return self_average_grade > other_average_grade
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f'Проверяющий:\nИмя: {self.name}\nФамилия: {self.surname}'
        


class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        all_grades = []
        for course in self.grades:
            all_grades.extend(self.grades[course])
        if len(all_grades) > 0:
            average_grade = round(sum(all_grades) / len(all_grades), 1)
        else:
            average_grade = 0
        return f'Лектор:\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекцию:{average_grade}'

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            self_grades = []
            other_grades = []
            for course in self.grades:
                self_grades.extend(self.grades[course])
            for course in other.grades:
                other_grades.extend(other.grades[course])
            if len(self_grades) > 0:
                self_average_grades = sum(self_grades) / len(self_grades)
            else:
                self_average_grades = 0
            
            if len(other_grades) > 0:
                other_average_grades = sum(other_grades) / len(other_grades)
            else:
                other_average_grades = 0
            return self_average_grades > other_average_grades
    
def main():
    best_student = Student('Obi-wan', 'Kenobi', 'male')
    second_best_student = Student('Luc', 'Skywalker', 'male')
    cool_reviewer = Reviewer('Darth', 'Wader')
    second_cool_reviewer = Reviewer('Darth', 'Sidious')
    cool_lecturer = Lecturer('John', 'Snow')
    second_cool_lecturer = Lecturer('Arya', 'Stark')
            
    best_student.finished_courses += ['Git']
    best_student.courses_in_progress += ['Python']
    best_student.courses_in_progress += ['OOP']
    best_student.give_marks(cool_lecturer, 'Python', 10)
    best_student.give_marks(cool_lecturer, 'Python', 7)
    best_student.give_marks(cool_lecturer, 'Git', 10)

    second_best_student.finished_courses += ['Python']
    second_best_student.courses_in_progress += ['Git']
    second_best_student.courses_in_progress += ['OOP']
    second_best_student.give_marks(cool_lecturer, 'Git',8)
    second_best_student.give_marks(cool_lecturer, 'Git', 10)
    second_best_student.give_marks(second_cool_lecturer, 'OOP', 10)
    second_best_student.give_marks(second_cool_lecturer, 'OOP', 8)
    
    cool_reviewer.courses_attached += ['Python']
    cool_reviewer.rate_hw(best_student, 'Python', 10)
    cool_reviewer.rate_hw(best_student, 'Python', 8)
    cool_reviewer.rate_hw(best_student, 'Python', 10)
    
    second_cool_reviewer.courses_attached += ['Git']
    second_cool_reviewer.courses_attached += ['OOP']
    second_cool_reviewer.rate_hw(second_best_student, 'Git', 8)
    second_cool_reviewer.rate_hw(second_best_student, 'Git', 9)
    second_cool_reviewer.rate_hw(second_best_student, 'Git',10)
    
    cool_lecturer.courses_attached += ['Python']
    cool_lecturer.courses_attached += ['Git']
    second_cool_lecturer.courses_attached += ['Git']
    second_cool_lecturer.courses_attached += ['OOP']
    
    print()
    
    if cool_lecturer > second_cool_lecturer:
        print(f'У лектора {cool_lecturer.name} {cool_lecturer.surname} средняя оценка выше!')
    elif cool_lecturer == second_cool_lecturer:
        print(f'Средние оценки у лекторов {cool_lecturer.name} {cool_lecturer.surname} и {second_cool_lecturer.name} {second_cool_lecturer.surname} равны')
    else:
        print(f'Средняя оценка у лектора {second_cool_lecturer.name} {second_cool_lecturer.surname} выше чкм у лектора {cool_lecturer.name}{cool_lecturer.surname}')
        
    if best_student > second_best_student:
        print(f'У студента {best_student.name} {best_student.surname} средняя оценка выше чем у студента {second_best_student.name} {second_best_student.surname}')
    elif best_student == second_best_student:
        print(f'Средние оценки у студентов {best_student.name} {best_student.surname} и {second_best_student.name} {second_best_student.surname} равны')
    else:
        print(f'Средняя оценка у студента {second_best_student.name} {second_best_student.surname} выше чем у студента {best_student.name} {best_student.surname}')
    
    
    print()
    students = [best_student, second_best_student]
    lecturers = [cool_lecturer, second_cool_lecturer]
    courses = ['Python', 'Git', 'OOP']
    
    def student_avrg_course_grade(students, course):
        all_grades = []
        for student in students:
            if course in student.grades:
                all_grades.extend(student.grades[course])
        if len(all_grades) > 0:
            average_grade = round(sum(all_grades) / len(all_grades))
        else:
            return f'По курсу {course} оценок еще не выставлено'
        return f'Средняя оценка по курсу {course} среди студентов:{average_grade}'
    
    def lecturer_avrg_course_grade(lecturers, course):
        all_grades = []
        for lecturer in lecturers:
            if course in lecturer.grades:
                all_grades.extend(lecturer.grades[course])
        if len(all_grades) > 0:
            average_grade = round(sum(all_grades) / len(all_grades))
        else:
            return f'По курсу {course} лекторам еще не ставили оценок'
        return f'Средняя оценка лекторов по курсу {course}: {average_grade}'
    
    for course in courses:
        print(student_avrg_course_grade(students, course))
        print(lecturer_avrg_course_grade(lecturers, course))
    print()   
    print(best_student)
    print()
    print(cool_lecturer)
    print()
    print(cool_reviewer)
    
    


        
main()



