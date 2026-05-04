FROM python:3.10-slim
WORKDIR /tests
COPY . .
RUN pip install pytest
CMD ["pytest", "test_app.py"]