class Student:
    def __init__(self, n, pattern):
        self.n = n
        self.pattern = pattern
        self.size = len(pattern)
        self.score = 0

    def grade_score(self, answers):
        for i, a in enumerate(answers):
            if a == self.pattern[i % self.size]:
                self.score += 1

    @classmethod
    def top(cls, students):
        top_score = -1

        for student in students:
            if top_score < student.score:
                top_score = student.score
                top_students = [student.n]
            elif top_score == student.score:
                top_students.append(student.n)

        return top_students


def solution(answers):
    students = [
        Student(1, [1, 2, 3, 4, 5]),
        Student(2, [2, 1, 2, 3, 2, 4, 2, 5]),
        Student(3, [3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    ]

    for student in students:
        student.grade_score(answers)

    return Student.top(students)
