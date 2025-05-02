# stats_calculator.py

import numpy as np
from scipy import stats

def calculate_mean(data):
    """Function to calculate the mean"""
    return np.mean(data)

def calculate_median(data):
    """Function to calculate the median"""
    return np.median(data)

def calculate_mode(data):
    """Function to calculate the mode"""
    return stats.mode(data).mode[0]

def calculate_variance(data):
    """Function to calculate the variance"""
    return np.var(data)

def calculate_standard_deviation(data):
    """Function to calculate the standard deviation"""
    return np.std(data)

def display_statistics(data):
    """Display all calculated statistics"""
    print("\nStatistics for the provided data:")
    print(f"Mean: {calculate_mean(data)}")
    print(f"Median: {calculate_median(data)}")
    print(f"Mode: {calculate_mode(data)}")
    print(f"Variance: {calculate_variance(data)}")
    print(f"Standard Deviation: {calculate_standard_deviation(data)}")

def main():
    print("Welcome to the Basic Statistics Calculator!")
    
    # Getting input from the user
    while True:
        try:
            data_input = input("\nPlease enter a list of numbers (separated by commas): ")
            data = [float(x.strip()) for x in data_input.split(',')]
            break
        except ValueError:
            print("Invalid input. Please enter a valid list of numbers.")
    
    # Displaying statistics
    display_statistics(data)

if __name__ == "__main__":
    main()
