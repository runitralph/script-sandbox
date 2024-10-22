import tkinter as tk
from tkinter import scrolledtext, messagebox

# HL7 segment dictionary - I used a subset of commonly occuring HL7 message fragments, and will add more depending on how frequently I use them

hl7_segments = {
    'MSH': 'Message Header',
    'EVN': 'Event Type',
    'PID': 'Patient Identification',
    'PD1': 'Patient Additional Demographic',
    'NK1': 'Next of Kin / Associated Parties',
    'PV1': 'Patient Visit',
    'PV2': 'Patient Visit - Additional Information',
    'OBR': 'Observation Request',
    'OBX': 'Observation/Result',
    'ORC': 'Common Order',
    'AL1': 'Allergy Information',
    'DG1': 'Diagnosis',
    'PR1': 'Procedures',
    'GT1': 'Guarantor Information',
    'IN1': 'Insurance Information',
    'IN2': 'Insurance Additional Information',
    'IN3': 'Insurance Additional Information, Certification',
    'ROL': 'Role',
}

# I used AI tools to customise my requirements for the HL7 parser
  
def parse_hl7_message(hl7_message):
    try:
        # Split the message into segments
        segments = hl7_message.strip().split('\n')
        
        output = []
        for segment in segments:
            fields = segment.split('|')
            segment_name = fields[0]
            segment_description = hl7_segments.get(segment_name, "Unknown Segment")
            output.append(f"Segment: {segment_name} ({segment_description})")
            
            # Enumerate fields starting from 1 for each segment
            for index, field in enumerate(fields[1:], start=1):
                output.append(f"  Field {index}: {field}")
                
            output.append("")  # Add a newline for better readability between segments
        
        return "\n".join(output)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to parse HL7 message: {e}")
        return ""

def on_parse():
    hl7_message = text_input.get("1.0", tk.END).strip()
    if not hl7_message:
        messagebox.showwarning("Input Error", "Please enter an HL7 message.")
        return
    
    parsed_output = parse_hl7_message(hl7_message)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, parsed_output)

# I used Tkinter to create and customise the GUI for the application

# Main application window
root = tk.Tk()
root.title("Raphael's HL7 Reader")

# Text area for input
text_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=16)
text_input.grid(column=0, row=0, padx=10, pady=10)

# Button for parsing
parse_button = tk.Button(root, text="Parse HL7 Message", command=on_parse)
parse_button.grid(column=0, row=1, padx=10, pady=10)

# Text area for output
text_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=32)
text_output.grid(column=0, row=2, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
