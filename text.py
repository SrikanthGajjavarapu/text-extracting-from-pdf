#importing required libraries
from PyPDF2 import PdfReader

#specifying the pdf file path
pdf = 'wordpress-pdf-invoice-plugin-sample.pdf'  

#specifying the text file path for saving extracted text 
text = 'text.txt' 

# Createing a PDF reader object
pdf_reader = PdfReader(pdf)

# giving empty string for storing extracted text data
extracted_text = ''

# Iterating through each page of the PDF file
for page in pdf_reader.pages:
    # Getting the text content of the pages
    page_text = page.extract_text()

    # Appending the page's text to the extracted_text variable
    extracted_text += page_text

# Writeing the extracted text to the output text file
with open(text, 'w', encoding='utf-8') as text_file:
    text_file.write(extracted_text)

print(f'Text extracted and saved to {text}')
