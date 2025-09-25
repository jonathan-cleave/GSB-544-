
# %% [markdown]
# # Data Visualization Using `plotnine`
# 
# Github Repository: <https://github.com/jonathan-cleave/GSB-544->

# The Palmer Penguins dataset had a variety of column types with which to explore some nice visualizations. The `mtcars` dataset is another popular dataset for doing some simple data work, but does not contain the same types of variables.
# 
# Run the following code to load the `mtcars` dataset and explore the observations and variables contained within. To learn more about this dataset check out [this site](https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/mtcars.html)


# %%
import statsmodels.api as sm
import pandas as pd

mtcars = sm.datasets.get_rdataset("mtcars", "datasets", cache=True).data
df = pd.DataFrame(mtcars)

# %%
df

# %% [markdown]
# The statement "the `mtcars` dataset does not contain the same types of variables as the penguins dataset" is a little true and a little false. There are no variables that contain text values, BUT there are variables that it makes sense to consider categorical variables. In most situations, it makes sense to treat the values of categorical variables as text values instead of numeric values.
# 
# Use the `astype()` method to convert the categorical variables of the `mtcars` (df) dataset to have text values in the code chunk below. We've done one for you!

# %%
df["am"] = df["am"].astype(str)

# Convert the other variables below
df["cyl"] = df["cyl"].astype(str)
df["gear"] = df["gear"].astype(str)
df["carb"] = df["carb"].astype(str)

# %% [markdown]
# If you print out your new dataset, is it clear that the variables have been converted to text values? If so, how can you tell?
# 
# It should also be clear by how `plotnine` treats these variables.
# 
# 1. Create side-by-side boxplots of the `mpg` variable by the different values of the `am` variable. What happens if you convert the `am` variable back to float values and then try to create this same plot? Explain the differences between the two plots.
# 
# 2. Create overlaid histograms of the `hp` variable for the different values of the `cyl` variable. What happens if you convert the `cyl` variable back to float values and then try to create this same plot? Explain the differences between the two plots.

# %%
# Create plot for (1) here
from plotnine import ggplot, geom_point, aes, geom_boxplot
(ggplot(df, aes(x = "am", y = "mpg"))
+ geom_boxplot()
)

# %%
# Create plot for (2) here
from plotnine import geom_histogram
(ggplot(df,
aes(
  x = "hp",
  fill = "cyl"
))
+ geom_histogram()
)

# %% [markdown]
# Some of these variables, like the `cyl` variable, have numeric values that actually make sense as numbers (i.e. the number of cylinders in the engine). However, it doesn't make the most sense to "do math" with this type of variable (e.g. take averages and such) because there are so few different value this can take on AND they're an explicit choice made by the car manufacturer. So, it makes more sense to treat the `cyl` variable as a categorical variable despite it having numeric values.
# 
# You will need to keep these kinds of nuances about data in mind as you work with an increasing variety and richness of data, and do more complex things with them.
# 
# Choose 3 new `geometries` from the [data-to-viz website](https://www.data-to-viz.com/) for graphs that you'd like to explore using the `mtcars` dataset, and then create those graphs!

# %%
# Create plot with first new geometry here
(ggplot(df,
aes(
  x = "hp",
  y = "mpg",
  fill = "gear"
))
+ geom_boxplot()
)

# %%
# Create plot with second new geometry here
import matplotlib.pyplot as plt
import pandas as pd

# Ensure the columns are numerical
df['drat'] = pd.to_numeric(df['drat'])
df['qsec'] = pd.to_numeric(df['qsec'])
df['wt'] = pd.to_numeric(df['wt'])

plt.stackplot(df.index.values, df["drat"], df["qsec"], df["wt"], labels=['drat','qsec','wt'])
plt.legend(loc='upper left')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# %%
# Create plot with third new geometry here
import matplotlib.pyplot as plt
import seaborn as sns

# use the scatterplot function to build the bubble map
sns.scatterplot(data=df, x="disp", y="hp", size="cyl",color="#68B0AB", legend=False, sizes=(100, 2000))

# show the graph
plt.show()




