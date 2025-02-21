def format_list_as_struct(lst, struct_name="transaction", traductions = "", var_name="all_transactions", double_field=False):
    struct_name = input(traductions["struct_prompt_name"]).strip() or struct_name
    var_name = input(traductions["struct_prompt_list"]).strip() or var_name
    
    print(traductions["struct_prompt_fields"])
    fields = input().strip().split(',')
    
    struct_def = "struct " + struct_name + " {\n    " + ";\n    ".join(f"std::string {field.strip()}" for field in fields) + ";\n};\n\n"
    
    formatted_items = []
    for item in lst:
        name, value = item[0].split(":", 1)
        name = name.strip()
        value = value.strip()
        
        if value.isdigit():
            formatted_item = f'{{"{name}", {value}}}'
        else:
            formatted_item = f'{{"{name}", "{value}"}}'

        formatted_items.append(formatted_item)
    
    formatted_output = struct_def + 'std::vector<' + struct_name + '> ' + var_name + ' = {\n    ' + ',\n    '.join(formatted_items) + '\n};'
    
    return formatted_output
