import csv

CSV_FILE = 'csv.csv'
NEW_CSV_FILE = 'csv_new.csv'
COMPANY_TYPES = [
'Musikalienbuchhandlung',
'Verlagsbuchhandlung',
'Buchhandlung',
'Verlag',
'Antiquariat',
'Verlagsbuchhandlung'
]


def extract_city(titel):
    
    city=titel.split(',')[-1].strip()
    return city

def company_type(description):
    """
    Detect the kind of company
    """
    type = []
    import pdb;pdb.set_trace

    type = [i for i in COMPANY_TYPES if i in description]

    if not type:
        type.append('nicht erkannt')
    
    return type


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
            fieldnames.append('Firmentyp')

            #crate a new csv_file with new columns
            new_csv = csv.DictWriter(f_new, fieldnames=fieldnames)
            new_csv.writeheader()

            # write new  rows
            for i in csv_data:
                i['Stadt'] = extract_city(i['Aktentitel'])
                i['Firmentyp'] = company_type(i['Aktentitel'])

                new_csv.writerow(i)



if __name__ == '__main__':
    new_csv()