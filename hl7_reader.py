import hl7

def parse_hl7_message(message):
    """Parse an HL7 message and print its segments and fields clearly."""
    parsed_message = hl7.parse(message)
    
    for segment in parsed_message:
        segment_name = segment[0]
        print(f"\nSegment: {segment_name}")
        print("=" * (len(segment_name) + 9))
        for i, field in enumerate(segment[1:], start=1):
            print(f"  Field {i}: {field}")

# Read HL7 message from hl7.txt file
with open('hl7.txt', 'r') as file:
    hl7_message = file.read()

parse_hl7_message(hl7_message)