from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(courses:list,):
    return reduce(lambda initial, item: item.credits + initial, courses,0)

def sum_of_passed_credits(courses:list):
    passed_courses = list(filter(lambda item: item.grade >= 1, courses))
    return reduce(lambda initial, item: item.credits + initial, passed_courses,0)

def average(courses:list):
    passed_courses = list(filter(lambda item: item.grade >= 1, courses))
    sum_of_passed_courses = reduce(lambda initial, item: item.grade + initial, courses,0)
    return sum_of_passed_courses / len(passed_courses)


if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    credit_sum = average([s1, s2, s3])
    print(credit_sum)