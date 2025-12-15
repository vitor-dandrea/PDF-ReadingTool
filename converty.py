import pdfplumber
import sys
import os
from tqdm import tqdm
import pytesseract
from PIL import Image
import io

# Set Tesseract path (adjust if installed elsewhere)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(pdf_path, txt_path):
    # Open PDF
    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        extracted = []

        # Progress bar
        with tqdm(total=total_pages, desc="Reading pages", unit="page") as pbar:
            for page in pdf.pages:
                text = page.extract_text() or ""
                extracted.append(text)
                pbar.update(1)

    # Save TXT
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(extracted))

    print(f"\n✔ Text saved to: {txt_path}")


def extract_text_ocr(pdf_path, txt_path):
    # Open PDF
    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        extracted = []

        # Progress bar
        with tqdm(total=total_pages, desc="Processing pages with OCR", unit="page") as pbar:
            for page in pdf.pages:
                # Convert page to image
                page_image = page.to_image(resolution=300).original
                # Perform OCR on the entire page
                text = pytesseract.image_to_string(page_image)
                extracted.append(text)
                pbar.update(1)

    # Save TXT
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(extracted))

    print(f"\n✔ Text saved to: {txt_path}")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "extracted_texts")
    os.makedirs(output_dir, exist_ok=True)

    while True:
        print("\nPDF Text Extractor Menu")
        print("1. Extract text from PDF")
        print("2. Extract text from scanned PDF (OCR)")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            pdf_path = input("Enter the path to the PDF file: ").strip('"')
            if not os.path.exists(pdf_path):
                print("Error: PDF file not found. Please check the path.")
                continue
            txt_name = input("Enter the name for the output .txt file (without extension): ")
            txt_path = os.path.join(output_dir, txt_name + ".txt")
            extract_text(pdf_path, txt_path)
        elif choice == "2":
            pdf_path = input("Enter the path to the scanned PDF file: ").strip('"')
            if not os.path.exists(pdf_path):
                print("Error: PDF file not found. Please check the path.")
                continue
            txt_name = input("Enter the name for the output .txt file (without extension): ")
            txt_path = os.path.join(output_dir, txt_name + ".txt")
            extract_text_ocr(pdf_path, txt_path)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
