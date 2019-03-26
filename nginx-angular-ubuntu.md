## Install and Configure Nginx for Angular

- First update the apt-get package lists and then install Nginx using apt-get:
```
sudo apt-get update
sudo apt-get install nginx
```

- Then open the default file to configure server which is located in /etc/nginx/sites-available/ directory.
```
sudo vi /etc/nginx/sites-available/default
```

- Delete everything in this configuration file and paste the following content:
```
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files $uri $uri/ /index.html =404;
    }
} 
```

- To make the changes active, restart the web server nginx:
```
sudo systemctl restart nginx
```
- Now check the status of Nginx service by running following command, you should get “active” green color text along with other text.
```
sudo systemctl status nginx
```
 
