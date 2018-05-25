import csv


CSV_FILE = 'csv.csv'
NEW_CSV_FILE = 'csv_new.csv'


def extract_city(titel):
    
    city=titel.split(',')[-1]
    return city


def new_csv():
    """
    Create new csv-file with aditional columns. 
    """
    with open (CSV_FILE , 'r') as f:
        with open (NEW_CSV_FILE , 'w') as f_new:
            csv_data = csv.DictReader(f)

            #extract and expand fieldnames

            fieldnames = csv_data.fieldnames
            fieldnames.append('Stadt')

            #crate a new csv_file
            new_csv = csv.DictWriter(f_new, fieldnames=fieldnames)
            new_csv.writeheader()

            # exctract and append citys and write the new row
            for i in csv_data:
                i['Stadt'] = extract_city(i['Aktentitel'])
                new_csv.writerow(i)

if __name__ == '__main__':
    new_csv()