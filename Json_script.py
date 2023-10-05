import json

# Path to the JSON file
file_path = "sample_data.json"
# Read data from JSON file
with open(file_path, "r") as json_file:
    data = json.load(json_file)

# Access and manipulate the data as needed
print(data["Sample1"]["Attribute1"])  # Accessing a specific value
# Modify the data dictionary as needed
data["Sample1"]["Attribute1"] = "NewValue"

# Write the modified data back to the JSON file if desired
with open(file_path, "w") as json_file:
    json.dump(data, json_file, indent=5)

print(f"Data has been read from {file_path}")
# print formatted json data 
print(json.dumps(data, indent=5))

# To Do: 
# Create CLI







#__________Create JSON file_____________________________________________________________________________
# import json

# # Define your data
# data = {
#     "Sample1": {
#         "Attribute1": "Value1",
#         "Attribute2": "Value2",
#         "Attribute3": "Value3"
#     },
#     "Sample2": {
#         "Attribute1": "Value4",
#         "Attribute2": "Value5",
#         "Attribute3": "Value6"
#     },
#     "Sample3": {
#         "Attribute1": "Value7",
#         "Attribute2": "Value8",
#         "Attribute3": "Value9"
#     }
# }

# # Specify the file path where you want to save the JSON file
# file_path = "sample_data.json"

# # Write the data to the JSON file
# with open(file_path, "w") as json_file:
#     json.dump(data, json_file, indent=4)

# print(f"Data has been written to {file_path}")


"""
Notes: 
- https://12factor.net/

"""