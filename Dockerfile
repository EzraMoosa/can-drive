FROM pypy:latest
WORKDIR /app
COPY . /app
CMD python method_override.py
