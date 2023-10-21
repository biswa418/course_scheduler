# individual course
class Course:
    def __init__(self, args) -> None:
        [self.title, self.instructor, self.date, self.minEmp, self.maxEmp] = args

    def printNice(self) -> None:
        print("Title - ", self.title)
        print("Instructor - ", self.instructor)
        print("Date - ", self.date)
        print("minEmp - ", self.minEmp)
        print("maxEmp - ", self.maxEmp)
