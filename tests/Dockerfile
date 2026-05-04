FROM python:3.10-slim
WORKDIR /tests
COPY . .
RUN pip install pytest --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org
CMD ["pytest", "test_app.py"]