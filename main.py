from catalog import extract_keys
from crossmap import filter_cm
from gen_crossmap import load_crossmap_data, allocate_crossmap_indices, write_crossmap_header
from gen_native import load_natives_data, write_natives_header

def main():
    print("Choice option")
    print("1. Filter netCatalog.json")
    print("2. Filter crossmap.txt")
    print("3. Generate crossmap.txt")
    print("4. Generate native.txt")

    choice = input("Enter your choice (1, 2, 3 or 4) : ")

    if choice == '1':
        input_file = 'net_catalog/netCatalog.json'
        output_file = 'net_catalog/filtered_keys.txt'
        prefixes = ['SERVICE_EARN', 'SERVICE_SPEND']
        extract_keys(input_file, output_file, prefixes)

    elif choice == '2':
        input_filename = "crossmap/crossmap.txt"
        end_input = "crossmap/new_cm.txt"
        filter_cm(input_filename, end_input)

    elif choice == '3':
        load_crossmap_data()
        allocate_crossmap_indices()
        write_crossmap_header()

    elif choice == '4':
        load_natives_data()
        write_natives_header()

    else:
        print("Choice invalid. Enter 1, 2, 3 or 4.")

if __name__ == "__main__":
    main()
