import re
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


def courseValid(args: list):
    if(len(args) != 5):
        return False
    
    [validity, obj] = validDate(args[2])

    print(validity, obj)


ans = courseValid(['DATASCIENCE', 'BOB', '05062022', 1, 3]);
print(ans)