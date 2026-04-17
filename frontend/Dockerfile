FROM node:18-alpine AS deps
WORKDIR /app
COPY package*.json ./
RUN npm install

FROM deps AS release
COPY . .
RUN npm run build
CMD ["npm", "start"]
