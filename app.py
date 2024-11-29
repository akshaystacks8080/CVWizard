from utils import load_csv, extract_text_from_pdf, merge_csv_and_pdfs, clean_text

#load CSV
csv_file = "D:/Coding/ML/CVWizard/resumes/Resume/Resume.csv"
data  = load_csv(csv_file)

#load PDF
pdf_path = "D:/Coding/ML/CVWizard/resumes/data/data/INFORMATION-TECHNOLOGY/10089434.pdf"
#print(extract_text_from_pdf(pdf_path))

base_folder = "D:/Coding/ML/CVWizard/resumes/data/data/"
merged_data = merge_csv_and_pdfs(data, base_folder)
#print(merged_data.head())
#print(merged_data[['ID', 'Category', 'Text']].head())

merged_data['Cleaned_Text'] = merged_data['Text'].apply(clean_text)
print(merged_data[['Cleaned_Text', 'Category']].head())