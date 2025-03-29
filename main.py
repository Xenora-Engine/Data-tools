import os
import time
from colorama import Fore, init

init(autoreset=True)

from src.catalog import extract_keys
from src.crossmap import filter_cm
from src.gen_crossmap import (
    load_crossmap_data,
    allocate_crossmap_indices,
    write_crossmap_header,
)
from src.gen_native import load_natives_data, write_natives_header
from src.gen_catalog import generate_catalog
from src.gen_list import format_list_as_struct
from src.lang import load_traductions
from src.util import print_gradient


def clear_console():
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")


def main():
    langue = (
        input(
            Fore.GREEN
            + "Enter your lang ('en', 'fr', 'al', 'es', 'it', 'jp', 'pt', 'rs', 'cn') : "
        ).strip()
        or "en"
    )
    traductions = load_traductions(langue)

    while True:
        ascii_art = """                                                                                                                                                                                                                            
    ,---,                   ___                            ___                         ,--,               
  .'  .' `\               ,--.'|_                        ,--.'|_                     ,--.'|               
,---.'     \              |  | :,'                       |  | :,'   ,---.     ,---.  |  | :               
|   |  .`\  |             :  : ' :                       :  : ' :  '   ,'\   '   ,'\ :  : '    .--.--.    
:   : |  '  |  ,--.--.  .;__,'  /    ,--.--.           .;__,'  /  /   /   | /   /   ||  ' |   /  /    '   
|   ' '  ;  : /       \ |  |   |    /       \          |  |   |  .   ; ,. :.   ; ,. :'  | |  |  :  /`./   
'   | ;  .  |.--.  .-. |:__,'| :   .--.  .-. |         :__,'| :  '   | |: :'   | |: :|  | :  |  :  ;_     
|   | :  |  ' \__\/: . .  '  : |__  \__\/: . .           '  : |__'   | .; :'   | .; :'  : |__ \  \    `.  
'   : | /  ;  ," .--.; |  |  | '.'| ," .--.; |           |  | '.'|   :    ||   :    ||  | '.'| `----.   \ 
|   | '` ,/  /  /  ,.  |  ;  :    ;/  /  ,.  |           ;  :    ;\   \  /  \   \  / ;  :    ;/  /`--'  / 
;   :  .'   ;  :   .'   \ |  ,   /;  :   .'   \          |  ,   /  `----'    `----'  |  ,   /'--'.     /  
|   ,.'     |  ,     .-./  ---`-' |  ,     .-./           ---`-'                      ---`-'   `--'---'   
'---'        `--`---'              `--`---'                                                                                                                                                                         
"""
        print_gradient(ascii_art)

        print_gradient(traductions["menu_filter_catalog"])
        print_gradient(traductions["menu_format_catalog"])
        print_gradient(traductions["menu_filter_crossmap"])
        print_gradient(traductions["menu_generate_crossmap"])
        print_gradient(traductions["menu_generate_native"])
        print_gradient(traductions["menu_generate_struct_list"])
        print_gradient(traductions["menu_quit"])

        choice = input(Fore.WHITE + traductions["enter_choice"])

        if choice == "1":
            input_file = "src/net_catalog/netCatalog.json"
            output_file = "src/net_catalog/filtered_keys.txt"
            prefixes = ["SERVICE_EARN", "SERVICE_SPEND"]
            extract_keys(input_file, output_file, prefixes, traductions)
            print(Fore.GREEN + traductions["filter_success"])

        elif choice == "2":
            generate_catalog()
            print(Fore.GREEN + traductions["format_success"])

        elif choice == "3":
            input_filename = "src/crossmap/crossmap.txt"
            end_input = "src/crossmap/new_cm.txt"
            filter_cm(input_filename, end_input, traductions)
            print(Fore.GREEN + traductions["crossmap_filter_success"])

        elif choice == "4":
            load_crossmap_data()
            allocate_crossmap_indices()
            write_crossmap_header()
            print(Fore.GREEN + traductions["crossmap_generate_success"])

        elif choice == "5":
            load_natives_data()
            write_natives_header()
            print(Fore.GREEN + traductions["native_generate_success"])

        # elif choice == "6":
        #     input_file = "src/list/input.txt"
        #     output_file = "src/list/output.txt"

        #     with open(input_file, "r", encoding="utf-8") as file:
        #         transactions = [
        #             tuple(line.strip().split(",")) for line in file if line.strip()
        #         ]

        #     print(f"DEBUG: traductions avant appel -> {type(traductions)}")
        #     formatted_output = format_list_as_struct(transactions, traductions)

        #     with open(output_file, "w", encoding="utf-8") as file:
        #         file.write(formatted_output)
        #     print(Fore.GREEN + traductions["struct_generate_success"])

        elif choice == "7":
            print(Fore.RED + traductions["menu_quit"])
            break

        else:
            print(Fore.RED + traductions["invalid_choice"])

        clear_console()


if __name__ == "__main__":
    main()
