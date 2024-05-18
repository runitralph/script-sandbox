import csv

with open('input.csv', 'r') as infile, open('output.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        writer.writerow(row)
        # Writing 2 rows - repeat code as necessary depending on how many empty rows are needed
        writer.writerow([])
        writer.writerow([])

