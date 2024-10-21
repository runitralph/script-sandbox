import hl7

def parse_hl7_message(file_path):
    try:
        with open(file_path, 'r') as file:
            hl7_message = file.read().strip()
            
        # Split the message into segments
        segments = hl7_message.split('\n')
        
        for segment in segments:
            fields = segment.split('|')
            segment_name = fields[0]
            print(f"Segment: {segment_name}")
            
            # Enumerate fields starting from 1
            for index, field in enumerate(fields[1:], start=1):
                print(f"  Field {index}: {field}")
                
            print()  # Add a newline for better readability between segments
            
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with the path to your HL7 file
parse_hl7_message('hl7.txt')