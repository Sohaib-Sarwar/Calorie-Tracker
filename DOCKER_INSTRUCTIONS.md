# Docker Setup for Calorie Tracker

This document explains how to build and run the Calorie Tracker application using Docker.

## Prerequisites

- Docker installed on your system
- Docker Compose installed on your system (optional but recommended)

## Building and Running with Docker

### Using Docker Compose (Recommended)

1. Build and start the container:
   ```bash
   docker-compose up --build
   ```

2. Access the application at http://localhost:8000

3. To stop the container:
   ```bash
   docker-compose down
   ```

### Using Docker Directly

1. Build the Docker image:
   ```bash
   docker build -t calorie-tracker:latest .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 calorie-tracker:latest
   ```

3. Access the application at http://localhost:8000

## Creating a Superuser in Docker

To create an admin user inside the running container:

```bash
# With Docker Compose
docker-compose exec web python calorie_tracker/manage.py createsuperuser

# With Docker
docker exec -it calorie-tracker python calorie_tracker/manage.py createsuperuser
```

## GitHub Repository

The complete code for this project, including Docker configuration, is available on GitHub:

[https://github.com/yourusername/calorie-tracker](https://github.com/yourusername/calorie-tracker)

## Notes for Production Deployment

For production environments, consider the following modifications:

1. Use environment variables for sensitive settings (SECRET_KEY, etc.)
2. Restrict ALLOWED_HOSTS to your specific domain
3. Set DEBUG=False
4. Use a production-ready database (PostgreSQL or MySQL)
5. Implement proper logging
6. Consider using Gunicorn or uWSGI instead of the Django development server
7. Add Nginx as a reverse proxy
