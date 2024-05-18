import csv

input_file = 'input.csv'
output_file = 'outpout.csv'

input_data = []
with open(input_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        input_data.append(row)

output_data = []

for row in input_data:
    key = row[0]
    values = [val for val in row[1:] if val != '']
    for value in values:
        output_data.append([key, value])

# Sorting output data by the first column
output_data.sort(key=lambda x: x[0])

# Writing output data to sortedtests.csv
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_data)