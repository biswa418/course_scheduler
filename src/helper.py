from datetime import datetime


def courseValid(args) -> list:
    try:
        [title, instructor, date, minEmp, maxEmp] = args
        maxEmp = int(maxEmp)
        minEmp = int(minEmp)
    except:
        return [False, args]

    return [True, [title, instructor, date, minEmp, maxEmp]]
