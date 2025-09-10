from fastapi import FastAPI, UploadFile
from utils.extractor import extract_text_from_pdf
from utils.llm import structure_text_with_ai

app = FastAPI()

@app.post("/extract-pdf")
async def extract_pdf(file: UploadFile):
    pdf_bytes = await file.read()
    raw_text = extract_text_from_pdf(pdf_bytes)
    result = structure_text_with_ai(raw_text)
    return result
