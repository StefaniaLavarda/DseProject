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
        # choose a random movie and select, from the df, the title and year of the movie
        question_row = data.sample(1)
        primary_title = question_row['primaryTitle'].value[0]
        start_year = question_row['startYear'].value[0]

        # create the question string using the selected movie's title
        question = f"What year was the movie {primary_title} released?"
        correct_answer = start_year
       
        # generate multiple choices options
        options = set()
        options.add(correct_answer)
        while len(options) < 4:
            random_year = np.random.choice(range(1894, 2024))
            options.add(random_year)
        
        return question, list(options), correct_answer