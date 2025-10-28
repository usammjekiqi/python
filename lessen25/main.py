from fastapi import FastAPI ,HTTPException
from typing import List
import database
import models
from models import Movecreate, Movie

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "wellcome to crud "}


@app.post("/movies/", response_model=Movie)
def create_movie(movie: Movecreate):
    """Creates a new movie in the database"""
    movie_id = database.create_movie(movie)
    return database.Movie(id=movie_id , **movie.dict()) 

@app.get("/movies/{movie_id}", response_model=Movie)
def read_movie(movie_id: int):
    """reads out muvie from the database single movie """
    movie = database.read_movies(movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@app.put("/movies/{movie_id}", response_model=Movie)
def update_movie(movie_id: int, movie: Movecreate):
    """updates movie """
    updated = database.update_movie( movie_id, movie)
    if not updated:
        raise HTTPException(status_code=404, detail="Movie not found")
    return model.Movie(id=movie_id, **movie.dict())

@app.delete("/movies/{movie_id}", response_model=dict)
def delete_movie( movie_id: int):
    """deletes movie """
    deleted = database.delete_movie(movie_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"message": "Movie deleted successfully"}
  



