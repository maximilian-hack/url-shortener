# add a reverse proxy that will route requests to the appropriate service
FROM nginx

# Copy the nginx.conf file to the container
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]