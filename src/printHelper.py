class PrintHelper:
    def __init__(self) -> None:
        self.inputError = "INPUT_DATA_ERROR"
        self.courseError = "COURSE_FULL_ERROR"
        self.regiCourse = "REG-COURSE-"
        self.offerCors = "OFFERING-"

    def inputErr(self):
        print(self.inputError)

    def courseErr(self):
        print(self.courseError)

    def regCourse(self, name, title):
        print(self.regiCourse + name + "-" + title + " ACCEPTED")

    def offerCourse(self, title, instructor):
        return self.offerCors + title + "-" + instructor
