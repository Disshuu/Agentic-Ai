from PyPDF2 import PdfReader

def load_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text

def load_txt(file):
    return file.read().decode("utf-8")