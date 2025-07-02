import json
import csv
import pandas as pd # you import pandas but don't use it yet, you can keep or remove

input_path = 'Data/Raw/Takeout/Yt_and_ytmusic/yt_002/history/search-history.json'
output_path = 'Data/Cleaned/search_history_cleaned.csv'

# Load the JSON file
with open('Data/Raw/Takeout/Yt_and_ytmusic/yt_002/history/search-history.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

rows = []
for entry in data:
    row = {
        'header': entry.get('header', ''),
        'title': entry.get('title', ''),
        'titleUrl': entry.get('titleUrl', ''),
        'description': entry.get('description', ''),
        'time': entry.get('time', ''),
        #Flatten lists into comma-sperated strings
        'products': ', '.join(entry.get('products', [])) if isinstance(entry.get('products'), list) else '',
        'activityControls': ', '.join(entry.get('activityControls', [])) if isinstance(entry.get('activityControls'), list) else '', 
    }

    #For details (lists of dicts), join all 'name' values, fallback to string conversation
    details = entry.get('details', [])
    if isinstance(details, list):
        names = []
        for d in details:
            if isinstance(d, dict) and 'name' in d:
                names.append(d['name'])
            else: 
                names.append(str(d))
        row['details'] = ', '.join(names)
    else: 
        row['details'] = ''

    rows.append(row)

#write to CSV
with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['header', 'title', 'titleUrl', 'description', 'time', 'products', 'details', 'activityControls']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Exported {len(rows)} rows to {output_path}")

