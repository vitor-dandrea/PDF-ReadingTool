# PDF-ReadingTool

A Python-based tool for extracting text from PDF files, supporting both regular PDFs and scanned PDFs using OCR (Optical Character Recognition). This tool provides a simple terminal menu interface for easy text extraction with progress tracking.

## Description

PDF-ReadingTool is a command-line utility written in Python that allows users to extract text content from PDF documents. It uses `pdfplumber` for direct text extraction from text-based PDFs and integrates `pytesseract` with `PIL` (Pillow) for OCR processing of scanned or image-based PDFs. The extracted text is saved as plain text files in an `extracted_texts` directory within the project folder.

The tool features a user-friendly menu interface, progress bars for long operations, and customizable output file names.

## Features

- **Dual Extraction Methods**: Supports text extraction from regular PDFs and OCR for scanned PDFs.
- **Progress Tracking**: Displays progress bars during page processing using `tqdm`.
- **User-Specified Output**: Allows users to name output text files.
- **Automatic Directory Creation**: Creates an `extracted_texts` folder if it doesn't exist.
- **Error Handling**: Checks for PDF file existence before processing.

## Requirements

- Python 3.6 or higher
- `pdfplumber` library
- `tqdm` library
- `pytesseract` library
- `Pillow` (PIL) library
- Tesseract OCR engine (external dependency)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vitor-dandrea/PDF-ReadingTool.git
   cd PDF-ReadingTool
   ```

2. **Install Python dependencies**:
   ```bash
   pip install pdfplumber tqdm pytesseract pillow
   ```

3. **Install Tesseract OCR**:
   - **Windows**: Download and install from [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki). The default installation path is `C:\Program Files\Tesseract-OCR\tesseract.exe`.

   Note: If Tesseract is installed in a non-default location, update the `pytesseract.pytesseract.tesseract_cmd` path in `converty.py`.

## Usage

Run the script from the command line:

```bash
python converty.py
```

The tool will display a menu with the following options:

1. **Extract text from PDF**: For text-based PDFs (faster, preserves formatting better)
2. **Extract text from scanned PDF (OCR)**: For image-based or scanned PDFs (slower, uses OCR)
3. **Exit**: Quit the application

For options 1 or 2:
- Enter the full path to the PDF file when prompted
- Provide a name for the output text file (without extension)
- The extracted text will be saved in the `extracted_texts` directory

## Examples

### Example 1: Extracting text from a regular PDF
```
PDF Text Extractor Menu
1. Extract text from PDF
2. Extract text from scanned PDF (OCR)
3. Exit
Choose an option: 1
Enter the path to the PDF file: C:\Users\Example\Documents\document.pdf
Enter the name for the output .txt file (without extension): my_document
Reading pages: 100%|███████████████████████████████████████████████████████████████| 10/10 [00:02<00:00, 4.50page/s]

✔ Text saved to: C:\Users\Example\Desktop\PDF-ReadingTool\extracted_texts\my_document.txt
```

### Example 2: Extracting text from a scanned PDF using OCR
```
PDF Text Extractor Menu
1. Extract text from PDF
2. Extract text from scanned PDF (OCR)
3. Exit
Choose an option: 2
Enter the path to the scanned PDF file: C:\Users\Example\Documents\scanned_doc.pdf
Enter the name for the output .txt file (without extension): scanned_text
Processing pages with OCR: 100%|██████████████████████████████████████████████████| 5/5 [00:15<00:00, 3.25page/s]

✔ Text saved to: C:\Users\Example\Desktop\PDF-ReadingTool\extracted_texts\scanned_text.txt
```

## Notes

- **OCR Accuracy**: OCR extraction may not be 100% accurate, especially with poor-quality scans, handwritten text, or complex layouts. Always review the output for errors.
- **Performance**: OCR processing is slower than direct text extraction. Use OCR only when necessary for scanned documents.
- **File Paths**: Use absolute paths for PDF files. Enclose paths with spaces in quotes if necessary.
- **Output Directory**: All extracted text files are saved in the `extracted_texts` subdirectory. This directory is created automatically if it doesn't exist.
- **Tesseract Path**: The script assumes Tesseract is installed at `C:\Program Files\Tesseract-OCR\tesseract.exe` on Windows. Modify this path in the code if your installation differs.
- **Dependencies**: Ensure all Python packages are installed and Tesseract is properly configured before running the script.
