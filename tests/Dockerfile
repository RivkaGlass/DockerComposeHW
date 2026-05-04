FROM python:3.10-slim
WORKDIR /tests
COPY . .
ENV PYTHONPATH=/app
RUN pip install pytest
CMD ["pytest", "test_app.py"]