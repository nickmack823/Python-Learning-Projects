from os.path import exists

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import random
import statistics
import pickle
from sklearn.naive_bayes import (BernoulliNB, ComplementNB, MultinomialNB,)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

# NLTK Resources used:
# names: A list of common English names compiled by Mark Kantrowitz

# stopwords: A list of really common words, like articles, pronouns, prepositions, and conjunctions

# state_union: A sample of transcribed State of the Union addresses by different US presidents,
# compiled by Kathleen Ahrens

# twitter_samples: A list of social media phrases posted to Twitter

# movie_reviews: Two thousand movie reviews categorized by Bo Pang and Lillian Lee

# averaged_perceptron_tagger: A data model that NLTK uses to categorize words into their part of speech

# vader_lexicon: A scored list of words and jargon that NLTK references when performing sentiment analysis,
# created by C.J. Hutto and Eric Gilbert

# punkt: A data model created by Jan Strunk that NLTK uses to split full texts into word lists

# words = [word for word in nltk.corpus.state_union.words() if word.isalpha()]
# stopwords = nltk.corpus.stopwords.words("english")
# # Filter out stopwords from words list
# words = [word for word in words if word.lower() not in stopwords]
#
# # Word frequencies in list
# frequency_distribution = nltk.FreqDist(words)
# print(frequency_distribution.most_common(3))
# frequency_distribution.tabulate(3)
#
# # Get frequency of specific word
# print(frequency_distribution['America'])
#
# # Normalizing all words to lowercase for accuracy
# lower_fd = nltk.FreqDist([word.lower() for word in frequency_distribution])
#
# # Could create freq-dist for words of particular letter, length, containing certain letters, etc.
#
# # Concordance: a collection of word locations along with their context
# # Used to find: number of word occurrences, locations of occurrences, words surrounding occurrences
#
# # Including stopwords here
# text = nltk.Text(nltk.corpus.state_union.words())
# concordance_list = text.concordance_list("america", lines=5)
# for entry in concordance_list:
#     print(entry.line)
#
# # Alternative to FreqDist
# # fd = text.vocab()
#
# # Collocations: series of words that frequently appear together (ex. 'United' and 'States')
# # bigrams (two-word), trigrams, quadgrams
#
# finder = nltk.collocations.TrigramCollocationFinder.from_words(words)
# print(finder.ngram_fd.tabulate(2))

# NLTK pre-trained analyzer: VADER
# Best suited for social media language (short sentences with slang y abbreviations)
sia = SentimentIntensityAnalyzer()


# print(sia.polarity_scores("Wow, NLTK is really powerful"))

# tweets = [tweet for tweet in nltk.corpus.twitter_samples.strings()]
#
#
# def is_tweet_positive(tweet):
#     """Returns true if tweet has a positive compound sentiment, otherwise False."""
#     return sia.polarity_scores(tweet)["compound"] > 0

# random.shuffle(tweets)
#
# for tweet in tweets[:10]:
#     print(">", is_positive(tweet), tweet)

def is_review_positive(review_id):
    """True if the average of all sentence compound scores is positive, otherwise False."""
    text = nltk.corpus.movie_reviews.raw(review_id)
    # Gets compound score for each sentence in text (VADER likes sentences)
    scores = [sia.polarity_scores(sentence)["compound"] for sentence in nltk.sent_tokenize(text)]
    return statistics.mean(scores) > 0.1


# IDs for movie reviews
# positive_review_ids = nltk.corpus.movie_reviews.fileids(categories=["pos"])
# negative_review_ids = nltk.corpus.movie_reviews.fileids(categories=["neg"])
# all_review_ids = positive_review_ids + negative_review_ids

# random.shuffle(all_review_ids)
#
# accuracies = {'TP': 0, 'TN': 0, 'FP': 0, 'FN': 0}
# done = 0
# for id in all_review_ids:
#     if done % 100 == 0:
#         print(f"Completed: {done}/{len(all_review_ids)}")
#     if is_review_positive(id):
#         if id in positive_review_ids:
#             accuracies['TP'] += 1
#         else:
#             accuracies['FP'] += 1
#     else:
#         if id in negative_review_ids:
#             accuracies['TN'] += 1
#         else:
#             accuracies['FN'] += 1
#     done += 1
#
# percent_accuracies = [accuracies[key]/len(all_review_ids) for key in accuracies.keys()]
# print(accuracies)
# print(percent_accuracies)
# acc = percent_accuracies[0] + percent_accuracies[1]
# print(f"Accuracy: {acc}%")


# Selecting Useful Features
unwanted = nltk.corpus.stopwords.words("english")
# Add names to unwanted words list, they don't help much for sentiment
unwanted.extend([w.lower() for w in nltk.corpus.names.words()])


def skip_unwanted(pos_tuple):
    # print(pos_tuple)
    word, tag = pos_tuple
    if not word.isalpha() or word in unwanted:
        return False
    # Skip singular nouns
    if tag.startswith("NN"):
        return False
    return True


# top_100_neg = {word for word, count in negative_fd.most_common(100)}
# print(top_100_pos)

