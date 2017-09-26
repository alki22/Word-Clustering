
from __future__ import print_function
import sys
import nltk
import spacy
from sklearn.feature_extraction import DictVectorizer
from sklearn.cluster import KMeans
from sklearn.externals import joblib
from collections import defaultdict, OrderedDict

parser = spacy.load('es')
file_name = "xaa"
with open(file_name, 'r') as file:
    text = file.read()
parsedData = parser(text)
stopwords = nltk.corpus.stopwords.words('spanish')

corpus = []
vect_to_string = {}

i = 0
for token in parsedData:
    if token.orth_.isalpha() and token.orth_ not in stopwords:
        token_features = {
                        'lemma' : token.lemma, 
                        'log probability' : token.prob, 'POS tag' : token.pos,
                        'dependency' : token.dep, 'head' : token.head.text,
                        'name': token.orth 
                        }
        corpus.append(token_features)
        vect_to_string[i] = token.orth_
        i += 1

vectorizer = DictVectorizer()
vectors = vectorizer.fit_transform(corpus)
# Run K-Means algorithm
k_clusters = 10
km = KMeans(n_clusters=k_clusters, init='k-means++', n_jobs=-1)
X = km.fit(vectors)

# Save results to avoid running the script every time
joblib.dump(km,  'doc_cluster.pkl')
clusters = defaultdict(list)

for j in range(len(vect_to_string)):
    clusters[X.labels_[j]].append(vect_to_string[j])

sorted(clusters)

# Print results
for j in range(len(clusters)):
    print('Cluster', j, file=open("output.txt", "a"))
    
    # Remove duplicated entries
    clusters[j] = list(OrderedDict.fromkeys(clusters[j]))
    
    for word in clusters[j]:
            print(word, file=open("output.txt", "a"))

