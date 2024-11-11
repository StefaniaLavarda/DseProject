# src/quiz.py

class Quiz:
    """
       A class for generating random questions, with four options, one of which 
       is correct. Return the question, the correct answer and the options.
    """
    def __init__(self, data):
        self.data = data