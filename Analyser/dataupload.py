import json

# Example data as string
data = {
    "name": "John Doe",
    "age": "25",
    "occupation": "Developer"
}

# Save the data to a JSON file
with open('suggestions.json', 'w') as f:
    json.dump(data, f)
