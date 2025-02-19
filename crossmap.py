import os

def filter_cm(entree, sortie):
    try:
        if not os.path.exists(entree):
            with open(entree, 'w', encoding='utf-8') as f:
                f.write("")

        with open(entree, 'r', encoding='utf-8') as f:
            lignes = f.readlines()
        
        line_without = [ligne.replace("{", "").replace("}", "") for ligne in lignes]
        line = sorted(line_without)
        
        with open(sortie, 'w', encoding='utf-8') as f:
            f.writelines(line)
        
        print(f"Successfuly formatted : {sortie}")
    except Exception as e:
        print(f"Fatal : {e}")