# Finding meaningful bigrams
# positive_bigram_finder = nltk.collocations.BigramCollocationFinder.from_words([
#     w for w in nltk.corpus.movie_reviews.words(categories=["pos"])
#     if w.isalpha() and w not in unwanted
# ])
# negative_bigram_finder = nltk.collocations.BigramCollocationFinder.from_words([
#     w for w in nltk.corpus.movie_reviews.words(categories=["neg"])
#     if w.isalpha() and w not in unwanted
# ])

# print(positive_bigram_finder.ngram_fd.tabulate(3))


def extract_features(text):
    """Finds features that indicate positivity in given text"""
    features = {}
    wordcount = 0
    compound_scores = []
    positive_scores = []

    # Go through text sentences
    for sentence in nltk.sent_tokenize(text):
        # Go through individual words
        for word in nltk.word_tokenize(sentence):
            # Check if word is in the above list of positive words
            if word.lower() in top_100_pos:
                wordcount += 1
        # Use VADER to determine scores for the sentence
        compound_scores.append(sia.polarity_scores(sentence)["compound"])
        positive_scores.append(sia.polarity_scores(sentence)["pos"])

    # Adding 1 to the final compound score to always have positive numbers
    # since some classifiers don't work with negative numbers.
    features["mean_compound"] = statistics.mean(compound_scores) + 1
    features["mean_positive"] = statistics.mean(positive_scores)
    features["wordcount"] = wordcount

    return features


# Saving top 100 positive words to file to save time on rerun
top_100_pos_file_exists = exists('top100pos')
if top_100_pos_file_exists:
    print('top100pos exists')
    with open('top100pos', 'rb') as f:
        top_100_pos = pickle.load(f)
else:
    print('top100pos does not exist, getting')
    positive_words = [word for word, tag in filter(
        skip_unwanted,
        nltk.pos_tag(nltk.corpus.movie_reviews.words(categories=["pos"]))
    )]
    negative_words = [word for word, tag in filter(
        skip_unwanted,
        nltk.pos_tag(nltk.corpus.movie_reviews.words(categories=["neg"]))
    )]

    # FD of pos y neg words
    positive_fd = nltk.FreqDist(positive_words)
    negative_fd = nltk.FreqDist(negative_words)

    # Words shared by pos y neg
    intersection = set(positive_fd).intersection(negative_fd)

    # Remove shared (ambiguous) words
    for word in intersection:
        del positive_fd[word]
        del negative_fd[word]

    top_100_pos = {word for word, count in positive_fd.most_common(100)}
    with open('top100pos', 'wb') as f:
        pickle.dump(top_100_pos, f)

# Training and Using a Classifier

# Create list of tuples, first item dictionary from extract_features, next is predefined category
# of the text (the review)

features_file_exists = exists('features')
if features_file_exists and top_100_pos_file_exists:
    with open('features', 'rb') as f:
        features = pickle.load(f)
else:
    features = [(extract_features(nltk.corpus.movie_reviews.raw(review)), 'pos')
                for review in nltk.corpus.movie_reviews.fileids(categories=['pos'])]
    features.extend([(extract_features(nltk.corpus.movie_reviews.raw(review)), 'neg')
                     for review in nltk.corpus.movie_reviews.fileids(categories=['neg'])])
    with open('features', 'wb') as f:
        pickle.dump(features, f)

# Now, train the classifier. Split one portion of the data for training, another portion for performance evaluation

train_count = len(features) // 4  # Using 1/4 of the features for training
random.shuffle(features)  # Shuffle to avoid grouping similarly classified reviews
# Create classifier considering features up to the train_count index
classifier = nltk.NaiveBayesClassifier.train(features[:train_count])
classifier.show_most_informative_features(10)

# Check classifier accuracy
nltk.classify.accuracy(classifier, features[train_count:])
print(nltk.classify.accuracy(classifier, features[train_count:]))

with open('new_review.txt', encoding='utf-8') as f:
    new_review = ''
    for line in f:
        new_review += line

# Testing a new positive review
new_features = extract_features(new_review)
print(new_features)
print(classifier.classify(new_features))

# Comparing Additional Classifiers
classifiers = {
    "BernoulliNB": BernoulliNB(),
    "ComplementNB": ComplementNB(),
    "MultinomialNB": MultinomialNB(),
    "KNeighborsClassifier": KNeighborsClassifier(),
    "DecisionTreeClassifier": DecisionTreeClassifier(),
    "RandomForestClassifier": RandomForestClassifier(),
    "LogisticRegression": LogisticRegression(),
    "MLPClassifier": MLPClassifier(max_iter=1000),
    "AdaBoostClassifier": AdaBoostClassifier(),
}

# Testing classifiers
random.shuffle(features)
for name, sklearn_classifier in classifiers.items():
    # Create classifier
    classifier = nltk.classify.SklearnClassifier(sklearn_classifier)
    # Train
    classifier.train(features[:train_count])
    # Test accuracy
    accuracy = nltk.classify.accuracy(classifier, features[train_count:])
    print(f"{accuracy:.2%} - {name}")

