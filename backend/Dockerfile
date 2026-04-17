FROM python:3.10-alpine

RUN apk update && \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    rm -rf /var/cache/apk/*

RUN addgroup -S appgroup && adduser -S student -G appgroup
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    apk --purge del .build-deps

COPY . .
RUN chown -R student:appgroup /app

USER student

CMD ["python", "app.py"]