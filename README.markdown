# Movie Recommendation System

## Overview
This repository contains a sophisticated movie recommendation system developed using Python. The system leverages machine learning techniques, including TF-IDF vectorization and cosine similarity, to provide personalized movie recommendations based on movie overviews, genres, cast, and crew data. The implementation includes a user-friendly Gradio interface with TMDB API integration for fetching movie posters and trailers, enhancing the user experience.

The system is designed to process two datasets (`tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`) and generates preprocessed data and similarity matrices saved as joblib files for efficient deployment. It supports fuzzy matching for robust movie title searches and provides a web-based interface for real-time recommendations.

## Features
- **Data Preprocessing**: Merges and cleans movie data, weighting genres, cast, and crew for enhanced recommendation accuracy.
- **TF-IDF Vectorization**: Converts movie tags into numerical vectors for similarity computation.
- **Cosine Similarity**: Computes similarity scores to rank related movies.
- **TMDB API Integration**: Fetches movie posters and YouTube trailers dynamically.
- **Gradio Interface**: Offers an interactive web application with shareable links.
- **Fuzzy Matching**: Handles typos or variations in movie titles.

## Prerequisites
- **Python 3.x**
- **Required Libraries**:
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `joblib`
  - `requests`
  - `gradio`
- **Google Colab**: For initial data mounting and processing (optional for local use).
- **TMDB API Key**: Obtain a free API key from [TMDB](https://www.themoviedb.org/) and replace the placeholder in the code.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/acharekarshubham12/Movie-recommendation-system.git
   cd Movie-recommendation-system
   ```
2. Install dependencies:
   ```
   pip install pandas numpy scikit-learn joblib requests gradio
   ```
3. Set up Git LFS to handle large `.csv` and `.joblib` files:
   - Install Git LFS: [Git LFS Download](https://git-lfs.github.com/)
   - Track files:
     ```
     git lfs install
     git lfs track "*.csv"
     git lfs track "*.joblib"
     git add .
     git commit -m "Track large files"
     git push origin main
     ```
4. Obtain a TMDB API key and update the `TMDB_API_KEY` variable in the code.

## Usage
1. **Prepare Data**:
   - Place `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` in your Google Drive or local directory.
   - Run the script in Google Colab to mount Drive and generate `movie_recommendation_df.joblib`, `movie_recommendation_similarity.joblib`, and `tfidf_vectorizer.joblib`.
2. **Launch the Interface**:
   - Run the script locally or in Colab:
     ```
     python script.py
     ```
   - Access the Gradio interface via the provided shareable link.
3. **Interact**:
   - Enter a movie name in the text box to receive top 5 recommendations with posters and trailer links.

## File Structure
- `tmdb_5000_movies.csv`: Movie metadata dataset.
- `tmdb_5000_credits.csv`: Cast and crew dataset.
- `movie_recommendation_df.joblib`: Preprocessed DataFrame.
- `movie_recommendation_similarity.joblib`: Similarity matrix.
- `tfidf_vectorizer.joblib`: Trained TF-IDF vectorizer (optional).
- `script.py`: Main Python script containing the recommendation logic and Gradio interface.

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests with detailed descriptions of changes. Ensure all tests pass and maintain the existing code style.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For questions or support, please contact [acharekarshubham12@gmail.com](mailto:acharekarshubham12@gmail.com).

## Acknowledgments
- Data sourced from [The Movie Database (TMDB)](https://www.themoviedb.org/).
- Built with open-source libraries from the Python ecosystem.
