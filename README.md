## Sentiment Analysis Web App (Backend)
### Set up
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
- Create a folder called `models` inside `src/files/`. Then download all the .hdf5 files from our google drive shared folder (`mlsa-project/models`) and save them inside the `src/files/models/` folder that you created.
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
