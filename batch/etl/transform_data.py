import csv
from etl.transform_data import transform

def save_to_csv(data):

    with open('data.csv', 'w', newline='') as csvfile:
        fieldnames = ['Station Name', 'RON 95', 'RON 97']  # Adjust fieldnames as needed
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        array_length = len(data)

        for i in range(array_length):
            # writer.writerow({
            #   'Station Name': i[data[0]],
            #   'RON 95': i[data[1]],
            #   'RON 97': i[data[2]]
            print(data[i[0]], data[i[1]])

    return data

def transform_csv():


def _init_():
