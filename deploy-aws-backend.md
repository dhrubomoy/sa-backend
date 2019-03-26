# Deploy sa-backend in AWS (EC2):

### If you are setting up for the first time:
1. Create a EC2 instance (Ubuntu machine with 8gb ram). Follow [this link](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html).
2. [Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html) to the EC2 instance. 
    - Sign in to aws
    - Go to Services > EC2 > Running Instances
    - Select the instance, then click 'Connect'
    - Then follow the instruction to connect to the machine (for linux ssh into the ubuntu machine)
      

3. clone repo and cd into folder

4. Update 
```
sudo apt-get update
```
5. Install pip
```
sudo apt install python3-pip
```

6. Install virtualenv
```
sudo apt install virtualenv
```

7. Create a virtual environment in Python 3 with the environment name of env:
```
virtualenv -p python3 env
```

8. Activate env
```
source env/bin/activate
```

9. Install packages 
```
pip3 install -r requirements.txt
```

10. Create a folder called `models` inside `src/files/`. Then download all the .hdf5 files (mlsa-project/models) and save them inside the `src/files/models/` folder that you created.
```
wget "https://www.dropbox.com/s/wirgt7epmi9y8p9/rnn-glove-model-01-0.8362.hdf5?dl=1" -O rnn-glove-model-01-0.8362.hdf5
```
```
wget "https://www.dropbox.com/s/yfncjn5ybx4b7i2/rnn-word2vec-model-03-0.8425.hdf5?dl=1" -O rnn-word2vec-model-03-0.8425.hdf5
``` 

11. Download the necessary NLTK data
```
python3 -m textblob.download_corpora
```

12. Go inside `src` folder (`cd src`) and run migrations
```
python manage.py migrate
```

13. Run server
```
python3 manage.py runserver 0.0.0.0:8000
```

Open browser and visit http://[PUBLIC_DNS]:8000/api/searched_tweets/ (e.g. http://ec2-3-17-181-123.us-east-2.compute.amazonaws.com:8000/api/searched_tweets/). You should be able to see the web page.

### If you have the instance set up:
If you've already set up the machine, everytime you stop and restart the instance, you must run **Step 8** and **Step 13** to start the backend.

### Next:
Deploy and start the server for frontend. Follow [these instructions](https://github.com/dhrubomoy/sa-backend/blob/master/deploy-aws-frontend.md)
