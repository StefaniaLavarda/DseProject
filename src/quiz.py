# src/quiz.py

import numpy as np

class Quiz:
    """
       A class for generating random questions, with four options, one of which 
       is correct. Return the question, the correct answer and the options.
    """
    def __init__(self, data):
        self.data = data
  
    def question_year(self,data):
        """
            Generates a question asking for the release year of a randomly chosen movie.
        """
        # Choose a random movie and select, from the df, the title and year of the movie
        question_row = data.sample(1).iloc[0]
        primary_title = question_row['primaryTitle']
        start_year = question_row['startYear']

        # Create the question string using the selected movie's title
        question = f"What year was the movie '{primary_title}' released?"
        correct_answer = start_year
       
        # Generate multiple choices options
        options = set()
        options.add(correct_answer)
        while len(options) < 4:
            random_year = np.random.choice(range(1894, 2024))
            options.add(random_year)
        
        # Convert the set option to a list and shuffle it
        options = list(options)
        np.random.shuffle(options)
        
        return question, options, correct_answer

    def question_director(self, data):
        """
            Generates a question asking who directed a randomly chosen movie.
        """
        # choose a random movie and select the title and the name of the director
        question_row = data.sample(1).iloc[0]
        primary_title = question_row['primaryTitle']
        director_name = question_row['primaryName']

        question = f"Who is the director of the movie '{primary_title}'?"
        correct_answer = director_name
        
        # Generate multiple choices options
        options = set()
        options.add(correct_answer)
        while len(options) < 4:
            random_director = np.random.choice(data['primaryName'].unique())
            options.add(random_director)
        
        options = list(options)
        np.random.shuffle(options)
        
        return question, options, correct_answer
        