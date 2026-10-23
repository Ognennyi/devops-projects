FROM debian:stable-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        nginx \
        build-essential \
        libfcgi-dev \
        spawn-fcgi && \
    rm -rf /var/lib/apt/lists/*

COPY server.c /app/server.c
COPY nginx/nginx.conf /etc/nginx/nginx.conf

RUN gcc /app/server.c -o /app/server -lfcgi && \
    chown -R www-data:www-data /app /var/lib/nginx /var/log/nginx

USER www-data

CMD spawn-fcgi -p 8080 /app/server && nginx -g "daemon off;"