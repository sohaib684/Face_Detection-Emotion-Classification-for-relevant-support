import json

def get_suggestion(emotion):
    # Load JSON file
    with open('suggestions.json') as f:
        data = json.load(f)
    
    # Get suggestion for the input emotion
    suggestion = data.get(emotion)
    
    if suggestion:
        return suggestion
    else:
        return "No suggestion available for this emotion."

