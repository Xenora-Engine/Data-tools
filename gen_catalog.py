import re

def generate_catalog():
    def transform_key(key):
        key = key.replace("SERVICE_EARN_", "").replace("SERVICE_SPEND_", "")
        key = key.replace("_", " ")
        return key.title()

    def safe_int(value):
        try:
            return int(value.strip())
        except ValueError:
            return None

    def should_include(value):
        if value is None or value < 10:
            return False
        return True

    with open("net_catalog/filtered_keys.txt", "r") as f:
        lines = f.readlines()

    transactions = []

    for line in lines:
        if ":" in line:
            key, value = line.strip().split(":", 1)
            value_int = safe_int(value)
            if value_int is not None and should_include(value_int):
                readable = f"{transform_key(key)} ({value_int})"
                transactions.append((readable, key, value_int))  # Ajout de la valeur entière pour tri

    # Trier les transactions par valeur (du plus grand au plus petit)
    transactions.sort(key=lambda x: x[2], reverse=True)

    with open("net_catalog/catalog.txt", "w") as f:
        f.write("#pragma once\n\n")
        f.write("namespace zenith\n{\n")
        f.write("    struct transaction {\n")
        f.write("        std::string name;\n")
        f.write("        std::string hash;\n")
        f.write("    };\n\n")
        f.write("    std::vector<transaction> all_transactions = {\n")
        for t in transactions:
            name, orig, _ = t  # On prend juste le nom et l'original
            f.write(f'        {{"{name}", "{orig}"}},\n')
        f.write("    };\n")
        f.write("}\n")
