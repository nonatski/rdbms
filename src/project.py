import os
import csv
from tabulate import tabulate
from antlr4 import *
from compiler.parser.SQLParser import SQLParser
from compiler.parser.SQLLexer import SQLLexer


class SQLHandler:
    def handle_sql_statement(self, statement):
        statement_context = statement[0] if isinstance(statement, list) else statement

        # Check for SELECT statement
        select_statements = statement_context.select_statement()
        if select_statements:
            self.handle_select(select_statements[0])
            return

        # Check for INSERT statement
        insert_statements = statement_context.insert_statement()
        if insert_statements:
            self.handle_insert(insert_statements[0])
            return

        # Check for DELETE statement
        delete_statements = statement_context.delete_statement()
        if delete_statements:
            self.handle_delete(delete_statements[0])
            return

        print("No valid SQL statement found.")  # Debug output

    def handle_select(self, select_statement_context):
        column_list_context = select_statement_context.column_list()
        columns = self.extract_columns(column_list_context)

        tables = []
        table_list_contexts = select_statement_context.table_list()
        for table_context in table_list_contexts:
            table_name = table_context.getText()
            tables.append(table_name)

        where_clause_context = select_statement_context.where_clause()
        conditions = self.extract_conditions(where_clause_context) if where_clause_context else None
        self.execute_select_query(columns, tables, conditions)

    def handle_insert(self, insert_statement_context):
        # Access the table list context
        table_list_context = insert_statement_context.table_list()

        if table_list_context is None:
            print("No table specified in INSERT statement.")
            return

        # Extract the first table name from the context
        if hasattr(table_list_context, 'WORD'):
            table_name = table_list_context.WORD(0).getText()  # Adjust based on your grammar's context structure
        else:
            print("Table list context does not have WORD attribute.")
            return

        # Access the values context
        values_context = insert_statement_context.values_list()

        if values_context is None:
            print("No values specified in INSERT statement.")
            return

        # Extract values
        values = self.extract_values(values_context)

        # Now insert the values into the specified table
        self.execute_insert_query(table_name, values)

    def handle_delete(self, delete_statement_context):
        # Access the table list context
        table_list_context = delete_statement_context.table_list()
        if table_list_context is None:
            print("No table specified in DELETE statement.")
            return

        # Extract the first table name from the context
        table_name = table_list_context.WORD(0).getText()  # Assuming table_list contains WORD contexts

        # Access the where clause
        where_clause_context = delete_statement_context.where_clause()
        conditions = self.extract_conditions(where_clause_context) if where_clause_context else None

        # Now execute the delete query
        self.execute_delete_query(table_name, conditions)

    def extract_columns(self, column_list_context):
        return [column.getText() for column in column_list_context.getTypedRuleContexts(SQLParser.ColumnContext)]

    def extract_values(self, values_list_context):
        values = []

        if values_list_context is None:
            print("Values list context is None.")
            return values

        # Extract value contexts
        for value_context in values_list_context.value():
            if value_context is None:
                print("Value context is None.")
                continue  # Skip this iteration if the context is None

            if hasattr(value_context, 'STRING') and value_context.STRING() is not None:
                values.append(value_context.STRING().getText().strip("'"))  # Remove surrounding single quotes
            elif hasattr(value_context, 'NUMBER') and value_context.NUMBER() is not None:
                values.append(int(value_context.NUMBER().getText()))  # Convert to int
            else:
                values.append(value_context.getText())  # Handle NULL or other types

        return values

    def extract_conditions(self, where_clause_context):
        conditions = []
        condition_list_context = where_clause_context.condition_list()
        for expression in condition_list_context.getTypedRuleContexts(SQLParser.ExpressionContext):
            conditions.append(expression.getText())
        return conditions

    def execute_select_query(self, columns, tables, conditions):
        if not tables:
            print("Error: No table specified in SELECT statement.")
            return

        table_name = tables[0]
        table_map = {
            "course_table": "data/course_table.csv",
            "student_table": "data/student_table.csv",
            "courseoffering_table": "data/courseoffering_table.csv",
            "studcourse_table": "data/studcourse_table.csv",
            "studenthistory_table": "data/studenthistory_table.csv",
        }

        if table_name in table_map:
            csv_path = table_map[table_name]
            if not os.path.exists(csv_path):
                print(f"Error: Table '{table_name}' not found.")
                return
            try:
                with open(csv_path, mode='r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)

                    # Apply conditions to filter rows
                    if conditions:
                        rows = [row for row in rows if all(self.evaluate_condition(row, cond) for cond in conditions)]

                    # Display all columns if columns list is empty (equivalent to *)
                    if not columns or columns == ["*"]:
                        display_rows = rows
                    else:
                        display_rows = [{col: row.get(col, "") for col in columns} for row in rows]

                    # Display filtered results or a no-matching-records message
                    if display_rows:
                        print(tabulate(display_rows, headers='keys', tablefmt='grid'))
                    else:
                        print("No records found matching the query.")
            except Exception as e:
                print(f"An error occurred while reading the CSV file: {e}")

    def execute_insert_query(self, table_name, values):
        table_map = {
            "course_table": "data/course_table.csv",
            "student_table": "data/student_table.csv",
            "courseoffering_table": "data/courseoffering_table.csv",
            "studcourse_table": "data/studcourse_table.csv",
            "studenthistory_table": "data/studenthistory_table.csv",
        }

        if table_name in table_map:
            csv_path = table_map[table_name]
            if not os.path.exists(csv_path):
                print(f"Error: Table '{table_name}' not found.")
                return

            try:
                # Read existing data
                with open(csv_path, mode='r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)

                # Create a new row with the values
                new_row = {col: value for col, value in
                           zip(rows[0].keys(), values)}  # Use column names from existing data

                # Append the new row to the list
                rows.append(new_row)

                # Write back to the CSV
                with open(csv_path, mode='w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=rows[0].keys())
                    writer.writeheader()
                    writer.writerows(rows)

                print("Insert successful.")
            except Exception as e:
                print(f"An error occurred while writing to the CSV file: {e}")

    def execute_delete_query(self, table_name, conditions):
        table_map = {
            "course_table": "data/course_table.csv",
            "student_table": "data/student_table.csv",
            "courseoffering_table": "data/courseoffering_table.csv",
            "studcourse_table": "data/studcourse_table.csv",
            "studenthistory_table": "data/studenthistory_table.csv",
        }

        if table_name in table_map:
            csv_path = table_map[table_name]
            if not os.path.exists(csv_path):
                print(f"Error: Table '{table_name}' not found.")
                return

            try:
                # Read existing data
                with open(csv_path, mode='r') as file:
                    reader = csv.DictReader(file)
                    rows = list(reader)

                # If no conditions specified, delete all rows
                if conditions is None or len(conditions) == 0:
                    rows.clear()  # Clear all rows
                    print("All rows deleted from the table.")
                else:
                    # Apply conditions to filter out rows to delete
                    rows = [row for row in rows if not all(self.evaluate_condition(row, cond) for cond in conditions)]

                # Write back to the CSV
                with open(csv_path, mode='w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=rows[0].keys() if rows else [])
                    writer.writeheader()
                    writer.writerows(rows)

                print("Delete successful.")
            except Exception as e:
                print(f"An error occurred while writing to the CSV file: {e}")

    def evaluate_condition(self, row, condition):
        # Split condition into column and value while accounting for spaces in values
        column, value = condition.split('=')
        column = column.strip()
        value = value.strip().strip("'")  # Remove surrounding single quotes if any

        # Handle numeric values by converting if possible
        if value.isdigit():
            value = int(value)
        elif value.replace('.', '', 1).isdigit():  # Check for float
            value = float(value)

        # Retrieve the row value for the specified column
        row_value = row.get(column)
        if row_value is None:
            print(f"Warning: Column '{column}' not found in row.")
            return False

        # Check for equality condition
        return str(row_value) == str(value)  # Convert to string for comparison


def main():
    sql_handler = SQLHandler()
    while True:
        try:
            sql_query = input("Enter your SQL query (or type 'exit' to quit): ")
            if sql_query.lower() == 'exit':
                print("Exiting the program.")
                break

            input_stream = InputStream(sql_query)
            lexer = SQLLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = SQLParser(token_stream)
            tree = parser.sql_statement()

            sql_handler.handle_sql_statement(tree)

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
