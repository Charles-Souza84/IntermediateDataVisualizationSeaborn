import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""
Building a FacetGrid
Seaborn's FacetGrid is the foundation for building data-aware grids. A data-aware grid allows you to create a series of 
small plots that can be useful for understanding complex data relationships.

For these exercises, we will continue to look at the College Scorecard Data from the US Department of Education. This rich 
dataset has many interesting data elements that we can plot with Seaborn.

When building a FacetGrid, there are two steps:

Create a FacetGrid object with columns, rows, or hue.
Map individual plots to the grid.
"""

# Read in the DataFrame
df = pd.read_csv("college_datav3.csv")

# Create FacetGrid with Degree_Type and specify the order of the rows using row_order
g2 = sns.FacetGrid(df, 
             row="Degree_Type",
             row_order=['Graduate', 'Bachelors', 'Associates', 'Certificate'])

# Map a pointplot of SAT_AVG_ALL onto the grid
g2.map(sns.pointplot, 'SAT_AVG_ALL')

# Show the plot
plt.show()
plt.clf()   

"""
Using a catplot

In many cases, Seaborn's catplot() can be a simpler way to create a FacetGrid. Instead of creating a grid and mapping the plot, 
we can use the catplot() to create a plot with one line of code.

For this exercise, we will recreate one of the plots from the previous exercise using catplot() and show how to create 
a boxplot on a data-aware grid.
"""

# Create a factor plot that contains boxplots of Tuition values
sns.catplot(data=df,
         x='Tuition',
         kind='box',
         row='Degree_Type')

plt.show()
plt.clf()

# Create a facetted pointplot of Average SAT_AVG_ALL scores facetted by Degree Type 
sns.catplot(data=df,
        x='SAT_AVG_ALL',
        kind='point',
        row='Degree_Type',
        row_order=['Graduate', 'Bachelors', 'Associates', 'Certificate'])

plt.show()
plt.clf()

"""
Using a lmplot

The lmplot is used to plot scatter plots with regression lines on FacetGrid objects. The API is similar to catplot 
with the difference that the default behavior of lmplot is to plot regression lines.

For the first set of exercises, we will look at the Undergraduate population (UG) and compare it to the percentage of students
 receiving Pell Grants (PCTPELL).

For the second lmplot exercise, we can look at the relationships between Average SAT scores and Tuition across the different 
degree types and public vs. non-profit schools.
"""

# Lists used in col_order argument
degree_ord = ['Graduate', 'Bachelors', 'Associates']
int_ord = ['Public', 'Private non-profit']

# Create a FacetGrid varying by column and columns ordered with the degree_order variable
g = sns.FacetGrid(df, col="Degree_Type", col_order=degree_ord)

# Map a scatter plot of Undergrad Population compared to PCTPELL
g.map(plt.scatter, 'UG', 'PCTPELL')

plt.show()
plt.clf()

# Re-create the previous plot as an lmplot
sns.lmplot(data=df,
        x='UG',
        y='PCTPELL',
        col="Degree_Type",
        col_order= degree_ord)

plt.show()
plt.clf()

# Create an lmplot that has a column for Ownership, a row for Degree_Type and hue based on the WOMENONLY column
sns.lmplot(data=df,
        x='SAT_AVG_ALL',
        y='Tuition',
        col="Ownership",
        row='Degree_Type',
        row_order=['Graduate', 'Bachelors'],
        hue='WOMENONLY',
        col_order=inst_ord)

plt.show()
plt.clf()

"""
Building a PairGrid
When exploring a dataset, one of the earliest tasks is exploring the relationship between pairs of variables. 
This step is normally a precursor to additional investigation.

Seaborn supports this pair-wise analysis using the PairGrid. In this exercise, we will look at the Car Insurance Premium 
data we analyzed in Chapter 1. All data is available in the df variable.
"""

