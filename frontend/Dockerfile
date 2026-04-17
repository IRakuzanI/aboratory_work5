FROM node:18-alpine

RUN apk update && rm -rf /var/cache/apk/*

RUN addgroup -S appgroup && adduser -S student -G appgroup
WORKDIR /app

COPY package*.json ./
RUN chown -R student:appgroup /app
USER student

RUN npm install
COPY --chown=student:appgroup . .

CMD ["npm", "start"]