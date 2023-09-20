"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# Import the lasagna module. Note: Make sure lasagna.py is in the same directory.
import lasagna

# Constants for expected bake time and preparation time
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 90

def bake_time_remaining(time):
    """Calculate the bake time remaining.

    :param time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    This function takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    # Print statements for testing purposes
    print(lasagna.EXPECTED_BAKE_TIME)
    print(lasagna.preparation_time_in_minutes(4))
    return EXPECTED_BAKE_TIME - time

# TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here if you have it defined.

def preparation_time_in_minutes(layers, time_per_layer=2):
    """Calculate the preparation time in minutes.

    :param layers: int - the number of layers in the lasagna.
    :param time_per_layer: int - the time it takes to prepare each layer in minutes (default is 2 minutes per layer).
    :return: int - total preparation time in minutes.

    This function calculates the total preparation time for making lasagna
    based on the number of layers and the time it takes to prepare each layer.
    """
    return layers * time_per_layer

# TODO: Define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining).
def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time in minutes.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    preparation_time = preparation_time_in_minutes(layers)
    return preparation_time + elapsed_bake_time
