""" 
Generate random movie quiz questions with multiple-choice answers
"""

import numpy as np

class Quiz:
    """
        A class for generating random questions, with four options, one of which 
        is correct. Return the question, the correct answer and the options.
        
        Parameters
        ----------
        data : pandas.DataFrame
        A DataFrame containing the movie dataset
    """
    def __init__(self, data):
        """
        Initializes the Quiz class with the given dataset.
        """
        self.data = data
  
    def generate_question(self, difficulty='easy'):
        """
            Generates a random quiz question based on the specified difficulty level.
        """
        # Filter movies based on the difficulty level
        if difficulty == 'easy':
            filter_data = self.data[self.data['averageRating'] >= 7.5]
        elif difficulty == 'medium':
            filter_data = self.data[(self.data['averageRating'] >= 4.5) & (self.data['averageRating'] < 7.5)]
        else:
            filter_data = self.data[self.data['averageRating'] < 4.5]
        
        # Create a list of question type
        question_types = [
            self.question_year,
            self.question_director,
            self.question_actor
        ]
        
        # Select a random question type and call it
        question_func = np.random.choice(question_types)
        return question_func(filter_data)
    
    def question_year(self, data):
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
        # Filter the data to include only rows where the person is a director
        director_data = data[data['category'] == 'director']
        
        # Choose a random movie and select the title and the name of the director
        question_row = director_data.sample(1).iloc[0]
        primary_title = question_row['primaryTitle']
        director_name = question_row['primaryName']

        # Create the question string using the selected movie's title
        question = f"Who is the director of the movie '{primary_title}'?"
        correct_answer = director_name
        
        # Generate multiple choices options
        options = set()
        options.add(correct_answer)
        while len(options) < 4:
            random_director = np.random.choice(director_data['primaryName'].unique())
            options.add(random_director)
        
        # Convert the set option to a list and shuffle it
        options = list(options)
        np.random.shuffle(options)
        
        return question, options, correct_answer
    
    def question_actor(self, data):
        """
            Generates a question asking who starred in a randomly chosen movie.
        """
        # Filter the data to include only rows where the person is an actor/actress
        actor_data = data[data['category'].isin(['actor', 'actress'])]
        
        # Choose a random movie and select the title and the name of the actor/actress
        question_row = actor_data.sample(1).iloc[0]
        primary_title = question_row['primaryTitle']
        actor_name = question_row['primaryName']

        question = f"Who is one of the main actors in the movie '{primary_title}'?"
        correct_answer = actor_name
        
        # Generate multiple choices options
        options = set()
        options.add(correct_answer)
        while len(options) < 4:
            random_actor = np.random.choice(actor_data['primaryName'].unique())
            options.add(random_actor)
       
        # Convert the set option to a list and shuffle it
        options = list(options)
        np.random.shuffle(options)
        
        return question, options, correct_answer
        