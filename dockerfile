FROM python:3.14

WORKDIR /app

COPY course.py .
CMD ["python", "course.py"]