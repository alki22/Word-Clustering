
from __future__ import print_function
import sys
import nltk
import spacy
from sklearn.feature_extraction import DictVectorizer
from sklearn.cluster import KMeans
from sklearn.externals import joblib
from collections import defaultdict, OrderedDict

parser = spacy.load('es')

# dataset/file to cluster
file_name = "lavoztextodump.txt"

with open(file_name, 'r') as file:
    text = file.read()

parsedData = parser(text)
stopwords = nltk.corpus.stopwords.words('spanish')

corpus = []
# (Vector number <-> word) dictionary
vect_to_string = {}

index = 0
for token in parsedData:
    # Clean the corpus out of stopwords and non alphabetic tokens
    if token.orth_.isalpha() and token.lower_ not in stopwords:
        token_features = {
                        'lemma' : token.lemma, 
                        'log probability' : token.prob, 'POS tag' : token.pos,
                        'dependency' : token.dep, 'head' : token.head.text,
                        'name': token.orth 
                        }                
        corpus.append(token_features)
        vect_to_string[index] = token.orth_
        index += 1
vectorizer = DictVectorizer()
vectors = vectorizer.fit_transform(corpus)

# Run K-Means algorithm
k_clusters = 30
km = KMeans(n_clusters=k_clusters, init='k-means++', n_jobs=-1)
X = km.fit(vectors)

# Save results to avoid running the script every time
joblib.dump(km,  'doc_cluster.pkl')
clusters = defaultdict(list)

# Put every word's index into its cluster
for j in range(len(vect_to_string)):
    clusters[X.labels_[j]].append(j)

# Print results to output.txt
for j in range(len(clusters)):  
    print('Cluster', j, file=open("output.txt", "a"))
    print('==========================', file=open("output.txt", "a"))
    for k in clusters[j]:
            print(vect_to_string[k], file=open("output.txt", "a"))

