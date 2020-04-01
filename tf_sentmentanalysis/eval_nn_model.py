from keras.models import Sequential, load_model
from keras.layers import Dense
import sys
import utils
import random
import numpy as np

FREQ_DIST_FILE = 'imdb-reviews-pt-br-processed_train-freqdist.pkl'
BI_FREQ_DIST_FILE = 'imdb-reviews-pt-br-processed_train-freqdist-bi.pkl'
UNIGRAM_SIZE = 15000
VOCAB_SIZE = UNIGRAM_SIZE
USE_BIGRAMS = True
if USE_BIGRAMS:
    BIGRAM_SIZE = 10000
    VOCAB_SIZE = UNIGRAM_SIZE + BIGRAM_SIZE
FEAT_TYPE = 'frequency'

def extract_features(tweets, unigrams, bigrams, batch_size=500, test_file=True, feat_type='presence'):
    num_batches = int(np.ceil(len(tweets) / float(batch_size)))
    for i in range(num_batches):
        batch = tweets[i * batch_size: (i + 1) * batch_size]
        features = np.zeros((batch_size, VOCAB_SIZE))
        labels = np.zeros(batch_size)
        for j, tweet in enumerate(batch):
            if test_file:
                tweet_words = tweet[1][0]
                tweet_bigrams = tweet[1][1]
            else:
                tweet_words = tweet[2][0]
                tweet_bigrams = tweet[2][1]
                labels[j] = tweet[1]
            if feat_type == 'presence':
                tweet_words = set(tweet_words)
                tweet_bigrams = set(tweet_bigrams)
            for word in tweet_words:
                idx = unigrams.get(word)
                if idx:
                    features[j, idx] += 1
            if USE_BIGRAMS:
                for bigram in tweet_bigrams:
                    idx = bigrams.get(bigram)
                    if idx:
                        features[j, UNIGRAM_SIZE + idx] += 1
        yield features, labels

def get_feature_vector(tweet, unigrams, bigrams):
    uni_feature_vector = []
    bi_feature_vector = []
    words = tweet.split()
    for i in range(len(words) - 1):
        word = words[i]
        next_word = words[i + 1]
        if unigrams.get(word):
            uni_feature_vector.append(word)
        if USE_BIGRAMS:
            if bigrams.get((word, next_word)):
                bi_feature_vector.append((word, next_word))
    if len(words) >= 1:
        if unigrams.get(words[-1]):
            uni_feature_vector.append(words[-1])
    return uni_feature_vector, bi_feature_vector

def process_tweets(csv_file, unigrams, bigrams, test_file=True):
    tweets = []
    print('Generating feature vectors')
    with open(csv_file, 'r') as csv:
        lines = csv.readlines()
        print(lines[0])
        total = len(lines)
        for i, line in enumerate(lines):
            if test_file:
                tweet_id, tweet = line.split(',')
            else:
                tweet_id, sentiment, tweet = line.split(',')
            feature_vector = get_feature_vector(tweet, unigrams, bigrams)
            if test_file:
                tweets.append((tweet_id, feature_vector))
            else:
                tweets.append((tweet_id, int(sentiment), feature_vector))
            utils.write_status(i + 1, total)
    print('\n')
    return tweets

def sentiment_analysis(indata):
    print("Predicting: {0}".format(indata))
    np.random.seed(1337)
    unigrams = utils.top_n_words(FREQ_DIST_FILE, UNIGRAM_SIZE)
    if USE_BIGRAMS:
        bigrams = utils.top_n_bigrams(BI_FREQ_DIST_FILE, BIGRAM_SIZE)
    batch_size = 500
    model = load_model('best_model.h5')
    
    test_data = [(1, get_feature_vector(indata, unigrams, bigrams))]
    n_test_batches = int(np.ceil(len(test_data) / float(batch_size)))
    predictions = np.array([])
    for test_set_X, _ in extract_features(test_data, unigrams, bigrams, feat_type=FEAT_TYPE, 
                                            batch_size=batch_size, test_file=True):
        prediction = np.round(model.predict_on_batch(test_set_X).flatten())
        predictions = np.concatenate((predictions, prediction))
    predictions = [(str(j), int(predictions[j])) for j in range(len(test_data))]
    
    if predictions[0][1] == 0:
        print("Feedback ruim")
        return 0
    else:
        print("Feedback bom")
        return 1

if __name__ == '__main__':
    sentiment_analysis(sys.argv[1])