import os
import time
from colorama import Fore, init

init(autoreset=True)

from catalog import extract_keys
from crossmap import filter_cm
from gen_crossmap import (
    load_crossmap_data,
    allocate_crossmap_indices,
    write_crossmap_header,
)
from gen_native import load_natives_data, write_natives_header
from gen_catalog import generate_catalog
from gen_list import format_list_as_struct
from lang import load_traductions
from util import print_gradient


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

        print(Fore.BLUE + traductions["menu_filter_catalog"])
        print(Fore.BLUE + traductions["menu_format_catalog"])
        print(Fore.BLUE + traductions["menu_filter_crossmap"])
        print(Fore.BLUE + traductions["menu_generate_crossmap"])
        print(Fore.BLUE + traductions["menu_generate_native"])
        print(Fore.BLUE + traductions["menu_generate_struct_list"])
        print(Fore.RED + traductions["menu_quit"])

        choice = input(Fore.WHITE + traductions["enter_choice"])

        if choice == "1":
            input_file = "net_catalog/netCatalog.json"
            output_file = "net_catalog/filtered_keys.txt"
            prefixes = ["SERVICE_EARN", "SERVICE_SPEND"]
            extract_keys(input_file, output_file, prefixes, traductions)
            print(Fore.GREEN + traductions["filter_success"])

        elif choice == "2":
            generate_catalog()
            print(Fore.GREEN + traductions["format_success"])

        elif choice == "3":
            input_filename = "crossmap/crossmap.txt"
            end_input = "crossmap/new_cm.txt"
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

        elif choice == "6":
            input_file = "list/input.txt"
            output_file = "list/output.txt"

            with open(input_file, "r", encoding="utf-8") as file:
                transactions = [
                    tuple(line.strip().split(",")) for line in file if line.strip()
                ]

            formatted_output = format_list_as_struct(transactions, traductions)

            with open(output_file, "w", encoding="utf-8") as file:
                file.write(formatted_output)
            print(Fore.GREEN + traductions["struct_generate_success"])

        elif choice == "7":
            print(Fore.RED + traductions["menu_quit"])
            break

        else:
            print(Fore.RED + traductions["invalid_choice"])

        clear_console()


if __name__ == "__main__":
    main()
