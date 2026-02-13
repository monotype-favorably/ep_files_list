import json
import pandas as pd
import csv

def parse_json(json_data):
    real_entries = []
    for entry in json_data:
        if entry.get("progress", {}).get("type") == "real":
            real_entries.append({
                'name': entry.get("name"),
                'extension': entry.get("progress", {}).get("extension")
            })
    return real_entries

with open('db.json', 'r') as f:
    json_data = json.load(f)

real_entries = parse_json(json_data)
real_df = pd.DataFrame(real_entries)

csv_df = pd.read_csv('files.csv', dtype={'record_number_padded': str})

merged_df = pd.merge(csv_df, real_df, left_on='file_stem', right_on='name', how='left')
merged_df = merged_df.drop(columns=["name"])
merged_df = merged_df.rename(columns={"extension":"file_extension"})
merged_df["file_extension"] = merged_df["file_extension"].fillna("pdf")
merged_df["file_name"] = merged_df["file_stem"] + '.' + merged_df["file_extension"]
print(merged_df.head(10))

merged_df.to_csv('files.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)
