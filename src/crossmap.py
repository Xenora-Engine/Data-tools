import os


def filter_cm(entree, sortie, traductions):
    try:
        if not os.path.exists(entree):
            with open(entree, "w", encoding="utf-8") as f:
                f.write("")

        with open(entree, "r", encoding="utf-8") as f:
            lignes = f.readlines()

        # Nettoyer les lignes et ajouter les accolades si besoin
        lignes_modifiees = [ligne.strip() for ligne in lignes]  # Supprime espaces et sauts de ligne
        lignes_avec_accolades = [f"{{{ligne}}}" if not ligne.startswith("{") or not ligne.endswith("}") else ligne for ligne in lignes_modifiees]

        # Trier les lignes avec accolades
        lignes_triees = sorted(lignes_avec_accolades)

        # Ajouter une virgule à la fin de chaque ligne
        lignes_finales = [ligne + "," for ligne in lignes_triees]

        with open(sortie, "w", encoding="utf-8") as f:
            f.writelines("\n".join(lignes_finales) + "\n")  # Ajout de sauts de ligne corrects

        print(traductions["filter_cm_success"].format(file=sortie))
    except Exception as e:
        print(traductions["filter_error"].format(error=e))
