# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.12-alpine
WORKDIR /app
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY . .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt
CMD ["flask", "run"]
