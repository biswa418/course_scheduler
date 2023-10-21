# main conditional file
def parse(command, restParams, courses):
    if command == "ADD-COURSE-OFFERING":
        courses.addCourse(restParams)

    elif command == "REGISTER":
        courses.regCourse(restParams)

    elif command == "ALLOT":
        courses.allotCourse(restParams)

    elif command == "CANCEL":
        courses.cancelCourse(restParams)

# line by line parsing
def parseLine(file_path, courses):
    with open(file_path, "r") as readLine:
        for i in readLine:
            line = i.rstrip()
            command = line.split(" ")[0]
            restParams = line.split(" ")[1::]
            parse(command, restParams, courses)
