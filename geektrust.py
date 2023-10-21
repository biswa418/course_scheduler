from sys import argv
from src.Courses import Courses

def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    
    file_path = argv[1]
    courses = Courses()
    
    with open(file_path, 'r') as readLine:
        for i in readLine:
            line = i.rstrip()
            command = line.split(' ')[0]
            
            match command:
                case 'ADD-COURSE-OFFERING':
                    courses.add_course(line.split(' ')[1::])
             
    
if __name__ == "__main__":
    main()