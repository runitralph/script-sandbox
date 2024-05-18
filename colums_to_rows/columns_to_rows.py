import csv

with open("input.csv", "r") as input_file, open("output.csv", "w") as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    for row in reader:
        num_cols = len(row)
        for i in range(1, num_cols):
            if row[i]:  # check if the column is not empty
                writer.writerow([row[0], row[i]])