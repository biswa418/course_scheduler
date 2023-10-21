from .Course import Course
from .helper import courseValid


class Courses:
    def __init__(self) -> None:
        self.courses = {}

    # add new course
    def addCourse(self, listDetails):
        [inputValid, newDetails] = courseValid(listDetails)

        if not inputValid:
            print("INPUT_DATA_ERROR")
            return

        newCourse = Course(newDetails)
        courseId = "OFFERING-" + newCourse.title + "-" + newCourse.instructor

        if courseId in self.courses:
            print("INPUT_DATA_ERROR")
        else:
            self.courses[courseId] = newCourse
            print(courseId)

    # register a course
    def regCourse(self, courseDetails):
        [email, courseId] = courseDetails
        name = email.split("@")[0]

        if courseId in self.courses:
            currCourse = self.courses[courseId]
            isSeatAvail = currCourse.checkSeat()

            if isSeatAvail:
                print("REG_COURSE-" + name + "-" + currCourse.title + ' ACCEPTED')
                currCourse.regEmps.append(email)
            else:
                print('COURSE_FULL_ERROR')

        else:
            print("INPUT_DATA_ERROR")
            return

    # cancel a course
    def cancelCourse(self):
        pass
