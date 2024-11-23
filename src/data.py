""" Manages and imports movie data from a CSV file """

import os
import pandas as pd

class MoviesData:
    """ 
    A class for managing and importing movie data from a CSV file.

    Parameters:
    ----------
    path : str
        The folder path where the movie data file is stored.
    """
    # Initializes the MoviesData instance with the specified folder path.
    def __init__(self, path):
        self.path = os.path.join(path, "")

    # Read a CSV file using pandas and returns it as a DataFrame.
    def import_data(self, file_path):
        df = pd.read_csv(file_path, sep=",")
        return df
    
