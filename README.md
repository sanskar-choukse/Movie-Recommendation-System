# 🎬 Movie Recommendation System

A content-based movie recommendation system built with FastAPI, Streamlit, and machine learning. Get personalized movie recommendations based on your favorite films using TF-IDF vectorization and cosine similarity.

## � Live Demo
(https://movie-recommendation-system-zukjowqs6ouc6iepssjgv3.streamlit.app/?view=home#movie-recommender)

## 🌟 Features

- **Smart Recommendations**: Uses TF-IDF and cosine similarity to find similar movies
- **Rich Movie Details**: Displays posters, ratings, genres, and overviews from TMDB API
- **Modern UI**: Clean, responsive interface built with Streamlit
- **Fast API Backend**: RESTful API powered by FastAPI
- **Real-time Search**: Instant movie search and recommendations

## 🛠️ Tech Stack

- **Backend**: FastAPI, Python 3.11
- **Frontend**: Streamlit
- **ML Libraries**: scikit-learn, pandas, numpy
- **API**: TMDB (The Movie Database)
- **Deployment**: Render (Backend), Streamlit Cloud (Frontend)

## � How It Works

1. **Data Processing**: Movie metadata is processed and cleaned from the TMDB dataset
2. **Feature Engineering**: Combined features (title, overview, genres) are created
3. **TF-IDF Vectorization**: Text features are converted to numerical vectors
4. **Similarity Calculation**: Cosine similarity is computed between movies
5. **Recommendation**: Top similar movies are returned based on user selection

## 📁 Project Structure

```
Movie-Recommendation-System/
├── main.py                    # FastAPI backend
├── app.py                     # Streamlit frontend
├── regenerate_pickles.py      # Script to regenerate pickle files
├── requirements.txt           # Python dependencies
├── runtime.txt               # Python version for deployment
├── .env                      # Environment variables (not in git)
├── movies_metadata.csv       # Movie dataset
├── df.pkl                    # Processed dataframe
├── indices.pkl               # Movie title to index mapping
├── tfidf.pkl                 # TF-IDF vectorizer
└── tfidf_matrix.pkl          # TF-IDF matrix
```

## � Deployment

### Backend (Render)
1. Connect your GitHub repository to Render
2. Set environment variable: `TMDB_API_KEY`
3. Build command: `pip install -r requirements.txt`
4. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Frontend (Streamlit Cloud)
1. Connect your GitHub repository to Streamlit Cloud
2. Main file: `app.py`
3. Python version: 3.11.9 (from runtime.txt)
4. Deploy!

## 🔑 Getting TMDB API Key

1. Go to [TMDB](https://www.themoviedb.org/)
2. Create an account
3. Go to Settings → API
4. Request an API key (choose "Developer" option)
5. Fill in the application details:
   - Application URL: `http://localhost:8501`
   - Application Summary: "Movie recommendation system for learning purposes"

## 👨‍💻 Author

**Sanskar Choukse**
- GitHub: [@sanskar-choukse](https://github.com/sanskar-choukse)

## 🙏 Acknowledgments

- Movie data from [TMDB](https://www.themoviedb.org/)
- Built with [FastAPI](https://fastapi.tiangolo.com/) and [Streamlit](https://streamlit.io/)

---

⭐ If you found this project helpful, please give it a star!
