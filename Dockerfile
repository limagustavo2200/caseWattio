# Dockerfile para projeto FastAPI com Poetry
FROM python:3.12-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Instala Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos do projeto
COPY pyproject.toml poetry.lock* ./

# Instala dependências do projeto
RUN poetry install --no-root --only main

# Copia o restante do código
COPY src/ ./src/

# Define o PYTHONPATH para o src
ENV PYTHONPATH=/app/src

# Expõe a porta padrão do FastAPI
EXPOSE 8000

# Comando para rodar o servidor
CMD ["poetry", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
