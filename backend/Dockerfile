FROM python:3.10-alpine AS deps

WORKDIR /app
COPY requirements.txt .
RUN apk update && \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk --purge del .build-deps

FROM deps AS release

COPY . .

CMD ["python", "app.py"]



