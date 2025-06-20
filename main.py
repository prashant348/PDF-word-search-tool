

import os
import PyPDF2 as p                                                                                                                                                            
import tkinter as tk
from tkinter import filedialog  

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
window = tk.Tk()                                                                                                                                                                                                                                                                       
window.withdraw()
pdf_path = filedialog.askopenfilename(title="Select PDF file", filetypes=[("PDF files", "*.pdf")])
print(f"Selected PDF file: {pdf_path}")
                  
# PyPDF2 library method that reads the pdf: 
# input_file_name = input("Enter the name of the PDF file (with .pdf extension): ")
# input_file_path = f"C:\\Users\\pc\\Downloads\\Note_Taking_app\\{input_file_name}"

input_file = open(pdf_path, 'rb')
pdf_reader = p.PdfReader(input_file)
pdf_text = ""

for page in pdf_reader.pages:
    pdf_text += f"{page.extract_text()}"
pdf_content_storage = pdf_text.splitlines()

output_file_path = os.path.join(os.path.dirname(__file__), "output.txt")

with open(output_file_path, "w", encoding="utf-8") as f:
    f.write(pdf_text)

input_file.close()

# with open("C:\\Users\\pc\\Downloads\\PYTHON_PROJECTS\\output.txt", "w", encoding="utf-8") as f:
#     f.write(pdf_text)

# input_file.close()
# # word search

input_word = input("Enter the word you want to search for: ")

# with open("C:\\Users\\pc\\Downloads\\PYTHON_PROJECTS\\output.txt", "r", encoding="utf-8") as f:
#     content_pdf_text = f.readlines()

found = False

line_num = 1
for line in pdf_content_storage:
    if input_word in line:
        print(f"word '{input_word}' found in line {line_num}")
        found = True
    line_num += 1

if not found:
    print(f"Word {input_word} not found")  