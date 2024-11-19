# Movie Quiz Game 🎬
## Project Description  
The **Movie Quiz Game** is an interactive quiz application built using **Streamlit**. It generates a dynamic set of multiple-choice questions based on a movie dataset. Players answer questions, receive instant feedback, and are scored based on the difficulty of the questions.

This project aims to provide an engaging way to test and enhance your movie knowledge while exploring concepts such as data processing, randomization, and interactive user interfaces.

---

## Features  
- **Dynamic Quiz Generation**: Randomly generated movie-related questions with three difficulty levels (easy, medium, hard).  
- **Scoring System**: Scoring is weighted by question difficulty:  
  - Easy: 1 point  
  - Medium: 2 points  
  - Hard: 3 points  
- **Interactive Feedback**: Provides instant feedback for correct/incorrect answers.  
- **Performance Visualization**: A bar chart displays the number of correct answers for each difficulty level.  
- **Replay Option**: Allows players to restart the game after completion.  

---

## How the Project is Organized  

The project is structured into three main components:  

1. **Data Preparation**  
   - The `data/` folder contains the `movies_dataset.csv` file, which serves as the source of movie information.  
   - The `src/data.py` file loads and preprocesses this dataset to prepare it for quiz generation.  

2. **Quiz Functionality**  
   - The `src/quiz.py` file handles question creation and evaluation. It selects random questions from the dataset and ensures difficulty-based scoring.  

3. **Streamlit Application**  
   - The main application is in `app.py`, which combines the data and quiz functionalities into an interactive web app. Players can answer questions, view feedback, and check their scores through the Streamlit interface.  

---
 
