# pdf_text_extractor.py
import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        num_pages = pdf_reader.numPages

        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text += page.extract_text()

    return text
