import csv
from tabulate import tabulate
from varname import argname # type: ignore


course_table = []
courseoffering_table = []
studcourse_table = []
student_table = []
studenthistory_table = []


def readFile(path): # read csv file given path
    integer_types = ["UnitsEarned", "NoOfUnits", "HasLab", "MaxStud"] # integer columns for typecasting

    data = []

    with open(path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
    
        for row in csv_reader:
            for column in row:
                if column in integer_types:
                    row[column] = int(row[column])
            data.append(dict(row))

    return data # returns list of dictionaries


def printTable(table): # prints table using tabulate given list of dictionaries
    print(tabulate(table, headers="keys", tablefmt="grid"))


def writeFile(table): # when an INSERT or DELETE statement is executed, run this function to update csv file
    path = "data/" + argname('table') + ".csv" # argname() gets the variable name of actual parameter

    with open(path, mode='w', newline='', encoding='utf-8') as file:
        if len(table) > 0:
            fieldnames = table[0].keys()

            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer.writeheader()

            csv_writer.writerows(table)


def main():
    print("READING FILES...\n")

    course_table = readFile("data/course_table.csv")
    courseoffering_table = readFile("data/courseoffering_table.csv")
    studcourse_table = readFile("data/studcourse_table.csv")
    student_table = readFile("data/student_table.csv")
    studenthistory_table = readFile("data/studenthistory_table.csv")
    
    # printTable(course_table) # sample function call to print table
    # printTable(courseoffering_table)
    # printTable(studcourse_table)
    # printTable(student_table)
    # printTable(studenthistory_table)

    print("SUCCESSFULLY READ FILES!\n")

    # writeFile(course_table) # sample function call to write table
    

main()