# Imagem base: Python 3.12 em versão "slim" (menor)
FROM python:3.12-slim

# Mostra os logs do Python na hora, sem esperar o buffer encher
ENV PYTHONUNBUFFERED=1

# Pasta de trabalho dentro do contêiner
WORKDIR /app

# Instala as dependências primeiro (aproveita o cache do Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY app.py .

# Documenta a porta em que a aplicação escuta
EXPOSE 8000

# Comando executado quando o contêiner inicia
CMD ["python", "app.py"]