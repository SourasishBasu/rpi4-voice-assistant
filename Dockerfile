FROM python:3.12.6-slim

WORKDIR /app

RUN apt-get update && apt-get install curl -y \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

RUN addgroup --gid 1001 --system app && \
    adduser --no-create-home --shell /bin/false --disabled-password --uid 1001 --system --group app && \
    chown -R app:app /app

USER app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV GEMINI_API_KEY=${GEMINI_API_KEY}

COPY --chown=app:app . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]