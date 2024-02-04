# Fase de resolución de dependencias
FROM python:3.9-slim as dependencies

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Fase de ejecución
FROM dependencies as runtime

COPY . .

CMD ["python", "app.py"]

