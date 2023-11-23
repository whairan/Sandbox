import pandas as pd

def check_names(input_names, file_path):
    # Read the data from the Excel or CSV file
    try:
        if file_path.endswith('.xlsx'):
            data = pd.read_excel(file_path)
        elif file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
        else:
            raise ValueError("Unsupported file format. Please provide either an Excel (.xlsx) or CSV (.csv) file.")
    except Exception as e:
        print(f"Error reading the file: {e}")
        return

    # Print the column names in the DataFrame
    print("Column names in the DataFrame:")
    print(data.columns.tolist())
    # print(data.columns[1])



    # print(data)
    # for name in input_names: 

    # Check if each input name is in the column names (case-insensitive)
    # for name in input_names:
    #     if name.lower() in map(str.lower, data.columns):
    #         print(f"{name} is present as a column in the reference file.")
    #     else:
    #         print(f"{name} is not present as a column in the reference file.")

# Example usage
input_names = ["John", "Alice", "Bob"]
file_path = "names.csv"  # Replace with the actual file path

check_names(input_names, file_path)


import pandas as pd

def print_column(csv_file, column_name):
    try:
        # Read the CSV file into a DataFrame
        data = pd.read_csv(csv_file)
        
        # Check if the specified column exists in the DataFrame
        if column_name not in data.columns:
            print(f"Column '{column_name}' not found in the CSV file.")
            return

        # Print the specified column
        column_data = data[column_name]
        print(f"Printing values from the '{column_name}' column:")
        print(column_data)

    except Exception as e:
        print(f"Error reading the file: {e}")

# Example usage
csv_file_path = "info.csv"  # Replace with the actual file path
column_to_print = "Name"  # Replace with the actual column name

print_column(csv_file_path, column_to_print)
