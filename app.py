from utils import load_csv, extract_text_from_pdf

#load CSV
csv_file = "D:/Coding/ML/CVWizard/resumes/Resume/Resume.csv"
data  = load_csv(csv_file)

#load PDF
pdf_path = "D:/Coding/ML/CVWizard/resumes/data/data/INFORMATION-TECHNOLOGY/10089434.pdf"
print(extract_text_from_pdf(pdf_path))

