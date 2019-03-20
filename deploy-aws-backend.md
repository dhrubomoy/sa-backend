# Deploy sa-backend in AWS (EC2):

- ssh into the ubuntu machine

- clone repo and cd into folder

- Update 
```
sudo apt-get update
```
- Install pip
```
sudo apt install python3-pip
```

- Install virtualenv
```
sudo apt install virtualenv
```

- Create a virtual environment in Python 3 with the environment name of env:
```
virtualenv -p python3 env
```

- Activate env
```
source env/bin/activate
```

- Install packages 
```
pip3 install -r requirements.txt
```

- Create a folder called `models` inside `src/files/`. Then download all the .hdf5 files (mlsa-project/models) and save them inside the src/files/models/ folder that you created.
```
wget "https://www.dropbox.com/s/wirgt7epmi9y8p9/rnn-glove-model-01-0.8362.hdf5?dl=1" -O rnn-glove-model-01-0.8362.hdf5
```
```
wget "https://www.dropbox.com/s/yfncjn5ybx4b7i2/rnn-word2vec-model-03-0.8425.hdf5?dl=1" -O rnn-word2vec-model-03-0.8425.hdf5
```

- In file src/project/settings.py, add PUBLIC_DNS (e.g. `ec2-3-17-181-123.us-east-2.compute.amazonaws.com`) to to `ALLOWED_HOSTS` 

- Download the necessary NLTK data
```
python3 -m textblob.download_corpora
```

- Run migrations
```
python manage.py migrate
```
- Run server
```
python3 manage.py runserver 0.0.0.0:8000
```

Open browser and visit http://[PUBLIC_DNS]:8000/api/searched_tweets/ (e.g. http://ec2-3-17-181-123.us-east-2.compute.amazonaws.com:8000/api/searched_tweets/).
