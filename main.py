import os
import csv
from src.some_storage_library import SomeStorageLibrary 

def parse_columns(file_path):
    columns= []

    with open(file_path, 'r') as f:
        for line in f:
            index, name = line.strip().split('|')
            columns.append((int(index), name))

    return sorted(columns)


def parse_data(file_path):
    with open(file_path, 'r') as f:

        return [line.strip().split('|') for line in f]

def write_csv(data, columns, output_file):

    ordered_columns =[name for _, name in columns]
    
    # Ensure the destination directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(ordered_columns)
        for row in data:
            ordered_row = [row[i-1] for i, _ in columns]
            writer.writerow(ordered_row)


    print("Writing Completed!")



def main():

    columns = parse_columns('data/source/SOURCECOLUMNS.txt')

    data = parse_data('data/source/SOURCEDATA.TXT')
    write_csv(data, columns, 'data/destination/output.csv')

    # Loading the CSV file into storage
    storage = SomeStorageLibrary()  # Now the class is recognized here

    storage.load_csv('data/destination/output.csv')


if __name__ == '__main__':
    main()