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

if 'questions' not in st.session_state:
    questions = []
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
    
    # # Save the questions and answers in session state
    st.session_state.questions = questions
    st.session_state.correct_answers = correct_answers
    st.session_state.difficulties = difficulties
    
    # Initialize empty answers for each question
    st.session_state.user_answers = [''] * 10
   
# Use the questions and answers stored in session state
questions = st.session_state.questions
correct_answers = st.session_state.correct_answers
user_answers = st.session_state.user_answers

# Initialize a counter for the question number
question_number = 1

# Display each question with options
for question_number, (question, options) in enumerate(questions, 1):
    st.subheader(f"Question {question_number}: {question}")
    
    # Get the user's answer
    user_answer = st.radio(
        f"Select your answer for Question {question_number}:", options)
    
    # Save the user's answer
    user_answers[question_number - 1] = user_answer


