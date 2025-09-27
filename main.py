from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import joblib

# Load model artifacts
movies = pd.read_csv("movies_clean.csv")
cosine_sim = joblib.load("cosine_sim.pkl")
indices = joblib.load("indices.pkl")

# FastAPI app
app = FastAPI(title="Movie Recommendation UI")
templates = Jinja2Templates(directory="templates")

# Recommendation function
def recommend_movies(title, num_recommendations=5):
    idx = indices.get(title)
    if idx is None:
        return ["Movie not found!"]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    movie_indices = [i[0] for i in sim_scores]
    return movies["title"].iloc[movie_indices].tolist()

# Home page
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Form submission
@app.post("/recommend_ui", response_class=HTMLResponse)
def recommend_ui(request: Request, title: str = Form(...), num_recommendations: int = Form(5)):
    recs = recommend_movies(title, num_recommendations)
    return templates.TemplateResponse("index.html", {"request": request, "recommendations": recs})
