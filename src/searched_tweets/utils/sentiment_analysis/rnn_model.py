import pickle
from keras.models import load_model
from sklearn.metrics import accuracy_score
from keras.preprocessing.sequence import pad_sequences
from keras import backend as K

RNN_W2V_MODEL_PATH = 'files/models/rnn-word2vec-model-03-0.8425.hdf5'
RNN_W2V_TOKENIZER_PATH = 'files/tokenizers/tokenizer-rnn-word2vec.pickle'

RNN_GLOVE_MODEL_PATH = 'files/models/rnn-glove-model-01-0.8362.hdf5'
RNN_GLOVE_TOKENIZER_PATH = 'files/tokenizers/tokenizer-rnn-glove.pickle'

class KerasAlg:

    def __init__(self, model_path, tokenizer_path):
        self.model = load_model(model_path)
        self.model._make_predict_function() # To avoid threading issue
        # Load tokenizer
        with open(tokenizer_path, 'rb') as handle:
            self.tokenizer = pickle.load(handle)


    def get_sentiment_prediction(self, text):
        test_sequences = self.tokenizer.texts_to_sequences([text])
        padded_test_sequences = pad_sequences(test_sequences, maxlen=35)
        pred = self.model.predict(padded_test_sequences, verbose=0, batch_size=2048)
        if(pred >= 0.5):
            return 'positive'
        else:
            return 'negative'



class RnnWord2Vec(KerasAlg):

    def __init__(self):
        KerasAlg.__init__(self, RNN_W2V_MODEL_PATH, RNN_W2V_TOKENIZER_PATH)


class RnnGloVe(KerasAlg):

    def __init__(self):
        KerasAlg.__init__(self, RNN_GLOVE_MODEL_PATH, RNN_GLOVE_TOKENIZER_PATH)