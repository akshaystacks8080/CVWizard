import pandas as pd
import os
from PyPDF2 import PdfReader

def load_csv(csv_path):
    data = pd.read_csv(csv_path)
    #print(data.head())
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
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return None

def merge_csv_and_pdfs(data, base_folder):
    pdf_data = []
    for category in os.listdir(base_folder):
        category_folder = os.path.join(base_folder, category)
        if os.path.isdir(category_folder):
            for pdf_file in os.listdir(category_folder):
                pdf_path = os.path.join(category_folder, pdf_file)
                text = extract_text_from_pdf(pdf_path)
                pdf_data.append({"ID": pdf_file.split(".")[0], "Category": category, "Text": text})
    pdf_df = pd.DataFrame(pdf_data)
    
    data['ID'] = data['ID'].astype(str)
    pdf_df['ID'] = pdf_df['ID'].astype(str)
    
    return pd.merge(data, pdf_df, on=["ID", "Category"], how="inner")
