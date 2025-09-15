import pandas as pd
import numpy as np
import ast
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
movies = pd.read_csv('../data/tmdb_5000_movies.csv')
credits = pd.read_csv('../data/tmdb_5000_credits.csv')

# Merge datasets on 'title'
movies = movies.merge(credits, on='title')

# Keep useful features
movies = movies[['movie_id','title','overview','genres','cast','crew']]
movies.dropna(inplace=True)

# Convert strings to lists
def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

movies['genres'] = movies['genres'].apply(convert)
movies['cast'] = movies['cast'].apply(lambda x: [i['name'] for i in ast.literal_eval(x)][:3])
movies['crew'] = movies['crew'].apply(lambda x: [i['name'] for i in ast.literal_eval(x) if i['job']=='Director'])

# Clean spaces
movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ","") for i in x])
movies['cast'] = movies['cast'].apply(lambda x: [i.replace(" ","") for i in x])
movies['crew'] = movies['crew'].apply(lambda x: [i.replace(" ","") for i in x])
movies['overview'] = movies['overview'].apply(lambda x: x.split())

# Weighted tags
movies['tags'] = movies['overview'] + movies['genres']*3 + movies['cast']*3 + movies['crew']*5
new_df = movies[['movie_id','title','tags']].copy()
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))

# Vectorization
tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
vectors = tfidf.fit_transform(new_df['tags']).toarray()
similarity = cosine_similarity(vectors)

# Save preprocessed data & models
joblib.dump(new_df, '../models/movie_recommendation_df.joblib')
joblib.dump(similarity, '../models/movie_recommendation_similarity.joblib')
joblib.dump(tfidf, '../models/tfidf_vectorizer.joblib')

print("✅ Preprocessing complete. Models saved in /models/")
