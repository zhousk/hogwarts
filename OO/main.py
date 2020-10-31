from OO.elementary_student import ElementaryStudent
from OO.middle_school_student import MiddleSchoolStudent
from OO.student import Student
from OO.teacher import Teacher

if __name__ == "__main__":
    teacher1 = Teacher("黄老师", "27")
    elementaryStudent = ElementaryStudent("小明", "17")
    middleSchoolStudent = MiddleSchoolStudent("小红", "18")

    teacher1.work()
    elementaryStudent.work()
    middleSchoolStudent.work()

    teacher1.teach(elementaryStudent)
    teacher1.teach(middleSchoolStudent)
