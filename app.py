""" app.py """

import streamlit as st

from src.data import MoviesData
from src.quiz import Quiz

# Load the movies dataset into a DataFrame
file_path = 'data/movies_dataset.csv'
movies_data = MoviesData(path='data')
movies_df = movies_data.import_data(file_path)

# Create an instance of the Quiz class using the loaded data
quiz = Quiz(movies_df)

# Define the scoring for each difficulty level
score_by_difficulty = {'easy': 1, 'medium': 2, 'hard': 3}

# Title
st.title("Movie Quiz Game")

# Instructions
st.write("Answer 10 multiple-choice questions about movies. Choose the correct option!")
