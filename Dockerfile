FROM python:3.11-slim

WORKDIR /app

# System deps + Microsoft ODBC Driver (modern Debian way)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        ca-certificates \
        gnupg \
        unixodbc \
        unixodbc-dev \
    && mkdir -p /etc/apt/keyrings \
    && curl -fsSL https://packages.microsoft.com/keys/microsoft.asc \
        | gpg --dearmor -o /etc/apt/keyrings/microsoft.gpg \
    && echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/microsoft.gpg] \
        https://packages.microsoft.com/debian/12/prod bookworm main" \
        > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && rm -rf /var/lib/apt/lists/*

# Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App code
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
