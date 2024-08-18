import pandas as pd
from sklearn.feature_extraction import text
from sklearn.metrics.pairwise import cosine_similarity

# read input data (data.csv)
df = pd.read_csv("data.csv", encoding="latin1")
print('\n')
print(' Original Data '.center(100, '-'))
print(df.head())

articles = df["Article"].tolist()
# perform cosine similarity
uni_tfidf = text.TfidfVectorizer(stop_words="english")
uni_matrix = uni_tfidf.fit_transform(articles)
uni_sim = cosine_similarity(uni_matrix)


def recommend_articles(x):
    return ", ".join(df["Title"].loc[x.argsort()[-5:-1]])


df["Recommended Articles"] = [recommend_articles(x) for x in uni_sim]
print('\n')
print(' Recommendation Data '.center(100, '-'))
print(df.head())
