import csv
from tabulate import tabulate
from varname import argname  # type: ignore


# Tables represented as lists of dictionaries
course_table = []
courseoffering_table = []
studcourse_table = []
student_table = []
studenthistory_table = []


def readFile(path):  # Read CSV file given path
    integer_types = ["NoOfUnits", "HasLab", "MaxStud", "UnitsEarned"]  # Integer columns for typecasting
    data = []

    with open(path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            for column in row:
                if column in integer_types:
                    row[column] = int(row[column])  # Typecast integer columns
            data.append(dict(row))

    return data  # Returns list of dictionaries


def printTable(table):  # Prints table using tabulate given list of dictionaries
    print(tabulate(table, headers="keys", tablefmt="grid"))


def writeFile(table, file_name):  # Accept file_name as a parameter
    path = f"data/{file_name}.csv"  # Construct the path with the provided file name

    with open(path, mode='w', newline='', encoding='utf-8') as file:
        if len(table) > 0:
            fieldnames = table[0].keys()
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(table)  # Write updated data to CSV


def parse_criteria(criteria_str):
    """Parse the criteria string into a dictionary."""
    criteria = {}
    if criteria_str:
        for criterion in criteria_str.split("AND"):
            key, value = criterion.split("=")
            criteria[key.strip()] = value.strip().strip('"')  # Strip quotes from values
    return criteria


def select(table, criteria=None):  # SELECT function with optional criteria
    if criteria is None:
        printTable(table)  # Select all if no criteria
    else:
        # Parse criteria into a dictionary
        parsed_criteria = parse_criteria(criteria)
        filtered_table = []

        for row in table:
            match = True
            for key, value in parsed_criteria.items():
                if str(row[key]) != str(value):  # Compare as strings for flexibility
                    match = False
                    break
            if match:
                filtered_table.append(row)

        if filtered_table:
            printTable(filtered_table)  # Print filtered results
        else:
            print("No matching records found.")  # Inform the user if no records match


def insert(table, new_record, file_name):  # Add file_name parameter
    # Ensure new record matches the table structure
    if set(new_record.keys()).issubset(table[0].keys()):
        table.append(new_record)  # Add new record to the table
        writeFile(table, file_name)  # Pass the table's file name to writeFile
        print("INSERT operation successful!")
    else:
        print("Error: The new record's fields do not match the table columns.")


def delete(table, criteria, file_name):  # Add file_name parameter
    original_len = len(table)
    # Ensure criteria contains the correct keys
    table[:] = [row for row in table if not all(row[key] == value for key, value in criteria.items())]
    if len(table) < original_len:
        writeFile(table, file_name)  # Pass the table's file name to writeFile
        print("DELETE operation successful!")
    else:
        print("No matching records found to delete.")


def parse_query(query):
    query = query.strip()
    if query.lower().startswith("insert into"):
        # Format: INSERT INTO table_name VALUES (value1, value2, ...)
        parts = query.split("VALUES", 1)
        table_name = parts[0].split()[2]  # Extract table name
        values_part = parts[1].strip().strip("()")  # Extract values and strip parentheses
        values = [value.strip().strip('"') for value in values_part.split(",")]  # Strip quotes and whitespace
        return "insert", table_name, values

    elif query.lower().startswith("select"):
        # Format: SELECT * FROM table_name WHERE ...
        parts = query.split(maxsplit=4)
        if len(parts) < 4 or parts[1] != "*":
            return None, None, None  # Invalid select statement
        table_name = parts[3]  # Extract the table name
        criteria = parts[4].replace("WHERE", "").strip() if len(parts) > 4 else None
        return "select", table_name, criteria

    elif query.lower().startswith("delete"):
        # Format: DELETE FROM table_name WHERE ...
        parts = query.split(maxsplit=3)
        table_name = parts[2]
        criteria = parts[3].replace("WHERE", "").strip() if len(parts) > 3 else None
        return "delete", table_name, criteria

    return None, None, None  # Invalid command


def main():
    print("READING FILES...\n")

    global course_table  # Declare global to modify the global variable
    course_table = readFile("data/course_table.csv")
    courseoffering_table = readFile("data/courseoffering_table.csv")
    studcourse_table = readFile("data/studcourse_table.csv")
    student_table = readFile("data/student_table.csv")
    studenthistory_table = readFile("data/studenthistory_table.csv")

    print("SUCCESSFULLY READ FILES!\n")

    table_mapping = {
        "course_table": (course_table, "course_table"),
        "courseoffering_table": (courseoffering_table, "courseoffering_table"),
        "studcourse_table": (studcourse_table, "studcourse_table"),
        "student_table": (student_table, "student_table"),
        "studenthistory_table": (studenthistory_table, "studenthistory_table")
    }

    while True:
        query = input("Input query (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            print("Exiting program.")
            break

        command, table_name, data = parse_query(query)

        if command == "select" and table_name in table_mapping:
            criteria = data  # Use data directly as the criteria
            select(table_mapping[table_name][0], criteria)

        elif command == "insert" and table_name in table_mapping:
            new_record = {}
            field_names = table_mapping[table_name][0][0].keys()  # Get the field names from the first row of the table
            if data:
                for i, field in enumerate(field_names):
                    # Map values to the corresponding field names and strip quotes
                    new_record[field] = int(data[i]) if field in ["NoOfUnits", "HasLab", "MaxStud", "UnitsEarned"] else \
                    data[i]
            insert(table_mapping[table_name][0], new_record, table_mapping[table_name][1])

        elif command == "delete" and table_name in table_mapping:
            criteria = {}
            if data:
                for criterion in data.split(","):
                    key, value = criterion.split("=")
                    criteria[key.strip()] = value.strip().strip('"')  # Strip quotes from values
            delete(table_mapping[table_name][0], criteria, table_mapping[table_name][1])

        else:
            print("Invalid command or table name!")


main()
