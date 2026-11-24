import pandas as pd
import numpy as np

series = pd.Series([10, 20, 30, 20, np.nan]) # Creates the series. 

print(series) # Prints the series. 

# Finds the sum, mean, maximum value, and minimum value in the series. 
print(f"Sum: {series.sum()}")
print(f"Mean: {series.mean()}")
print(f"Maximum: {series.max()}")
print(f"Minimum: {series.min()}")

print(series.head(3)) # Prints the first 3 values in the series. 

print(series.isnull()) # Finds any missing values. 
series = series.fillna(0) # Replaces missing values with 0.
print(series) # Prints the new series with the missing values replaced with 0.

print(series.sort_values()) # Sorts the values from lowest to highest. 

print(series.value_counts()) # Counts how many of each value is in the series. 