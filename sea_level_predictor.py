import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data', color='blue')

    # Create first line of best fit
    result_full = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_full = pd.Series([i for i in range(1880, 2051)])
    y_full = result_full.slope * x_full + result_full.intercept
    plt.plot(x_full, y_full, 'r', label='Fit Line 1880-2050', color='red')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    result_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = pd.Series([i for i in range(2000, 2051)])
    y_recent = result_recent.slope * x_recent + result_recent.intercept
    plt.plot(x_recent, y_recent, 'g', label='Fit Line 2000-2050', color='green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# Example usage
if __name__ == "__main__":
    draw_plot()
