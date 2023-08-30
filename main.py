import requests
import io
import tempfile
from pdf2docx import Converter

import boto3

# URL of the PDF file
pdf_url = "https://rvs3reports-54654654654.s3.amazonaws.com/pdf/testnowv8.pdf"

# Download the PDF from the URL
response = requests.get(pdf_url)
pdf_bytes = io.BytesIO(response.content)

# Create a temporary file to save the PDF content
with tempfile.NamedTemporaryFile(delete=False) as temp_pdf_file:
    temp_pdf_file.write(pdf_bytes.read())
    temp_pdf_file_path = temp_pdf_file.name

# Convert the PDF to DOCX
output_docx = "outputfrom_pdf.docx"
cv = Converter(temp_pdf_file_path)
cv.convert(output_docx, start=0, end=None)
cv.close()

# Clean up the temporary PDF file
temp_pdf_file.close()

print(f"Converted PDF from {pdf_url} to {output_docx}")