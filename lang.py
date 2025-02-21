import json


def load_traductions(langue="fr"):
    try:
        with open(f"lang/{langue}.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found '{langue}.json'")
        with open("lang/en.json", "r", encoding="utf-8") as f:
            return json.load(f)


traductions = load_traductions("en")
