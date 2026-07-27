import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD
docs = []
n = int(input("Enter number of documents: "))
for i in range(n):
docs.append(input("Enter document: "))
query = input("\nEnter search query: ")
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)
Expt.No:4 BUILD AN INFORMATION RETRIEVAL SYSTEMUSINGCLASSICALAND NONCLASSICAL MODELS ANDCOMPARETHEIR PERFORMANCE ON A DATASET OF SCIENTIFICPAPERS. Date:
query_vec = vectorizer.transform([query])
scores = cosine_similarity(query_vec, X)
print("\nTF-IDF Similarity Scores:")
for i, s in enumerate(scores[0]):
print("Document", i+1, ":", round(s, 3))
svd = TruncatedSVD(n_components=2)
X_lsa = svd.fit_transform(X)
query_lsa = svd.transform(query_vec)