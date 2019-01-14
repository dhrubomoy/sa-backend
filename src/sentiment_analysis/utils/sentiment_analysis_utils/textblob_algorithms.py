from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

class NaiveBayesAlg:
    
    def __init__(self):
        self.analyzer = NaiveBayesAnalyzer()

    def get_sentiment_prediction(self, text):
        analysis = TextBlob(text, analyzer=self.analyzer)
        if analysis.sentiment.classification == 'pos':
            return 'positive'
        elif analysis.sentiment.classification == 'neg':
            return 'negative'


class PatternLibAlg:
    
    def get_sentiment_prediction(self, text):
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:     # Positive
            return 'positive'
        elif analysis.sentiment.polarity < 0:   # Negative
            return 'negative'
        else:
            return 'neutral'

                      