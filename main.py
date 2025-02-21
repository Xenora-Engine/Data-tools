import os
import time
import pyfiglet
from colorama import Fore, Style, init

init(autoreset=True)

from catalog import extract_keys
from crossmap import filter_cm
from gen_crossmap import load_crossmap_data, allocate_crossmap_indices, write_crossmap_header
from gen_native import load_natives_data, write_natives_header
from gen_catalog import generate_catalog

from gen_list import format_list_as_struct

def clear_console():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        ascii_art = """       
                                                           ,----,                                       
                                                         ,/   .`|                                       
    ,---,                   ___                            ,`   .'  :                    ,--,               
  .'  .' `\               ,--.'|_                        ;    ;     /                  ,--.'|               
,---.'     \              |  | :,'                     .'___,/    ,'  ,---.     ,---.  |  | :               
|   |  .`\  |             :  : ' :                     |    :     |  '   ,'\   '   ,'\ :  : '    .--.--.    
:   : |  '  |  ,--.--.  .;__,'  /    ,--.--.           ;    |.';  ; /   /   | /   /   ||  ' |   /  /    '   
|   ' '  ;  : /       \ |  |   |    /       \          `----'  |  |.   ; ,. :.   ; ,. :'  | |  |  :  /`./   
'   | ;  .  |.--.  .-. |:__,'| :   .--.  .-. |             '   :  ;'   | |: :'   | |: :|  | :  |  :  ;_     
|   | :  |  ' \__\/: . .  '  : |__  \__\/: . .             |   |  ''   | .; :'   | .; :'  : |__ \  \    `.  
'   : | /  ;  ," .--.; |  |  | '.'| ," .--.; |             '   :  ||   :    ||   :    ||  | '.'| `----.   \ 
|   | '` ,/  /  /  ,.  |  ;  :    ;/  /  ,.  |             ;   |.'  \   \  /  \   \  / ;  :    ;/  /`--'  / 
;   :  .'   ;  :   .'   \ |  ,   /;  :   .'   \            '---'     `----'    `----'  |  ,   /'--'.     /  
|   ,.'     |  ,     .-./  ---`-' |  ,     .-./                                         ---`-'   `--'---'   
'---'        `--`---'              `--`---'                                                                                                                                                                            
        """
        print(Fore.CYAN + ascii_art)
        
        print(Fore.BLUE + "1. Filter netCatalog.json")
        print(Fore.BLUE + "2. Formated netCatalog.json")
        print(Fore.BLUE + "3. Filter crossmap.txt")
        print(Fore.BLUE + "4. Generate crossmap.txt")
        print(Fore.BLUE + "5. Generate native.txt")
        print(Fore.BLUE + "6. Generate struct and list")
        print(Fore.RED + "7. Quit")

        choice = input(Fore.WHITE + "Enter your choice: ")

        if choice == '1':
            input_file = 'net_catalog/netCatalog.json'
            output_file = 'net_catalog/filtered_keys.txt'
            prefixes = ['SERVICE_EARN', 'SERVICE_SPEND']
            extract_keys(input_file, output_file, prefixes)
            print(Fore.GREEN + "netCatalog.json filtered successfully!")

        elif choice == '2':
            generate_catalog()
            print(Fore.GREEN + "catalog formatted successfully!")

        elif choice == '3':
            input_filename = "crossmap/crossmap.txt"
            end_input = "crossmap/new_cm.txt"
            filter_cm(input_filename, end_input)
            print(Fore.GREEN + "crossmap.txt filtered successfully!")

        elif choice == '4':
            load_crossmap_data()
            allocate_crossmap_indices()
            write_crossmap_header()
            print(Fore.GREEN + "crossmap.txt generated successfully!")

        elif choice == '5':
            load_natives_data()
            write_natives_header()
            print(Fore.GREEN + "native.txt generated successfully!")

        elif choice == '6':
            input_file = "list/input.txt"
            output_file = "list/output.txt"

            with open(input_file, "r", encoding="utf-8") as file:
                transactions = [tuple(line.strip().split(',')) for line in file if line.strip()]

            formatted_output = format_list_as_struct(transactions)

            with open(output_file, "w", encoding="utf-8") as file:
                file.write(formatted_output)

        elif choice == '7':
            print(Fore.RED + "Exiting.")
            break 

        else:
            print(Fore.RED + "Invalid choice. Enter 1, 2, 3, 4, 5, or 7.")

        clear_console()

if __name__ == "__main__":
    main()
