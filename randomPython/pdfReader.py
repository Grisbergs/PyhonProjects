import PyPDF2
import re

def extract_text_from_pdf(pdf_path):
    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        reader = PyPDF2.PdfReader(file)
        
        # Initialize a variable to store the extracted text
        text = ''
        
        # Loop through all pages in the PDF
        for page_num in range(len(reader.pages)):
            # Extract text from each page
            page = reader.pages[page_num]
            text += page.extract_text()
        
        return text

# Example usage
pdf_path = 'C:\C#Class2\Bads\OK00143_WFS_Third_Party_First_Request_Ancillary_1735446847332.pdf'
text = extract_text_from_pdf(pdf_path)
vin_pattern = r'\b[A-HJ-NPR-Z0-9]{17}\b'
vin_pattern2 = r'^[A-HJ-NPR-Za-hj-npr-z\d]{9}[A-HJ-NPR-Za-hj-npr-z\d]{3}\d{5}$'
vin_pattern3 = r'\b[A-HJ-NPR-Za-hj-npr-z\d]{9}[A-HJ-NPR-Za-hj-npr-z\d]{2}'
match = re.search(vin_pattern, text)
match2 = re.search(vin_pattern2, text)
cleaned_string = re.sub(r'\s+', '', text)
match3 = re.search(vin_pattern3, text)
if match:
    print(f"Found VIN: {match.group()}")
else:
    if match2:
        print(f"PT2 Found VIN: {match2.group()}")
    else:
        if match3:
            print(f"PT3 Found VIN: {match3.group()}")
        else:
            print(text)
