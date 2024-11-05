import tkinter as tk
from tkinter import scrolledtext

def convert_tsv_to_csv():
    # Get the input TSV data from the text widget
    tsv_data = tsv_input.get("1.0", tk.END).strip()
    
    # Split the input into lines and then process each line
    csv_data = []
    for line in tsv_data.splitlines():
        # Split by tab and join by semicolon, preserving semicolons in the data
        csv_line = ";".join(line.split("\t"))
        csv_data.append(csv_line)
    
    # Set the output CSV data in the output text widget
    csv_output.delete("1.0", tk.END)
    csv_output.insert(tk.END, "\n".join(csv_data))

# Create the main window
root = tk.Tk()
root.title("Raphael's TSV to CSV Converter")
root.geometry("600x400")

# Create a label for the input area
input_label = tk.Label(root, text="Paste TSV data below:")
input_label.pack(pady=5)

# Create a scrolled text widget for TSV input
tsv_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=10)
tsv_input.pack(pady=5)

# Create a button to trigger the conversion
convert_button = tk.Button(root, text="Convert", command=convert_tsv_to_csv)
convert_button.pack(pady=10)

# Create a label for the output area
output_label = tk.Label(root, text="Converted CSV data:")
output_label.pack(pady=5)

# Create a scrolled text widget for CSV output
csv_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=10)
csv_output.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()