# individual course
from typing import Any


class Course:
    def __init__(self, args) -> None:
        [self.title, self.instructor, self.date, self.minEmp, self.maxEmp] = args
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
            self.setValue("currEmp", self.currEmp + 1)
            return True

    def printNice(self) -> None:
        print("Title - ", self.title)
        print("Instructor - ", self.instructor)
        print("Date - ", self.date)
        print("minEmp - ", self.minEmp)
        print("maxEmp - ", self.maxEmp)
