
import csv 

def write_csv(data):
    '''
    This function appends all our data to csv file
    '''

    with open('google_search_data.csv', 'a', newline = '', encoding='utf-8') as file:
        write_file = csv.writer(file)
        write_file.writerow(data)





