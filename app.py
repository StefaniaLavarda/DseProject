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
st.title("Movie Quiz Game")

# Instructions
st.write("Answer 10 multiple-choice questions about movies. Choose the correct option!")

# Initialize session state variables
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_question' not in st.session_state:
    st.session_state.current_question = 1
if 'correct_answers_by_difficulty' not in st.session_state:
    st.session_state.correct_answers_by_difficulty = {'easy': 0, 'medium': 0, 'hard': 0}
if 'total_correct_answers' not in st.session_state:
    st.session_state.total_correct_answers = 0

# Generate a new question until it reached the 10th question
if st.session_state.current_question <= 10:
    # Select difficulty
    level_of_difficulty = np.random.choice(['easy', 'medium', 'hard'])
    
    # Generate a question
    question, options, correct_answer = quiz.generate_question(difficulty=level_of_difficulty)

    # Display question and options
    st.subheader(f"Question {st.session_state.current_question}: {question}")
    user_answer = st.radio("Choose your answer:", options)

    # Submit button
    if st.button("Submit"):
        if user_answer == correct_answer:
            st.success("Correct!")
            st.session_state.score += score_by_difficulty[level_of_difficulty]
            st.session_state.total_correct_answers += 1
            st.session_state.correct_answers_by_difficulty[level_of_difficulty] += 1
        else:
            st.error(f"Wrong! The correct answer was: {correct_answer}")
        
        # Increment question number
        st.session_state.current_question += 1
else:
    # Display final score
    max_score = quiz.max_score(num_questions=10)
    st.write(f"Your final score is {st.session_state.score} out of {max_score}.")
    st.write(f"You answered {st.session_state.total_correct_answers} out of 10 questions correctly.")
    st.write("Quiz finished!")
    
