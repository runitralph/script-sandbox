import os
import csv
import requests
import mysql.connector

# Function to use PDB IDs to fetch FASTA sequences
def fetch_fasta(pdb_id):
    url = f'https://www.rcsb.org/fasta/entry/{pdb_id}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch data for PDB ID {pdb_id}")
        return None

# Function to parse FASTA sequences
def parse_fasta(fasta_text):
    sequences = []
    sequence = ''
    name = ''
    description = ''
    for line in fasta_text.split('\n'):
        if line.startswith('>'):
            if sequence:
                sequences.append((name, sequence, description))
            header = line[1:].strip().split(None, 1)
            name = header[0]
            description = header[1] if len(header) > 1 else ''
            sequence = ''
        else:
            sequence += line.strip()
    if sequence:
        sequences.append((name, sequence, description))
    return sequences

# Function to insert protein sequences into MySQL database
def insert_proteins(sequences):
    conn = mysql.connector.connect(
        host="host_name",
        user="uname_here",
        password="pass_here",
        database="protein_db"
    )
    cur = conn.cursor()
    for name, sequence, description in sequences:
        cur.execute(
            "INSERT INTO proteins (name, sequence, description) VALUES (%s, %s, %s)",
            (name, sequence, description)
        )
    conn.commit()
    cur.close()
    conn.close()

# Function to fetch, parse, and insert sequences for a list of PDB IDs
def main(pdb_ids):
    all_sequences = []
    for pdb_id in pdb_ids:
        fasta_text = fetch_fasta(pdb_id)
        if fasta_text:
            sequences = parse_fasta(fasta_text)
            all_sequences.extend(sequences)
    insert_proteins(all_sequences)

# Analysis Script: Retrieve and analyze protein sequences from MySQL database
def get_proteins():
    conn = mysql.connector.connect(
        host="host_name",
        user="uname_here",
        password="pass_here",
        database="protein_db"
    )
    cur = conn.cursor()
    cur.execute("SELECT id, name, sequence FROM proteins")
    proteins = cur.fetchall()
    cur.close()
    conn.close()
    return proteins

def calculate_molecular_weight(sequence):
    weights = {'A': 89.1, 'C': 121.2, 'D': 133.1, 'E': 147.1, 'F': 165.2,
               'G': 75.1, 'H': 155.2, 'I': 131.2, 'K': 146.2, 'L': 131.2,
               'M': 149.2, 'N': 132.1, 'P': 115.1, 'Q': 146.2, 'R': 174.2,
               'S': 105.1, 'T': 119.1, 'V': 117.1, 'W': 204.2, 'Y': 181.2}
    molecular_weight = 0
    for aa in sequence:
        if aa in weights:
            molecular_weight += weights[aa]
        else:
            print(f"Ignoring unknown amino acid: {aa}")
    return molecular_weight

def analyse_proteins():
    proteins = get_proteins()
    with open('protein_analysis.csv', 'w', newline='') as csvfile:
        fieldnames = ['Protein ID', 'Name', 'Molecular Weight']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for prot_id, name, sequence in proteins:
            weight = calculate_molecular_weight(sequence)
            writer.writerow({'Protein ID': prot_id, 'Name': name, 'Molecular Weight': weight})

# Function to generate list of PDB IDs from CSV files in the current directory
def read_pdb_ids_from_csv():
    pdb_ids = []
    for file_name in os.listdir():
        if file_name.endswith('.csv'):
            with open(file_name, newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header row
                for row in reader:
                    pdb_ids.append(row[0])  # Assuming PDB ID is in the first column
    return pdb_ids

if __name__ == "__main__":
    # Read PDB IDs from CSV files in the current directory
    pdb_ids = read_pdb_ids_from_csv()
    if pdb_ids:
        main(pdb_ids)
        analyse_proteins()
    else:
        print("No PDB IDs found in the CSV files.")
