def format_list_as_struct(
    lst,
    struct_name="transaction",
    traductions=None,
    var_name="all_transactions",
    double_field=False,
):
    # Vérification que traductions est bien un dictionnaire
    if not isinstance(traductions, dict):
        raise TypeError(
            f"❌ ERREUR : traductions doit être un dictionnaire, mais a reçu {type(traductions)} avec valeur {traductions}"
        )

    print(f"DEBUG: Traductions reçu -> {traductions}")  # Debug

    # Demander le nom de la structure
    struct_name_input = input(traductions.get("struct_prompt_name", "Enter struct name: ")).strip()
    struct_name = struct_name_input if struct_name_input else struct_name

    # Demander le nom de la variable
    var_name_input = input(traductions.get("struct_prompt_list", "Enter variable name: ")).strip()
    var_name = var_name_input if var_name_input else var_name

    # Demander les champs
    print(traductions.get("struct_prompt_fields", "Enter fields (comma-separated):"))
    fields_input = input().strip()
    
    # Vérifier si l'utilisateur a entré des champs
    if not fields_input:
        raise ValueError("❌ ERREUR : Aucun champ spécifié pour la structure !")
    
    fields = [field.strip() for field in fields_input.split(",")]

    # Générer la définition de la structure
    struct_def = (
        f"struct {struct_name} {{\n    "
        + ";\n    ".join(f"std::string {field}" for field in fields)
        + ";\n};\n\n"
    )

    formatted_items = []
    for item in lst:
        try:
            name, value = item[0].split(":", 1)
            name, value = name.strip(), value.strip()

            if value.isdigit():
                formatted_item = f'{{"{name}", {value}}}'
            else:
                formatted_item = f'{{"{name}", "{value}"}}'

            formatted_items.append(formatted_item)
        except ValueError:
            print(f"⚠️ AVERTISSEMENT : Ligne ignorée (mauvais format) -> {item}")

    # Générer la sortie finale
    formatted_output = (
        struct_def
        + f"std::vector<{struct_name}> {var_name} = {{\n    "
        + ",\n    ".join(formatted_items)
        + "\n};"
    )

    return formatted_output
