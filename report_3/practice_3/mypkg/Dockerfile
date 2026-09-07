FROM python:3.13-slim
RUN pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ mypkg-25030021039
CMD ["python", "-c", "from mypkg import hello; print(hello('from Docker'))"]
