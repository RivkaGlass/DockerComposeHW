FROM python:3.10-slim
WORKDIR /tests
COPY . .
ENV PYTHONPATH=/app
RUN pip install pytest --trusted-host pypi.org --trusted-host files.pythonhosted.org
CMD ["pytest", "test_app.py"]