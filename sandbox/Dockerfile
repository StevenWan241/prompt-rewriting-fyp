FROM python:3.12-slim
RUN pip install --no-cache-dir pytest
RUN useradd -m runner
USER runner
WORKDIR /work