import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import plotly.express as px
import statsmodels.api as sm
from scipy import stats

#Author: Nadir Shahzad Khan

def rda_logreg():
    """
    Reads in World Bank data and does regression discontinuity analysis to pre- and post-treatment
    data. Creates a scatter plot of Log Commitment Amount vs. Year with separate trendlines
    for the pre- and post-treatment periods.

    Returns
    None. Creates Regression Plot
    """
    df = pd.read_csv('project_tracker/data/ll_wb.csv')
    
    # Drop rows with negative or zero 'Commitment_Amount'
    df = df[df['Commitment Amount'] > 0]

    # Convert Commitment_Amount to log10
    df['Commitment Amount'] = np.log10(df['Commitment Amount'])

    cutoff_year = 2017
    df['Post_2017'] = df['Year'] >= 2017
    treatment = df.loc[df['Year'] >= cutoff_year].copy()
    control = df.loc[df['Year'] < cutoff_year].copy()

    # Create the treatment and control variables
    treatment.loc[:, 'Treatment'] = 1
    control.loc[:, 'Treatment'] = 0

    treatment_model = LinearRegression().fit(treatment[['Year']], treatment['Commitment Amount'])
    control_model = LinearRegression().fit(control[['Year']], control['Commitment Amount'])

    treatment_effect = treatment_model.coef_[0]

    fig = px.scatter(df, x='Year', y='Commitment Amount', color='Post_2017')

    fig.update_yaxes(tickformat='.1e', ticksuffix='M')
        
    fig.add_trace(px.scatter(treatment, x='Year', y='Commitment Amount',
                            color_discrete_sequence=['grey'],
                            trendline='ols', trendline_color_override='grey').data[1])
    fig.add_trace(px.scatter(control, x='Year', y='Commitment Amount',
                            color_discrete_sequence=['blue'],
                            trendline='ols', trendline_color_override='blue').data[1])
    

    treatment_r_squared = treatment_model.score(treatment[['Year']], treatment['Commitment Amount'])
    control_r_squared = control_model.score(control[['Year']], control['Commitment Amount'])

    # Calculate the treatment effect and its standard error using statsmodels
    treatment_model = sm.OLS(treatment['Commitment Amount'], sm.add_constant(treatment['Year'])).fit()
    treatment_effect = treatment_model.params['Year']
    treatment_effect_se = treatment_model.bse['Year']

    # Calculate the t-statistic and p-value for the treatment effect using statsmodels
    t_stat = treatment_effect / treatment_effect_se
    p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=treatment_model.df_resid))

    annotations = []
    annotations.append(dict(x=1.0, y=0.9,
                            xref='paper', yref='paper',
                            text='Treatment effect estimate: {:.4f}'.format(treatment_effect),
                            showarrow=False,
                            bgcolor="white"))

    annotations.append(dict(x=1.0, y=0.85,
                            xref='paper', yref='paper',
                            text='t-statistic: {:.4f}'.format(t_stat),
                            showarrow=False,
                            bgcolor="white"))
                            

    annotations.append(dict(x=1.0, y=0.80,
                            xref='paper', yref='paper',
                            text='p-value: {:.4f}'.format(p_value),
                            showarrow=False,
                            bgcolor="white"))
    fig.update_layout(annotations=annotations)
    return fig

def rda_linearreg():
    """
    Reads in World Bank data and does regression discontinuity analysis to pre- and post-treatment
    data. Creates a scatter plot of Commitment Amount vs. Year with separate trendlines
    for the pre- and post-treatment periods.

    Returns
    None. Creates Regression Plot
    """
    df = pd.read_csv('project_tracker/data/ll_wb.csv')
    
    cutoff_year = 2017
    df['Post_2017'] = df['Year'] >= 2017

    treatment = df.loc[df['Year'] >= cutoff_year].copy()
    control = df.loc[df['Year'] < cutoff_year].copy()

    # Create the treatment and control variables
    treatment.loc[:, 'Treatment'] = 1
    control.loc[:, 'Treatment'] = 0

    # Convert Commitment_Amount to millions of dollars
    df['Commitment Amount'] = df['Commitment Amount'] / 1000000
    
    treatment_model = LinearRegression().fit(treatment[['Year']], treatment['Commitment Amount'])
    control_model = LinearRegression().fit(control[['Year']], control['Commitment Amount'])

    treatment_effect = treatment_model.coef_[0]

    fig = px.scatter(df, x='Year', y='Commitment Amount', color='Post_2017')
    
    fig.update_yaxes(tickprefix='$', ticksuffix='M')
    
    fig.add_trace(px.scatter(treatment, x='Year', y='Commitment Amount',
                              color_discrete_sequence=['grey'],
                              trendline='ols', trendline_color_override='grey').data[1])
    fig.add_trace(px.scatter(control, x='Year', y='Commitment Amount',
                              color_discrete_sequence=['blue'],
                              trendline='ols', trendline_color_override='blue').data[1])

    treatment_r_squared = treatment_model.score(treatment[['Year']], treatment['Commitment Amount'])
    control_r_squared = control_model.score(control[['Year']], control['Commitment Amount'])

    treatment_model = sm.OLS(treatment['Commitment Amount'], sm.add_constant(treatment['Year'])).fit()
    treatment_effect = treatment_model.params['Year']
    treatment_effect_se = treatment_model.bse['Year']

    # Calculate the t-statistic and p-value for the treatment effect using statsmodels
    t_stat = treatment_effect / treatment_effect_se
    p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=treatment_model.df_resid))

    # Create the annotations
    annotations = []

    annotations.append(dict(x=1.0, y=0.9,
                            xref='paper', yref='paper',
                            text='Treatment effect estimate: {:.4f}'.format(treatment_effect),
                            showarrow=False,
                            bgcolor="white"))

    annotations.append(dict(x=1.0, y=0.85,
                            xref='paper', yref='paper',
                            text='t-statistic: {:.4f}'.format(t_stat),
                            showarrow=False,
                            bgcolor="white"))

    annotations.append(dict(x=1.0, y=0.80,
                            xref='paper', yref='paper',
                            text='p-value: {:.4f}'.format(p_value),
                            showarrow=False,
                            bgcolor="white"))

    fig.update_layout(annotations=annotations)
    return fig


def hist_data():
    """
    Reads in World Bank project data from a CSV file, converts the commitment amounts to 
    log millions of dollars, and creates a histogram of the distribution of 
    commitment amounts using the Plotly library.

    Returns:
    None. Creates histogram
    """

    df = pd.read_csv('project_tracker/data/ll_wb.csv')

    # Convert Commitment_Amount to millions of dollars
    df['Commitment Amount'] = df['Commitment Amount'] / 1000000
    df['Commitment Amount'] = np.log10(df['Commitment Amount'])

    fig = px.histogram(df, x='Commitment Amount', nbins=20, histnorm='probability',
                       title='Commitment Amount Distribution (Overall)')
    fig.update_yaxes(title='Percentage', tickformat='.05%', range=[0, .35])
    fig.update_xaxes(title='Commitment Amount (Millions of Dollars)')
    return fig
