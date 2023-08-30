# import requests
# import io
# import tempfile
# from pdf2docx import Converter

# import boto3

# # URL of the PDF file
from pdf2docx import parse
pdf_file = "main.pdf"
word_file = "test.docx"
parse(pdf_file, word_file, start=0, end=None)



