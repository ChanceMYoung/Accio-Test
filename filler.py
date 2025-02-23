import json

# Load the JSON file
with open('cards.json', 'r') as file:
    cards = json.load(file)

# Create sets to store unique types and subtypes
all_types = set()
all_subtypes = set()

# Iterate through each card in the JSON data
for card in cards:
    # Check if the card has a 'type' key and add each type
    if 'type' in card and isinstance(card['type'], list):
        for t in card['type']:
            all_types.add(t)
    # Check if the card has a 'subTypes' key and add each subtype
    if 'subTypes' in card and isinstance(card['subTypes'], list):
        for st in card['subTypes']:
            all_subtypes.add(st)

# Print the results
print("Unique Types:")
for t in sorted(all_types):
    print(t)

print("\nUnique Subtypes:")
for st in sorted(all_subtypes):
    print(st)
