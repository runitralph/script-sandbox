import hl7

def parse_hl7_message(message):
    """Parse an HL7 message and print its segments and fields clearly."""
    parsed_message = hl7.parse(message)
    
    for segment in parsed_message:
        segment_name = segment[0]
        print(f"Segment: {segment_name}")
        for i, field in enumerate(segment[1:], start=1):
            print(f"  Field {i}: {field}")

def main():
    # Prompt user for HL7 message input
    hl7_message = input("Paste the HL7 message: ")
    parse_hl7_message(hl7_message)

if __name__ == "__main__":
    main()