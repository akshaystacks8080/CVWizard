import pandas as pd
from PyPDF2 import PdfReader

def load_csv(csv_path):
    data = pd.read_csv(csv_path)
    print(data.head())
    return data

def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text.strip()
    
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return None

