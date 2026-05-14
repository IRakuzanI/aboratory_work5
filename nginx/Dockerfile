FROM alpine:latest

RUN apk update && \
    apk add --no-cache nginx && \
    rm -rf /var/cache/apk/*

RUN mkdir -p /var/cache/nginx /var/run/nginx /var/log/nginx && \
    chown -R nginx:nginx /var/cache/nginx /var/run/nginx /var/log/nginx /etc/nginx

USER nginx

CMD ["nginx", "-g", "daemon off;"]

