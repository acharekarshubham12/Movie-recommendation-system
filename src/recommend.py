import joblib
import requests
from difflib import get_close_matches

# Load preprocessed data
new_df = joblib.load('../models/movie_recommendation_df.joblib')
similarity = joblib.load('../models/movie_recommendation_similarity.joblib')

# 🔑 Replace with your TMDB API key
TMDB_API_KEY = "YOUR_TMDB_API_KEY"

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return None

def fetch_trailer(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={TMDB_API_KEY}&language=en-US"
    data = requests.get(url).json()
    for video in data.get('results', []):
        if video['site'] == 'YouTube' and video['type'] == 'Trailer':
            return f"https://www.youtube.com/watch?v={video['key']}"
    return None

def get_closest_title(movie_name):
    movie_name = movie_name.lower().strip()
    titles = new_df['title'].str.lower().tolist()
    matches = get_close_matches(movie_name, titles, n=1, cutoff=0.6)
    return matches[0] if matches else None

def recommend(movie_name):
    closest_title = get_closest_title(movie_name)
    if not closest_title:
        return "<p>❌ Movie not found in database.</p>"

    idx = new_df[new_df['title'].str.lower() == closest_title].index[0]
    distances = similarity[idx]
    movie_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    html_content = "<div style='display:flex; flex-wrap:wrap;'>"
    for i in movie_list:
        movie_id = new_df.iloc[i[0]].movie_id
        title = new_df.iloc[i[0]].title
        poster_url = fetch_poster(movie_id)
        trailer_url = fetch_trailer(movie_id)
        if poster_url:
            if trailer_url:
                html_content += f"""
                <div style='margin:10px; text-align:center;'>
                    <a href='{trailer_url}' target='_blank'>
                        <img src='{poster_url}' width='200'><br>
                        <b>{title}</b>
                    </a>
                </div>
                """
            else:
                html_content += f"""
                <div style='margin:10px; text-align:center;'>
                    <img src='{poster_url}' width='200'><br>
                    <b>{title}</b>
                </div>
                """
    html_content += "</div>"
    return html_content
