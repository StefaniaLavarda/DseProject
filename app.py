""" 
Runs the movie quiz app, generates questions, tracks answers, and displays results using Streamlit.
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Import the necessary classes from data.py and quiz.py
from src.data import MoviesData
from src.quiz import Quiz

# Load the movies dataset into a DataFrame
file_path = 'data/movies_dataset.csv'
movies_data = MoviesData(path='data')
movies_df = movies_data.import_data(file_path)

# Create an instance of the Quiz class using the loaded data
quiz = Quiz(movies_df)

# Define scoring rules for each difficulty level
score_by_difficulty = {'easy': 1, 'medium': 2, 'hard': 3}

# Initialize a session state variable to track if the user wants to stop playing
if 'stop_playing' not in st.session_state:
    st.session_state.stop_playing = False

# If the user decided to stop playing, display a thank-you message and stop the app
if st.session_state.stop_playing:
    st.title("Thank you for playing! 😄")
    st.stop()  # Stop the execution of the app

# Set the app title and display initial instruction
st.title("Movie Quiz Game 🎞️")
st.write("Answer 10 multiple-choice questions about movies. Choose the correct option!")

# Initialize session state variables if not already present
if 'questions' not in st.session_state:
    questions = [] # Store generated questions and their options
    correct_answers = [] # Store correct answers for the questions
    difficulties = [] # Store difficulty levels of each question
    
    # Generate 10 random quiz questions
    for i in range(10):
        # Randomly select a difficulty level for each question
        level_of_difficulty = np.random.choice(['easy', 'medium', 'hard'])
        question, options, correct_answer = quiz.generate_question(difficulty=level_of_difficulty)
        
        # Store the question, options, correct answer, and difficulty level
        questions.append((question, options))
        correct_answers.append(correct_answer)
        difficulties.append(level_of_difficulty)
    
    # Save these variables in the Streamlit session state for persistence
    st.session_state.questions = questions
    st.session_state.correct_answers = correct_answers
    st.session_state.difficulties = difficulties
    st.session_state.quiz_completed = False
    
    # Initialize empty answers for each question
    st.session_state.user_answers = [''] * 10
   
# Retrieve session state variables
questions = st.session_state.questions
correct_answers = st.session_state.correct_answers
user_answers = st.session_state.user_answers
difficulties = st.session_state.difficulties

# Display each question along with its answer options
for question_number, (question, options) in enumerate(questions, 1):
    st.subheader(f"Question {question_number}: {question}")
    # Radio button for the user to select an answer
    user_answer = st.radio(
        f"Select your answer for Question {question_number}:", options)
    # Save the user's answer
    user_answers[question_number - 1] = user_answer

# Add a button to submit answers and calculate the score
if st.button("Submit Answers"):
    score = 0 # Initialize the total score
    total_correct_answers = 0 # Count the number of correct answers
    correct_answers_by_difficulty = {'easy': 0, 'medium': 0, 'hard': 0} # Track correct answers by difficulty
    
    # Feedback for each question
    st.subheader("Question Feedback")
    
    # Evaluate the user's answers and calculate their score
    for i in range(10):
        question, options = questions[i]
        user_answer = user_answers[i]
        correct_answer = correct_answers[i]
        difficulty = difficulties[i]

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            # Update score and counters for correct answers
            score += score_by_difficulty[difficulty]
            total_correct_answers += 1
            correct_answers_by_difficulty[difficulty] += 1
            # Display feedback for a correct answer
            st.write(f"**Question {i + 1}:** Correct ✅")
        else:
            # Display feedback for an incorrect answer
            st.write(f"**Question {i + 1}:** Wrong ❌")
            st.markdown(f"- **Your answer:** {user_answer}")
            st.markdown(f"- **The correct answer was:** {correct_answer}")
   
    # Calculate the maximum possible score
    ideal_scores = np.array([score_by_difficulty[difficulty] for difficulty in difficulties])
    max_score = np.sum(ideal_scores)
    
    # Calculate percentage of correct answers
    correct_percentage = np.round((total_correct_answers / 10) * 100, 2)

    # Display the final score and summary
    st.success(f'Your final score is: {score} out of {max_score}.')
    st.info(f"You answered {total_correct_answers} out of 10 questions correctly.")
    st.info(f"That's {correct_percentage}% correct answers!")
    
    # Generate a bar chart showing correct answers by difficulty level
    difficulty_levels = ['Easy', 'Medium', 'Hard']
    correct_counts = [correct_answers_by_difficulty['easy'],
                  correct_answers_by_difficulty['medium'],
                  correct_answers_by_difficulty['hard']]

    fig, ax = plt.subplots()
    ax.bar(difficulty_levels, correct_counts, color=['green', 'orange', 'red'])
    ax.set_title("Correct Answers by Difficulty Level", fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel("Difficulty Level", fontsize=12, labelpad=20)
    ax.set_ylabel("Number of Correct Answers", fontsize=12, labelpad=20)
    ax.set_ylim(0, 10)
    ax.set_yticks(range(0, 11))
    
    # Display the bar chart in the app
    st.pyplot(fig)
    
    # Mark the quiz as completed in the session state
    st.session_state.quiz_completed = True

# Show "Play Again" and "Don't Play Again" options after the quiz is completed
if st.session_state.quiz_completed:
    if st.button("Play again"):
        st.session_state.clear()  # Reset all session state variables
        st.rerun()  # Rerun the app to start a new quiz
    if st.button("Don't play again"):
        st.session_state.stop_playing = True
        st.rerun()  # Rerun the app to display the thank-you message
