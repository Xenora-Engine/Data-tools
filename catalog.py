import json

def extract_keys(input_file, output_file, prefixes):
    with open(input_file, 'r') as infile:
        data = json.load(infile)

    matching_items = [
        (item['key'], item.get('price', 'N/A'))
        for item in data.get('items', [])
        if item['key'].startswith(tuple(prefixes))
    ]

    with open(output_file, 'w') as outfile:
        for key, price in matching_items:
            outfile.write(f"{key}: {price}\n")

    print(f"Succès ! Les données filtrées ont été enregistrées dans '{output_file}'.")
