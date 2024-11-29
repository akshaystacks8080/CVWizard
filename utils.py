import pandas as pd
import re, os, nltk
from PyPDF2 import PdfReader
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

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

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    return " ".join(tokens)