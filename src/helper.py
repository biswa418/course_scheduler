from datetime import datetime


def validDate(i) -> list:
    try:
        day = int(i[0:2])
        month = int(i[2:4])
        year = int(i[4:])
        dt_object = datetime(year, month, day)
        return [True, dt_object]
    except:
        return [False, None]


def courseValid(args) -> list:
    if len(args) != 5:
        return [False, args]

    [title, instructor, date, minEmp, maxEmp] = args

    try:
        maxEmp = int(maxEmp)
        minEmp = int(minEmp)
    except:
        return [False, args]

    [isValidDate, newDate] = validDate(date)

    if isValidDate:
        return [True, [title, instructor, newDate, minEmp, maxEmp]]
    else:
        return [False, args]
