# individual course
from typing import Any


class Course:
    def __init__(self, args) -> None:
        [self.title, self.instructor, self.date, self.minEmp, self.maxEmp] = args
        self.isAlloted = False
        self.regEmps = []
        self.currEmp = 0

    def setValue(self, attr, value) -> None:
        setattr(self, attr, value)

    def getValue(self, attr) -> Any:
        return getattr(self, attr)

    def checkSeat(self) -> bool:
        if self.currEmp >= self.maxEmp:
            return False
        else:
            return True

    def printNice(self, courseId) -> None:
        self.regEmps =  sorted(self.regEmps)
        self.isAlloted = True

        if self.currEmp > self.minEmp:
            cancel = " CONFIRMED"
        else:
            cancel = " COURSE_CANCELED"

        for emp in self.regEmps:
            [name, _] = emp.split("@")
            courseTitle = "REG-COURSE-" + name + "-" + self.title

            print(
                courseTitle,
                emp,
                courseId,
                self.title,
                self.instructor,
                self.date + cancel,
            )

    # add a new student
    def addStudent(self, email):
        self.regEmps.append(email)
        self.setValue("currEmp", self.currEmp + 1)

    # remove a student
    def removeStudent(self, name):
        for emp in self.regEmps:
            [parsedName, _] = emp.split("@")

            if parsedName == name:
                self.regEmps.remove(emp)
                self.setValue("currEmp", self.currEmp - 1)
