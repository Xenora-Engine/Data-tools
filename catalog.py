import json

def extract_keys(input_file, output_file, prefixes):
    with open(input_file, 'r') as infile:
        data = json.load(infile)

    keys = [item['key'] for item in data.get('items', [])]

    matching_keys = [key for key in keys if key.startswith(tuple(prefixes))]

    with open(output_file, 'w') as outfile:
        for key in matching_keys:
            outfile.write(key + '\n')

    print(f"Successfuly filter in '{output_file}'.")
