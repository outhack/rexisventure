# Use a lightweight Python image
FROM python:3.12-slim

# Set environment vars
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Work directory inside the container
WORKDIR /app

# Install system packages if needed (e.g. for psycopg2)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirement file and install deps
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code
COPY . /app/

# Set Django env vars (override in Cloud Run with real secrets)
ENV DJANGO_SETTINGS_MODULE="rexisventure_site.settings"

# Collect static files at build time
RUN python manage.py collectstatic --noinput

# Expose port 8080 for Cloud Run
EXPOSE 8080

# Use gunicorn as WSGI server
CMD ["gunicorn", "rexisventure_site.wsgi:application", "--bind", "0.0.0.0:8080"]
