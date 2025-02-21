def format_list_as_struct(lst, struct_name="transaction", var_name="all_transactions", double_field=False):
    struct_name = input("Enter the name of the struct : ").strip() or struct_name
    var_name = input("Enter the name of list : ").strip() or var_name
    
    print("Enter the argument for the struct :")
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
