from .Course import Course
from .helper import courseValid
from .printHelper import PrintHelper


class Courses:
    def __init__(self) -> None:
        self.courses = {}
        self.printHelp = PrintHelper()

    def setValue(self, key, value) -> None:
        self.courses[key] = value

    def getValue(self, attr) -> any:
        return self.courses[attr]

    def get(self) -> dict:
        return self.courses

    def checkCourse(self, courseId) -> bool:
        if courseId in self.get():
            return True
        return False

    def createAddCourse(self, details):
        newCourse = Course(details)
        courseId = self.printHelp.offerCourse(
            newCourse.getValue("title"), newCourse.getValue("instructor")
        )

        if self.checkCourse(courseId):
            self.printHelp.inputErr()
        else:
            self.setValue(courseId, newCourse)
            print(courseId)

    # add new course
    def addCourse(self, listDetails):
        [inputValid, newDetails] = courseValid(listDetails)

        if not inputValid:
            self.printHelp.inputErr()
            return

        self.createAddCourse(newDetails)

    # register a course
    def regCourse(self, courseDetails):
        try:
            [email, courseId] = courseDetails
            [name, _] = email.split("@")
            isSeatAvail = False

            if self.checkCourse(courseId):
                isSeatAvail = self.getValue(courseId).checkSeat()
            else:
                self.printHelp.inputErr()
                return

            if isSeatAvail:
                self.getValue(courseId).addStudent(email)
                self.printHelp.regCourse(name, self.getValue(courseId).title)
            else:
                self.printHelp.courseErr()

        except:
            self.printHelp.inputErr()
            return

    # allot a course
    def allotCourse(self, course):
        [courseId] = course

        if courseId in self.get():
            currCourse = self.getValue(courseId)
            currCourse.printNice(courseId)
        else:
            self.printHelp.inputErr()

    # cancel a course
    def cancelCourse(self, reg):
        [regId] = reg
        [_, _, name, courseName] = regId.split("-")

        for course in self.get():
            courseObj = self.getValue(course)
            title = courseObj.getValue("title")
            isAlloted = courseObj.getValue("isAlloted")

            if title == courseName and isAlloted:
                print(regId, "CANCEL_REJECTED")
            else:
                courseObj.removeStudent(name)
                print(regId, "CANCEL_ACCEPTED")
