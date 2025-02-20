import os
import time
import pyfiglet
from colorama import Fore, Style, init

init(autoreset=True)

from catalog import extract_keys
from crossmap import filter_cm
from gen_crossmap import load_crossmap_data, allocate_crossmap_indices, write_crossmap_header
from gen_native import load_natives_data, write_natives_header

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
        print(Fore.BLUE + "2. Filter crossmap.txt")
        print(Fore.BLUE + "3. Generate crossmap.txt")
        print(Fore.BLUE + "4. Generate native.txt")
        print(Fore.RED + "5. Quit")

        choice = input(Fore.WHITE + "Enter your choice: ")

        if choice == '1':
            input_file = 'net_catalog/netCatalog.json'
            output_file = 'net_catalog/filtered_keys.txt'
            prefixes = ['SERVICE_EARN', 'SERVICE_SPEND']
            extract_keys(input_file, output_file, prefixes)
            print(Fore.GREEN + "netCatalog.json filtered successfully!")

        elif choice == '2':
            input_filename = "crossmap/crossmap.txt"
            end_input = "crossmap/new_cm.txt"
            filter_cm(input_filename, end_input)
            print(Fore.GREEN + "crossmap.txt filtered successfully!")

        elif choice == '3':
            load_crossmap_data()
            allocate_crossmap_indices()
            write_crossmap_header()
            print(Fore.GREEN + "crossmap.txt generated successfully!")

        elif choice == '4':
            load_natives_data()
            write_natives_header()
            print(Fore.GREEN + "native.txt generated successfully!")

        elif choice == '5':
            print(Fore.RED + "Exiting.")
            break 

        else:
            print(Fore.RED + "Invalid choice. Enter 1, 2, 3, 4, or 5.")

        clear_console()

if __name__ == "__main__":
    main()
