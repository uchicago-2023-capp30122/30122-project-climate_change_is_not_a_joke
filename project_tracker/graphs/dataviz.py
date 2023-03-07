import pandas as pd
from rdd import rdd
import numpy as np
import matplotlib.pyplot as plt

def rdd_example():
    """
    """
    data = pd.read_csv('project_tracker/data/raw/wb_data.csv')
    cutoff_year = 2017
    data['treatment'] = np.where(data['Year'] >= cutoff_year, 1, 0)
    bandwidth_opt = rdd.optimal_bandwidth(data['Commitment Amount'], data['Year'], cut=cutoff_year)
    print("Optimal bandwidth:", bandwidth_opt)
    data_rdd = rdd.truncated_data(data, 'Year', bandwidth_opt, cut=cutoff_year)

    plt.figure(figsize=(12, 8))
    plt.scatter(data_rdd['Year'], data_rdd['Commitment Amount'], facecolors='none', edgecolors='r')
    plt.xlabel('Year')
    plt.ylabel('Commitment Amount')
    plt.axvline(x=cutoff_year, color='b')
    plt.savefig('rdd_plot.png')  # save plot to a separate file
    model = rdd.rdd(data_rdd, 'Year', 'Commitment Amount', cut=cutoff_year)
    print(model.fit().summary())
    
rdd_example()