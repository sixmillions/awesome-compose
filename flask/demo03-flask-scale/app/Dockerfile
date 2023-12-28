# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.12-alpine
WORKDIR /app
COPY . .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]
