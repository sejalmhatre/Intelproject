import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    try:
        document = fitz.open(pdf_path)
        text = ""
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            text += page.get_text()
        return text
    except Exception as e:
        return str(e)

# Path to your PDF file
pdf_path = "sample_contract.pdf"  # Replace with the correct path to your PDF

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Output the extracted text to a file
output_path = "extracted_text.txt"
with open(output_path, "w", encoding="utf-8") as output_file:
    output_file.write(pdf_text)

print(f"Text extracted from {pdf_path} and saved to {output_path}.")
