import numpy as np
import csv

def read_input(filename):
    """
    This function reads in the text input for each puzzle and returns a numpy array
    """
    lines = []
    with open(f'../inputs/{filename}.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            lines.append(int(row[0]))
    return lines