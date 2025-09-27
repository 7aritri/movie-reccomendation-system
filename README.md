

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Project Structure](#project-structure)  
- [Installation](#installation)  
- [Usage](#usage)  
- [How It Works](#how-it-works)  
- [Datasets & Model Files](#datasets--model-files)  
- [Extending / Customization](#extending--customization)  
- [Requirements](#requirements)  
- [License](#license)  
- [Credits & Acknowledgments](#credits--acknowledgments)  

---

## Overview

This project implements a **content-based** movie recommendation engine. Given a movie title, it suggests similar movies by analyzing metadata (genres, keywords, descriptions, etc.) and computing similarity scores. The project also includes a minimal web interface to let users enter input and receive suggestions.

---

## Features

- Content-based filtering: recommends movies based on similarity of features (genre, keywords, etc.).  
- Uses **TF-IDF** vectorization + **cosine similarity** to compute similarity between movies.  
- Web interface (via a simple web server / framework) for user interaction.  
- Precomputed similarity matrix & index files for fast lookup.  

---

## Project Structure

movie-recommendation-system/ ├── templates/                    ← (if any HTML templates for UI)
├── main.py                        ← Entry point / web server
├── train_model.ipynb              ← Notebook to preprocess data & build model
├── movies_clean.csv               ← Cleaned movie metadata
├── tfidf_vectorizer.pkl           ← Serialized TF-IDF vectorizer
├── cosine_sim.pkl                 ← Serialized cosine similarity matrix
├── indices.pkl                     ← Mapping from titles ↔ indices
├── requirements.txt (optional)     ← Python dependencies
└── README.md                       ← This documentation

- **templates/** – HTML templates (if using Flask, FastAPI + Jinja, etc.)  
- **main.py** – runs the web server and handles recommendation requests  
- **train_model.ipynb** – code to preprocess data, compute TF-IDF, build similarity matrix  
- **movies_clean.csv** – dataset of movies after cleaning / preprocessing  
- **tfidf_vectorizer.pkl**, **cosine_sim.pkl**, **indices.pkl** – serialized model artifacts loaded by `main.py`

---

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/7aritri/movie-reccomendation-system.git
   cd movie-reccomendation-system

2. (Recommended) Set up a virtual environment

python3 -m venv venv
source venv/bin/activate   # macOS / Linux
# venv\Scripts\activate    # Windows


3. Install dependencies
Ensure you have a requirements.txt listing required packages (e.g. scikit-learn, pandas, flask or fastapi, etc.). Then run:

pip install -r requirements.txt




---

Usage

1. Make sure the serialized model files are present:

tfidf_vectorizer.pkl

cosine_sim.pkl

indices.pkl

movies_clean.csv



2. Run the main application:

python main.py


3. Open your browser and navigate to the displayed URL (e.g. http://127.0.0.1:8000).


4. Enter a movie title and receive a list of recommended similar movies.




---

How It Works

1. Data Preprocessing

Clean and prepare metadata (genres, keywords, descriptions, etc.).

Combine relevant textual fields into a single “feature string” per movie.



2. TF-IDF Vectorization

Convert the combined textual data into TF-IDF vectors.

Fit a TfidfVectorizer to the corpus; serialize it to tfidf_vectorizer.pkl.



3. Similarity Computation

Compute a cosine similarity matrix between all movie pairs.

Save it as cosine_sim.pkl.



4. Index Mapping

Maintain a mapping between movie titles and their indices.

Save it in indices.pkl.



5. Recommendation Flow

Given a movie title, look up its index.

Fetch the row of similarity scores; sort top related movies.

Return the top N movie recommendations to the user.





---

Datasets & Model Files

movies_clean.csv — cleaned and preprocessed movie metadata used to build the model.

tfidf_vectorizer.pkl — the fitted TF-IDF vectorizer (so you don’t re-train every time).

cosine_sim.pkl — precomputed cosine similarity matrix for fast lookup.

indices.pkl — mapping between movie titles and dataframe indices.


If you want to retrain the model (e.g., with more data), use train_model.ipynb to regenerate these artifacts.


---

Extending / Customization Ideas

Add collaborative filtering (user ratings) to build a hybrid recommender.

Incorporate more features (e.g. cast, director, release year, user reviews).

Improve UI/UX (search autocomplete, pagination, movie posters, etc.).

Deploy the app (e.g. to Heroku, AWS, or another cloud service).

Use a larger / more varied movie dataset (e.g. MovieLens, TMDb API).

Cache popular queries for better performance.



---

Requirements

Below is an example of packages you might need. You should create a requirements.txt:

numpy
pandas
scikit-learn
flask        # or fastapi / another web framework
gunicorn     # (if deploying)

You can freeze the actual versions using:

pip freeze > requirements.txt


---

License

(You can choose a license, e.g., MIT, Apache 2.0, etc.)

This project is released under the MIT License — see the LICENSE file for details.


---

Credits & Acknowledgments

Based on content-based recommendation fundamentals (TF-IDF, cosine similarity).

Inspired by tutorials and implementations using MovieLens / Kaggle datasets.

Thanks to the open-source community for sample datasets, code references, and best practices.



---
