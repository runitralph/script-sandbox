import csv

input_file = 'sites_input.csv'
output_file = 'sites_output.csv'

data = {}
with open(input_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        key = row[0]
        value = row[1]
        if key in data:
            data[key].append(value)
        else:
            data[key] = [value]

with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for key, value in data.items():
        csvwriter.writerow([key, ';'.join(value)])
