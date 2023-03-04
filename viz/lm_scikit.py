import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import plotly.express as px

def scikit_example():
    """
    """
    df = pd.read_csv('../data/wb_data.csv')
    # Define the cutoff year
    cutoff_year = 2017

    # Split the data into treatment and control groups
    treatment = df.loc[df['Year'] >= cutoff_year].copy()
    control = df.loc[df['Year'] < cutoff_year].copy()

    # Create the treatment and control variables
    treatment.loc[:, 'Treatment'] = 1
    control.loc[:, 'Treatment'] = 0

    # Combine the treatment and control groups
    data = pd.concat([treatment, control])

    # Fit the regression model using scikit-learn
    X = data[['Year', 'Treatment']]
    y = data['Commitment_Amount']
    model = LinearRegression().fit(X, y)

    # Print the treatment effect estimate
    treatment_effect = model.coef_[1]
    print('Treatment effect estimate:', treatment_effect)

    # Create the scatter plot and fitted line using Plotly Express
    fig = px.scatter(data, x='Year', y='Commitment_Amount', color='Treatment',
                    trendline='ols', trendline_color_override='blue')
    fig.show()

    # Print the R-squared value
    r_squared = model.score(X, y)
    print('R-squared:', r_squared)

# scikit_example()





