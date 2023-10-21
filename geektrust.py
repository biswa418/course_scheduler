from sys import argv
import sys
from src.Courses import Courses
from parseMain import parseLine

def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    
    file_path = sys.argv[1]
    courses = Courses()
    parseLine(file_path, courses) #read command and send
    
if __name__ == "__main__":
    main()