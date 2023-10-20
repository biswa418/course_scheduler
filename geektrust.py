from sys import argv

def main():
    
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    
    with open(file_path, 'r') as readLine:
        for i in readLine:
            print(i.rstrip())

    # print(Lines)
    
if __name__ == "__main__":
    main()