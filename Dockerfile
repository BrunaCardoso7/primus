FROM python:3.13

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

RUN chmod +x /app/entrypoint.sh

RUN useradd -m -r appuser && \
    chown -R appuser:appuser /app

USER appuser
CMD ["/app/entrypoint.sh"]