import pdfplumber
import pytesseract
from PIL import Image
import io
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    text = ""
    try:
        # Primeiro tenta extrair como texto (PDF pesquisável)
        reader = PdfReader(io.BytesIO(pdf_bytes))
        for page in reader.pages:
            text += page.extract_text() or ""
    except:
        pass

    # Se não extraiu nada, tenta OCR
    if not text.strip():
        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            for page in pdf.pages:
                pil_image = page.to_image(resolution=300).original
                text += pytesseract.image_to_string(pil_image, lang="por") + "\n"

    return text
