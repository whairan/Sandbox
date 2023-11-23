import csv

# Sample data
data = [
    ['Name', 'Age', 'City'],
    ['John', 25, 'New York'],
    ['Alice', 30, 'San Francisco'],
    ['Bob', 22, 'Los Angeles']
]

# Specify the file path
csv_file_path = 'info.csv'

# Writing to the CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write the data to the CSV file
    csv_writer.writerows(data)

print(f'CSV file "{csv_file_path}" created successfully.')
