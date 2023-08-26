import json
import os

def merge_all_json_files(directory, output_path):
    merged_data = {}

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                merged_data.update(data)

    with open(output_path, 'w') as output_file:
        json.dump(merged_data, output_file, indent=4)

if __name__ == "__main__":
    merge_all_json_files("/data", "finish/merged.json")
