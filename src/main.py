import numpy as np
import pandas as pd
import doubleml as dml
from doubleml.datasets import fetch_401K

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LassoCV, LogisticRegressionCV
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

from xgboost import XGBClassifier, XGBRegressor

import matplotlib.pyplot as plt
import seaborn as sns

data = fetch_401K(return_type='DataFrame')

# Setting up basic model
features_base = ["age", "inc", "educ", "fsize", 
                 "marr", "twoearn", "db", "hown"]

# Initialize DoubleMLData backend for model with basic features
data_dml_base = dml.DoubleMLData(data, y_col="net_tfa",
                                 d_cols="e401",
                                 x_cols=features_base)

print(data_dml_base)

# Setting up flexible model
features = data.copy()[['marr', 'twoearn', 'db', 'pira', 'hown']]

# Choosing degree for polynomial terms. Still includes orignal degree 1 term
poly_dict = {'age': 2,
             'inc': 2,
             'educ': 2,
             'fsize': 2
             }


# Iterating through each of the above
for key, degree in poly_dict.items():

    # Generating the polynomial feature object
    poly = PolynomialFeatures(degree, include_bias=False)

    # Using the object to transform this column
    data_transf = poly.fit_transform(data[[key]])

    # Gets the name of the generated column
    x_cols = poly.get_feature_names_out([key])

    # New dataframe with the transformed column
    data_transf = pd.DataFrame(data_transf, columns=x_cols)

    # Joining back to features dataframe
    features = pd.concat([features, data_transf], axis=1)

# Combining features with treatment and outcome columns
model_data = pd.concat((data.copy()[['net_tfa', 'e401']], 
                        features.copy()),
                        axis=1, sort=False)

# Initialize DoubleMLData backend for model with flexible features
data_dml_flex = dml.DoubleMLData(model_data,
                                 y_col='net_tfa',
                                 d_cols='e401')

