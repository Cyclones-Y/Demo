import pdfplumber
import chardet

path = '1.1投标函.pdf'

def get_text(path_file):
    with pdfplumber.open(path_file) as pdf:
        first_page = pdf.pages[0]
        print(first_page.extract_text())

get_text(path)