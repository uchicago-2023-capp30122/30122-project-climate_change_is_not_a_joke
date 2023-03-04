import pandas as pd
from rdd import rdd

data_path = 'data/wb_data.csv'

# load your data into a pandas dataframe
df = pd.read_csv(data_path)

# define the cutoff variable
cutoff = 2017

# create a RDD object
rdd_object = rdd(df['Commitment_Amount'], df['year'], cutoff=cutoff, order=1)

# estimate the local linear regression model
results = rdd_object.fit()

# print the treatment effect
print('Estimated treatment effect:', results.params['Treated'])