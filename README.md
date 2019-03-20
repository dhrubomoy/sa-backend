
## Sentiment Analysis Web App (Backend)
### Set up in local computer
- Clone the repo
    ```
    git clone https://github.com/dhrubomoy/sa-backend.git
    ```
- Install virtualenv if not installed
    ```
    pip install virtualenv
    ```
- Create a virtual environment
    ```
    cd sa-backend
    virtualenv env
    ```
- Activate the environment
    ```
    source env/bin/activate
    ```
- Install packages
    ```
    pip install -r requirements.txt
    ```
- Open the `/src/sentiment_analysis/utils/twitter_analysis_utils.py` file and replace following lines with your actual consumer key and access token for twitter api
    ```
    consumer_key = 'YOUR CONSUMER KEY'
    consumer_secret = 'YOUR CONSUMER SECRET'
    access_token = 'YOUR ACCESS TOKEN'
    access_token_secret = 'YOUR ACCESS TOKEN SECRET'
    ```
- Copy the models in `src/files/models`
    - **Use existing model or tokenizer:** Create a folder called `models` inside `src/files/`. Download these models and save it inside the `models` folder: [rnn-glove-model-01-0.8362.hdf5](https://www.dropbox.com/s/wirgt7epmi9y8p9/rnn-glove-model-01-0.8362.hdf5?dl=0) and [rnn-word2vec-model-03-0.8425.hdf5](https://www.dropbox.com/s/yfncjn5ybx4b7i2/rnn-word2vec-model-03-0.8425.hdf5?dl=0)
    - **If you create a new model and tokenizer:** Create a folder called `models` inside `src/files/`. After training the model, copy the saved model in `models` folder, save the tokenizer in `src/files/tokenizers` folder. Make sure that that the names of the files are reflected in `src⁩/⁨sentiment_analysis⁩/⁨utils⁩/sentiment_analysis_utils⁩/rnn_model.py` file by updating variables such as `RNN_W2V_MODEL_PATH`, `RNN_GLOVE_MODEL_PATH` etc. 

Then download all the .hdf5 files from our google drive shared folder (`mlsa-project/models`) and save them inside the `src/files/models/` folder that you created.
- Apply migrations
    ```
    cd src
    python manage.py migrate
    ```
- Run server
    ```
    python manage.py runserver
    ```

The server should be up and running. Check http://127.0.0.1:8000/api/searched_tweets/

### Set up frontend in local computer

Follow instruction from [sa-frontend](https://github.com/dhrubomoy/sa-frontend) repository README

### Deploy to AWS (EC2)
Unfortunately deploying both backend and frontend to aws is quite tedious, and I couldn't find an easier way to make it easier.
Follow these instructions:
1. [Deploy backend](https://github.com/dhrubomoy/sa-backend/blob/master/deploy-aws-backend.md)
2. [Deploy frontend](https://github.com/dhrubomoy/sa-backend/blob/master/deploy-aws-frontend.md)
