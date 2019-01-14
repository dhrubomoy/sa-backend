from django.db import models

class SentimentPrediction(models.Model):
    # machine learning model's prediction: number or string?
    # choosig string for now (e.g. 'positive', 'negative' etc)
    naive_bayes = models.CharField(max_length=15, blank=True, null=True)
    pattern_analyzer = models.CharField(max_length=15, blank=True, null=True)
    rnn_word2vec = models.CharField(max_length=15, blank=True, null=True)
    rnn_gloVe = models.CharField(max_length=15, blank=True, null=True)

class Tweet(models.Model):
    text = models.TextField()
    user_location = models.CharField(max_length=30)
    created_at = models.CharField(max_length=20)
    sentiment_prediction = models.OneToOneField(
        SentimentPrediction, 
        blank=True,
        null=True, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.text


class SearchedTweet(models.Model):
    query = models.CharField(max_length=100)
    tweets = models.ManyToManyField(Tweet, blank=True)

    def __str__(self):
        return self.query
