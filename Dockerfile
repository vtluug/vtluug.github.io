FROM nginx:alpine

RUN apk add --no-cache git busybox

# shithack. i'm lazy. ~rsk
RUN rm -rf /usr/share/nginx/html/*
RUN git clone https://github.com/vtluug/vtluug.github.io /usr/share/nginx/html
RUN git config --global --add safe.directory /usr/share/nginx/html
RUN chown -R nginx:nginx /usr/share/nginx/html

# gh doesn't ratelimit
RUN echo "* * * * * git -C /usr/share/nginx/html pull origin master >> /var/log/pull 2>&1" >> /etc/crontabs/root

EXPOSE 80
CMD ["sh", "-c", "crond -b -L /var/log/cron && nginx -g 'daemon off;'"]