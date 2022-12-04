import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read in the DataFrame
df = pd.read_csv("ushousing_urban.csv")
"""
Setting the default style

For these exercises, we will be looking at fair market rent values calculated by the 
US Housing and Urban Development Department. This data is used to calculate guidelines 
for several federal programs. The actual values for rents vary greatly across the US. 
We can use this data to get some experience with configuring Seaborn plots.
"""

# Plot the pandas histogram
df['fmr_2'].plot.hist()
plt.show()
plt.clf()

# Set the default seaborn style
sns.set()

# Plot the pandas histogram again
df['fmr_2'].plot.hist()
plt.show()
plt.clf()

"""
Comparing styles

Seaborn supports setting different styles that can control the aesthetics of the final plot. In this exercise, 
you will plot the same data in two different styles in order to see how the styles change the output.
"""

# Create a displot() of the fmr_2 column using a dark style 
sns.set_style('dark')
sns.displot(df['fmr_2'])
plt.show()
plt.clf()

# Create a displot() of the fmr_2 column using a dark style 
sns.set_style('whitegrid')
sns.displot(df['fmr_2'])
plt.show()
plt.clf()

"""
Removing spines

In general, visualizations should minimize extraneous markings so that the data speaks for itself. Seaborn 
allows you to remove the lines on the top, bottom, left and right axis, which are often called spines.
""" 

# Set the style to white
sns.set_style('white')

# Create a regression plot
sns.lmplot(data=df,
           x='pop2010',
           y='fmr_2')

# Remove the spines
sns.despine(top=True, right=True)

# Show the plot and clear the figure
plt.show()
plt.clf()

"""
Matplotlib color codes

Seaborn offers several options for modifying the colors of your visualizations. The simplest approach is to 
explicitly state the color of the plot. A quick way to change colors is to use the standard matplotlib color codes.
"""

# Set style, enable color code, and create a magenta displot
sns.set(color_codes=True)
sns.displot(df['fmr_3'], color='m')

# Show the plot
plt.show()

"""
Using default palettes

Seaborn includes several default palettes that can be easily applied to your plots. In this example, we will look at the 
impact of two different palettes on the same displot.
"""

# Loop through differences between bright and colorblind palettes
for p in ['bright', 'colorblind']:
    sns.set_palette(p)
    sns.displot(df['fmr_3'])
    plt.show()
    
    # Clear the plots    
    plt.clf()

"""
Creating Custom Palettes
Choosing a cohesive palette that works for your data can be time consuming. Fortunately, Seaborn provides the color_palette() 
function to create your own custom sequential, categorical, or diverging palettes. Seaborn also makes it easy to view your 
palettes by using the palplot() function.
"""
# create and display a Purples sequential palette containing 8 colors
sns.palplot(sns.color_palette("Purples", 8))
plt.show()

# create and display a palette with 10 colors using the husl system
sns.palplot(sns.color_palette('husl', 10))
plt.show()

# create and display a diverging palette with 6 colors coolwarm
sns.palplot(sns.color_palette("coolwarm", 6))
plt.show()
"""
Using matplotlib axes

Seaborn uses matplotlib as the underlying library for creating plots. Most of the time, you can use the Seaborn API 
to modify your visualizations but sometimes it is helpful to use matplotlib's functions to customize your plots. 
The most important object in this case is matplotlib's axes.

Once you have an axes object, you can perform a lot of customization of your plot.
"""
# Create a figure and axes
fig, ax = plt.subplots()

# Plot the distribution of data
sns.histplot(df['fmr_3'], ax=ax)

# Create a more descriptive x axis label
ax.set(xlabel="3 Bedroom Fair Market Rent")

# Show the plot
plt.show()
"""
Additional plot customizations

The matplotlib API supports many common customizations such as labeling axes, adding titles, and setting limits. 
"""

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the distribution of 1 bedroom rents
sns.histplot(df['fmr_1'], ax=ax)

# Modify the properties of the plot
ax.set(xlabel="1 Bedroom Fair Market Rent",
       xlim=(100,1500),
       title="US Rent")

# Display the plot
plt.show()

"""
Adding annotations

Each of the enhancements we have covered can be combined together. In the next exercise, we can annotate our distribution 
plot to include lines that show the mean and median rent prices.
"""
# Create a figure and axes. Then plot the data
fig, ax = plt.subplots()
sns.histplot(df['fmr_1'], ax=ax)

# Customize the labels and limits
ax.set(xlabel="1 Bedroom Fair Market Rent", xlim=(100,1500), title="US Rent")

# Add vertical lines for the median and mean
ax.axvline(x=df['fmr_1'].median(), color='m', label='Median', linestyle='--', linewidth=2)
ax.axvline(x=df['fmr_1'].mean(), color='b', label='Mean', linestyle='-', linewidth=2)

# Show the legend and plot the data
ax.legend()
plt.show()

"""
Multiple plots
For the final exercise we will plot a comparison of the fair market rents for 1-bedroom and 2-bedroom apartments.
"""
# Create a plot with 1 row and 2 columns that share the y axis label
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharey=True)

# Plot the distribution of 1 bedroom apartments on ax0
sns.histplot(df['fmr_1'], ax=ax0)
ax0.set(xlabel="1 Bedroom Fair Market Rent", xlim=(100,1500))

# Plot the distribution of 2 bedroom apartments on ax1
sns.histplot(df['fmr_2'], ax=ax1)
ax1.set(xlabel="2 Bedroom Fair Market Rent", xlim=(100,1500))

# Display the plot
plt.show()
