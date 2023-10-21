from .Course import Course
from .helper import courseValid


class Courses:
    def __init__(self) -> None:
        self.courses = {}

    # add new course
    def add_course(self, listDetails):
        [inputValid, newDetails] = courseValid(listDetails)  # data validation

        if not inputValid:
            print("INPUT_DATA_ERROR")
            return

        newCourse = Course(newDetails)  # add new course
        courseId = (
            "OFFERING-" + newCourse.title + "-" + newCourse.instructor
        )  # unique course ID

        # check if course exist
        if hasattr(self.courses, courseId):
            print("INPUT_DATA_ERROR")
        else:
            self.courses[courseId] = newCourse
            print(courseId)
            # newCourse.printNice() ---------------------- DELETE AFTER DONE

    # register a course
    def regCourse(self):
        if self.currEmp == self.maxEmp:
            return "COURSE_FULL_ERROR"
        else:
            currEmp += 1
            return "ACCEPTED"

    # cancel a course
    def cancelCourse(self):
        pass
