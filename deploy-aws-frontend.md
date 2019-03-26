# Deploy sa-frontend in AWS (EC2):

sa-frontend in AWS:

1. Make sure back end is setup. 

2. ssh into the ubuntu machine

3. Install nodejs and build-essential
```
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo apt-get install -y build-essential
```

4. clone repo and cd into folder
```
git clone https://github.com/dhrubomoy/sa-frontend
```

5. Install packages
```
npm install
```
6. In `src/app/core/constants.ts` file, change the `SENTIMENT_ANALYSIS_API` const, replace the current api URL with the one where the backend server is currently running. e.g
```
export const SENTIMENT_ANALYSIS_API = "http://ec2-3-17-181-123.us-east-2.compute.amazonaws.com:8000/api/";
```
   - Note: You can use [vim](https://www.howtoforge.com/vim-basics) to edit the file.

7. Follow [this link](https://github.com/dhrubomoy/sa-backend/blob/master/nginx-angular-ubuntu.md) and configure nginx for angular. 

8. Create a bundle in production mode:
```
npm run build:prod
```
9. To move files use
``` 
sudo cp -a dist/. /var/www/html/
```
10. Now open browser and enter the public dns of the AWS EC2 instance (e.g. "http://ec2-3-17-181-123.us-east-2.compute.amazonaws.com"). You should see the app running.

### Everytime you stop and start server:
Everytime you stop and start the EC2 instance, the public DNS changes. So you need to update the the backend url with the new DNS. Which means, you need to go through step 6,8, and 9. 
