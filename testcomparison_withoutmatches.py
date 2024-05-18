import csv

def compare_csv_files(file1_path, file2_path, output_file_path, num_columns):
    # Read the contents of both CSV files
    with open(file1_path, 'r') as t1, open(file2_path, 'r') as t2:
        fileone = t1.readlines()
        filetwo = t2.readlines()

    # Create a new CSV file for the comparison results
    with open(output_file_path, 'w', newline='') as outFile:
        writer = csv.writer(outFile)

        # Write the header row (assuming the first row contains column names)
        header = ["Column" + str(i) for i in range(1, num_columns + 1)] + ["Comparison Result"]
        writer.writerow(header)

        # Create a dictionary to store rows from fileone
        fileone_dict = {}
        for line in fileone:
            row = line.strip().split(',')
            fileone_dict[row[0]] = row[1:]

        # Compare rows from filetwo with fileone
        for line in filetwo:
            row2 = line.strip().split(',')
            if row2[0] in fileone_dict:
                row1 = fileone_dict[row2[0]]
                if row1 != row2[1:]:
                    # Column values don't match
                    writer.writerow(row2 + ["discrepancy: " + ", ".join(f"Column{i} ({val1}) != {val2}" for i, (val1, val2) in enumerate(zip(row1, row2[1:]), start=1) if val1 != val2)])
            else:
                # Row is missing in fileone
                writer.writerow(row2 + ["missing in file1"])

        # Check for rows missing in filetwo
        for line in fileone:
            row1 = line.strip().split(',')
            if row1[0] not in fileone_dict:
                # Row is missing in filetwo
                writer.writerow(row1 + ["missing in file2"])

# Example usage
compare_csv_files('file1.csv', 'file2.csv', 'file_comparison.csv', num_columns=3)
print("Comparison results written to 'file_comparison.csv'")


#Issue with code: currently not comparing less/more than 3 columns.