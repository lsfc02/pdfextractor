FROM python:3.10-slim

# Instala dependências do sistema (inclui Tesseract)
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Cria diretório de trabalho
WORKDIR /app

# Copia arquivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expõe porta
EXPOSE 8089

# Comando para rodar API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8089"]
