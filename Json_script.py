import json
"""
This creates a json data file based on a given schema.
It also allows you to edit the json
"""

# Data to be written to the JSON file
data = {
    "Sample1": {
        "Attribute1": "Value1",
        "Attribute2": "Value2",
        "Attribute3": "Value3"
    },
    "Sample2": {
        "Attribute1": "Value4",
        "Attribute2": "Value5",
        "Attribute3": "Value6"
    },
    "Sample3": {
        "Attribute1": "Value7",
        "Attribute2": "Value8",
        "Attribute3": "Value9"
    }
}

# Specify the file name
file_name = "output.json"

# Write data to the JSON file
with open(file_name, 'w') as json_file:
    json.dump(data, json_file, indent=2)

print(f"JSON data has been written to {file_name}")

#__________________________


def edit_json(file_name, field_to_edit, new_value):
    # Read existing data from the JSON file
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)

    # Update the specified field with the new value
    data[field_to_edit] = new_value

    # Write the updated data back to the JSON file
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=2)

    print(f"Field '{field_to_edit}' updated with value '{new_value}' in {file_name}")


file_name = "output.json"
field_to_edit = "sample2"
new_value = "testing"

# Call the function to edit the JSON file
edit_json(file_name, field_to_edit, new_value)


# To Do: 
# parse any part of the json file and edit
# Create a CLI for the above task
