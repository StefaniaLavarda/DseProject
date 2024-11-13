""" src/data.py """

import os
import pandas as pd

class MoviesData:
    """ A class for managing and importing movie data from a CSV file.

    Parameters:
    ----------
    path (str): 
        A path pointing to the folder in which the movie data file is stored .
    """
    # initializes the MoviesData instance with the given path.
    def __init__(self, path):
        self.path = os.path.join(path, "")

    # read a CSV file using pandas and returns it as a DataFrame.
    def import_data(self, file_path):
        df = pd.read_csv(file_path, sep=",")
        return df
    
