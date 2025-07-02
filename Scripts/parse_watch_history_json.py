import json
import csv
import pandas as pd # you import pandas but don't use it yet, you can keep or remove

input_path = 'Data/Raw/Takeout/Yt_and_ytmusic/yt_002/history/watch-history.json'
output_path = 'Data/Cleaned/watch_history_cleaned.csv'

# Load the JSON file
with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

rows = []
for entry in data:
    # Extract subtitle (channel name) if avaliable
    subtitles = entry.get('subtitles', [])
    if isinstance(subtitles, list) and len(subtitles) > 0:
        channel_name = subtitles[0].get('name', '')
    else:
        channel_name = ''

    #Extract details (optional)
    details = entry.get('details', [])
    if isinstance(details, list):
        detail_names = []
        for d in details:
            if isinstance(d, dict) and 'name' in d:
                detail_names.append(d['name'])
            else: 
                detail_names.append(str(d))
        detail_str = ','.join(detail_names)
    else: 
        detail_str = ''

    row = {
        'header': entry.get('header', ''),
        'title': entry.get('title', ''),
        'titleUrl': entry.get('titleUrl', ''),
        'channel': channel_name,
        'time': entry.get('time', ''),
        'products': ','.join(entry.get('products', [])) if isinstance(entry.get('products'), list) else '',
        'details': detail_str,
        'activityControls': ','.join(entry.get('activityControls', [])) if isinstance(entry.get('activityControls'), list) else '',
    }

    rows.append(row)

#write to CSV
with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['header', 'title', 'titleUrl', 'channel', 'time', 'products', 'details', 'activityControls']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Exported {len(rows)} rows to {output_path}")

