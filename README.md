# movie-reccomendation-system
# 🎬 Movie Recommendation System

A content-based movie recommendation system built using Python and a dataset from [Specify Your Source, e.g., Kaggle, MovieLens].

## ✨ Features

* **Content-Based Filtering:** Recommends movies based on similarity in genre, director, and/or keywords.
* **Cosine Similarity:** Uses a Vectorizer and Cosine Similarity to calculate the degree of likeness between movie features.
* **Web Interface:** Hosted via a simple web server FastAPI for user interaction.

## 🚀 Getting Started

### Prerequisites

You need **Python 3.x** installed.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/7aritri/movie-reccomendation-system.git](https://github.com/7aritri/movie-reccomendation-system.git)
    cd movie-reccomendation-system
    ```

2.  **Create and activate a virtual environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # .\venv\Scripts\activate   # On Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You must first create the `requirements.txt` file.)*

## ⚙️ How to Run the App

1.  **Ensure model files are present:**
    The system relies on the following files:
    * `cosine_sim.pkl`
    * `indices.pkl`
    * `tfidf_vectorizer.pkl`
    
    *(If these are managed by Git LFS, run `git lfs pull` here.)*

2.  **Execute the main application:**
    ```bash
    python main.py
    ```

3.  Open your web browser to `http://127.0.0.1:5000` (or whatever address the script specifies).

## 📚 Repository Structure
