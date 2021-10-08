import pickle
import random
import re
import string
from time import time

import nltk
from nltk import NaiveBayesClassifier, classify
from nltk.corpus import stopwords, twitter_samples
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

# # nltk.download('twitter_samples')
# # nltk.download('wordnet')
# # nltk.download('averaged_perceptron_tagger')
# # nltk.download('stopwords')
# # nltk.download('punkt')


class TwitterSentiment:

    positive_tokenized = twitter_samples.tokenized('positive_tweets.json')
    negative_tokenized = twitter_samples.tokenized('negative_tweets.json')
    neutral_tokenized = twitter_samples.tokenized(
        'tweets.20150430-223406.json')

    PKL_MODEL_FILENAME = 'pkl_classifier.pkl'

    def clean(self, tokens, stop_words=stopwords.words('english')):
        """Method to remove nosie and lemmetize tokens"""
        clean = []
        lemmatizer = WordNetLemmatizer()
        for token, tag in pos_tag(tokens):
            token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'
                           '(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', token)
            token = re.sub("(@[A-Za-z0-9_]+)", "", token)
            if tag.startswith('NN'):
                pos = 'n'
            elif tag.startswith('VB'):
                pos = 'v'
            else:
                pos = 'a'
            token = lemmatizer.lemmatize(token, pos)
            if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
                clean.append(token.lower())

        return clean

    def get_cleaned_list(self):
        positive_cleaned = []
        negative_cleaned = []
        neutral_cleaned = []

        for tokens in self.positive_tokenized:
            positive_cleaned.append(self.clean(tokens))

        for tokens in self.negative_tokenized:
            negative_cleaned.append(self.clean(tokens))

        for tokens in self.neutral_tokenized:
            neutral_cleaned.append(self.clean(
                tokens, stopwords.words('english')))

        return (positive_cleaned, negative_cleaned)

    # def get_all_words(cleand_list):
    #     """Generator function for getting all the words in the list"""
    #     for sentence in cleand_list:
    #         for token in sentence:
    #             yield token

    def get_tweets_for_model(self, cleaned_list):
        for sentence in cleaned_list:
            yield dict([token, True] for token in sentence)

    def get_dataset(self):
        positive_cleaned, negative_cleaned = self.get_cleaned_list()
        positive_model = self.get_tweets_for_model(
            positive_cleaned)
        negative_model = self.get_tweets_for_model(
            negative_cleaned)
        pd = [(tweet_dict, 'Positive') for tweet_dict in positive_model]
        nd = [(tweet_dict, 'Negative') for tweet_dict in negative_model]
        dataset = pd+nd
        random.shuffle(dataset)
        train_data = dataset[7000:]
        test_data = dataset[:7000]
        return (train_data, test_data)

    def get_model(self):
        train_data, _ = self.get_dataset()
        classifier = NaiveBayesClassifier.train(train_data)
        return classifier

    def save_model(self):
        classifier = self.get_model()
        with open(self.PKL_MODEL_FILENAME, 'wb') as f:
            pickle.dump(classifier, f)

    def get_tokens(self, sentence):
        return self.clean(word_tokenize(sentence))

    def analyze(self, sentence):
        tokens = self.get_tokens(sentence)
        with open(self.PKL_MODEL_FILENAME, 'rb') as f:
            classifier = pickle.load(f)
        return classifier.classify(dict([token, True] for token in tokens))


if __name__ == '__main__':
    start = time()
    s = input('Enter the sentence you want to analyze: ')
    sentiment = TwitterSentiment()
    analysis = sentiment.analyze(s)
    print(analysis)
    print(time()-start)
