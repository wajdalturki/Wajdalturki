#########  Missing Values #########

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pip install matplotlib

plt.style.use("seaborn")

PATH = "./data/burritos.csv"

df = pd.read_csv(PATH, header=None)

df.info()
df.head()


#After:

PATH = "./data/burritos.csv"

df = pd.read_csv(PATH, header=None, na_values="?")

df.head()

df.head(2)

type(df.iloc[1,6])

df.isnull().sum().sort_values().plot(kind="barh", title="Missing Values ");


############# Mean #############
############ Q: Choose a column and replace NaN values with the mean ############

# -
# First Create Hist Plot to show columns 5
df[5].plot(kind="hist", bins=20, title="Histogram of Column 5");

# Then Calculate Variance before handling NaN values
df[5].var()

# Then Calculate mean 
c5_mean = df[5].mean()
c5_mean

# Replace NaN values with the mean:
df[5] = df[5].fillna(c5_mean)
df[5].isnull().sum()

# Create Hist plot after Handled NaN Values
 df[5].plot(kind="hist", bins=20, title="Histogram of Column 5 with Handled NaN Values");

# Variance after handling NaN values
df[5].var()


############# Median #############
############ Q: Choose a column and replace NaN values with the median ############

# -
# Imputing Median in column 8

# First Creatte a histogram plot
#with bins=20 to see distribution of data
df[8].plot(kind="hist", bins=20, title="Histogram of Column 8 without Handled NaN Values");

# Then Calculate median 
c8_median = df[8].median()
c8_median

# Replace NaN values with mode
df[8] = df[8].replace(np.NaN, c8_median)

# Create Hist plot after Handled NaN Values
# with bins=20 to see distribution of data
df[8].plot(kind="hist", bins=20, title="Histogram of Column 8 after Handled NaN Values");


############# Mode #############
############ Q: Choose a column and replace NaN values with the mode ############

# -
# Imputing Mode in column 19

# First Create Plot that shows column 19
df[19].plot(kind="hist", bins=20, title="Histogram of Column 19 before Handled NaN Values");

# Then Calculate mode
c19_mode = df[19].mode()[0]
c19_mode

# Replace NaN values after Calculated mode
df[19] = df[19].replace(np.NaN, 19_mode)

# Then Create hist After Handled NaN Values
# Plot a histogram with bins=20 to see distribution of data
df[19].plot(kind="hist", bins=20, title="Histogram of Column 19 After Handled NaN Values");



############# Choose a column and replace NaN values with your own value #############

# replace NaN values in Address with No Address
df["Address"].fillna("No Address", inplace = True)

df


#############  backwards filling #############
############ Q: Choose a column and use  backwards filling ############

# -
# Backward filling will use the next value if it is not a NaN value to replace the NaN value being replaced.
# Imputing Mode in column 23

# show a target column
df[23]

df[23].fillna(method="bfill")


############# forwards filling #############
############ Q: Choose a column and use forwards filling ############

# -

#Forward filling will use the previous value if it is not a NaN value to replace the NaN value being replaced. 

# Imputing Mode in column 23

# show a target column
df[23]

df[23].fillna(method="ffill")


########### Q: Determine how many missing values are present in each column ###########

# -
# Count total NaN at each column in a DataFrame

print(" \nCount total NaN at each column in a DataFrame : \n\n",
      df.isnull().sum())


########### Q:Determine the total amount of missing values ###########

#apply a count over the rows:
test_df.apply(lambda x: x.count(), axis=1)

# then add the result as a column:
test_df['full_count'] = test_df.apply(lambda x: x.count(), axis=1)
