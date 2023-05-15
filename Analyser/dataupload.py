import json

# Example data as string
data = {
    "name": "Embrace the beauty of each moment, for in your happiness lies the infinite potential to inspire and uplift those around you."
}

# Save the data to a JSON file
with open('suggestions.json', 'w') as f:
    json.dump(data, f)
