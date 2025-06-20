# PDF Word Search Tool 📄🔍

A **Python-based PDF word search tool** that allows you to:
- Select a PDF file using a file manager pop-up.
- Automatically extract the entire content of the PDF into a `output.txt` file.
- Search for any word inside the selected PDF and find the exact line number where it exists.

---

## 🚀 Project Objective
The main goal of this project is to build a tool that:
- Makes it easy to read PDF files using Python.
- Allows users to **interactively select files via GUI pop-up**.
- Searches for specific words within the PDF and displays their **line positions**.
- Stores the full content of the PDF in a separate text file for easy reference.

---

## 🛠️ Key Features
- 📂 **PDF File Selection:** Choose the PDF file using a file manager window.
- 📄 **PDF Content Extraction:** Extracts the entire PDF content and saves it in an `output.txt` file.
- 🔍 **Word Search:** Search for any word and find the exact line number where the word appears.
- ❌ **Word Not Found Handling:** Displays a friendly message if the word is not found.

---

## 💻 Technologies Used
- Python
- `tkinter` (for file selection pop-up)
- `PyPDF2` (for PDF reading and text extraction)
- OS module (for path handling)

---

## 📂 How to Run
1. Make sure you have Python installed on your system.
2. Install the required library:
   ```bash
   pip install PyPDF2
   ```
   
3. Run the Python file:
   ```bash
    python main.py
   ```

4. Select a PDF file from the file manager pop-up.

5. The PDF content will be automatically saved in output.txt.

6. Enter the word you want to search in the terminal.

7. The program will display the line number(s) where the word is found, or will show Word not found if the word does not exist.

## 🤝 Contribution

Feel free to fork this project and contribute improvements or new features. 🚀

## 🗒️ Note
Make sure the PDF file is text-based (not scanned images), otherwise the text extraction might not work properly.
