import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
   import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv ("epa-sea-level.csv")


    # Create scatter plot
    plt.scatter (df['Year'], df['CISRO Adjusted Sea Level'])
    plt.xlabel ('Year') #x axis label
    plt.ylabel ('CISRO Adjusted Sea Level (inches)') #y axis label
    plt.title ('Year vs CISRO Adjusted Sea Level') #Title of the plot

    plt.show()

    #linear regression
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    #Predict values from the first year in the dataset till 2050
    years_extended = range(df["Year"].min(),2051)
    line_fit = intercept + slope*pd.series(years_extended)

    # Plot the line of the best fit
    plt.plot(years_extended, line_fit, 'r', label="Best Fit Line")

    #Sea level in 2050
    sea_level_2050 = slope * 2050 + intercept
    print(f"Predicted sea level in 2050: {sea_level_2050:.2f} inches")


    # Create first line of best fit
    # Scatter plot for all data
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], 
    label="All data", alpha=0.5)

    # Create second line of best fit
    # Scatter plot for data since 2000
    plt.scatter(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"], 
    label="Data since 2000", color="orange")


    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Show the plot
    plt.show()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()hg