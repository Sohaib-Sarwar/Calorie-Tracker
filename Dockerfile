<<<<<<< HEAD
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=calorie_tracker.settings

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python calorie_tracker/manage.py collectstatic --noinput

# Run migrations
RUN python calorie_tracker/manage.py makemigrations tracker
RUN python calorie_tracker/manage.py migrate

# Expose port
EXPOSE 8000

# Start server
CMD ["python", "calorie_tracker/manage.py", "runserver", "0.0.0.0:8000"]
=======
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=calorie_tracker.settings

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python calorie_tracker/manage.py collectstatic --noinput

# Run migrations
RUN python calorie_tracker/manage.py makemigrations tracker
RUN python calorie_tracker/manage.py migrate

# Expose port
EXPOSE 8000

# Start server
CMD ["python", "calorie_tracker/manage.py", "runserver", "0.0.0.0:8000"]
>>>>>>> 8127e94 (Initial commit with Docker support)
