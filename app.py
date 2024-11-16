""" app.py """

import streamlit as st
import numpy as np

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
st.title("Movie Quiz Game 🎞️")

# Instructions
st.write("Answer 10 multiple-choice questions about movies. Choose the correct option!")

# Generate 10 quiz questions
questions = []
answers = []
correct_answers = []
difficulties = []

# Generate 10 quiz questions
for i in range(10):
    # Randomly select a difficulty level
    level_of_difficulty = np.random.choice(['easy', 'medium', 'hard'])
    question, options, correct_answer = quiz.generate_question(difficulty=level_of_difficulty)
    
    # Append question, options, correct answer and level of difficulty
    questions.append((question, options))
    correct_answers.append(correct_answer)
    difficulties.append(level_of_difficulty)

# List to collect user answers
user_answers = []

# Initialize a counter for the question number
question_number = 1

# Display each question with options
for question, options in questions:
    st.subheader(f"Question {question_number}: {question}")
    user_answer = st.radio(
        f"Select your answer for Question {question_number}:", 
        options,
    )
    user_answers.append(user_answer)
    
    # Increment the counter for the next question
    question_number += 1 


