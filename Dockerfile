FROM python:3.9-alpine

WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files
COPY app /app

# Expose port and run FastAPI with Uvicorn
EXPOSE 80
CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "80"]
