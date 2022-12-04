# import all modules
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# This first step in most data analysis is to import pandas and seaborn and read a data file 
# in order to analyze it further.

# Read in the DataFrame
df = pd.read_csv("schoolimprovement2010grants.csv")

"""
Comparing a histogram and displot

The pandas library supports simple plotting of data, which is very convenient when data is already 
likely to be in a pandas DataFrame.

Seaborn generally does more statistical analysis on data and can provide more sophisticated 
insight into the data.
"""

# Pandas histogram vs seaborn displot

# Display pandas histogram
df['Award_Amount'].plot.hist()
plt.show()

# Clear out the pandas histogram
plt.clf()

# Display a Seaborn displot
sns.displot(df['Award_Amount'])
plt.show()

# Clear the displot
plt.clf()

"""
Plot a histogram

The displot() function will return a histogram by default. The displot() can also create a KDE 
or rug plot which are useful ways to look at the data. Seaborn can also combine these plots 
so you can perform more meaningful analysis.
"""

# Create a displot
sns.displot(df['Award_Amount'],
             bins=20)

# Display the plot
plt.show()

"""
Rug plot and kde shading

Now that you understand some function arguments for displot(), we can continue further 
refining the output. This process of creating a visualization and updating it in an incremental 
fashion is a useful and common approach to look at data from multiple perspectives.

Seaborn excels at making this process simple.
"""

# Create a displot of the Award Amount
sns.displot(df['Award_Amount'],
             kind='kde',
             rug=True,
             fill=True)

# Plot the results
plt.show()

"""
Create a regression plot
For this set of exercises, we will be looking at FiveThirtyEight's data on which US State has the worst drivers. 
The data set includes summary level information about fatal accidents as well as insurance premiums for each state as of 2010.

In this exercise, we will look at the difference between the regression plotting functions.
"""

# Read in DataFrame
df = pd.read_csv("insurance_premiums.csv")

# Create a regression plot of premiums vs. insurance_losses
sns.regplot(data = df, x="insurance_losses", y="premiums")

# Display the plot
plt.show()

# Create an lmplot of premiums vs. insurance_losses
sns.lmplot(data = df, x="insurance_losses", y="premiums")

# Display the second plot
plt.show()

"""
Plotting multiple variables

Since we are using lmplot() now, we can look at the more complex interactions of data. This data set includes geographic information
by state and area. It might be interesting to see if there is a difference in relationships based on the Region of the country.
"""

# Create a regression plot using hue - creates multiple lines on the same graphic with labels for each color
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           hue="Region")

# Show the results
plt.show()

"""
Facetting multiple regressions

lmplot() allows us to facet the data across multiple rows and columns. In the previous plot, the multiple lines 
were difficult to read in one plot. We can try creating multiple plots by Region to see if that is a more useful visualization.

The lmplot function supports plotting regression data by column, row and hue. This concept is used repeatedly throughout Seaborn.
"""

# Create a regression plot with multiple rows - displays the plots across multiple rows
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           row="Region")

# Show the plot
plt.show()