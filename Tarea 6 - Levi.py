import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(url, header=None)
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Compute the correlation matrix
corr = iris.corr()

# Plot the correlation matrix
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')

# Perform feature selection based on correlation
threshold = 0.5
corr_features = set()
for i in range(len(corr.columns)):
    for j in range(i):
        if abs(corr.iloc[i, j]) > threshold:
            corr_features.add(corr.columns[i])

print('Selected features:', list(corr_features))

# Create a new dataframe with the selected features
selected_features_df = iris[list(corr_features)]

# Display the new dataframe
print('\nNew dataframe with selected features:')
print(selected_features_df.head())

import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_classif

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(url, header=None)
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Separate features and target variable
X = iris.iloc[:, :-1]  # features
y = iris.iloc[:, -1]   # target variable

# Apply mutual information feature selection
k = 2  # number of top features to select
selector = SelectKBest(mutual_info_classif, k=k)
selector.fit(X, y)

# Get the selected features
selected_features = X.columns[selector.get_support()]

print('Selected features:', list(selected_features))

import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_classif

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(url, header=None)
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Separate features and target variable
X = iris.iloc[:, :-1]  # features
y = iris.iloc[:, -1]   # target variable

# Apply mutual information feature selection
k = 2  # number of top features to select
selector = SelectKBest(mutual_info_classif, k=k)
selector.fit(X, y)

# Get the selected features
selected_features = X.columns[selector.get_support()]

print('Selected features:', list(selected_features))

import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(url, header=None)
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Separate features and target variable
X = iris.iloc[:, :-1]  # features
y = iris.iloc[:, -1]   # target variable

# Apply recursive feature elimination
n_features = 2  # number of features to select
estimator = LogisticRegression()
selector = RFE(estimator, n_features_to_select=n_features)
selector = selector.fit(X, y)

# Get the selected features
selected_features = X.columns[selector.support_]

print('Selected features:', list(selected_features))

import pandas as pd
from sklearn.feature_selection import f_regression
from sklearn.linear_model import LinearRegression

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
housing = pd.read_csv(url, sep='\s+', header=None)
housing.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
                   'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# Separate features and target variable
X = housing.iloc[:, :-1]  # features
y = housing.iloc[:, -1]   # target variable

# Perform forward feature selection
n_features = 5  # number of features to select
estimator = LinearRegression()
selected_features = set()

for i in range(n_features):
    best_score = 0
    best_feature = None
    
    for feature in X.columns:
        if feature not in selected_features:
            selected_features.add(feature)
            X_selected = X[list(selected_features)]
            scores, _ = f_regression(X_selected, y)
            score = scores.mean()
            
            if score > best_score:
                best_score = score
                best_feature = feature
                
            selected_features.remove(feature)
            
    selected_features.add(best_feature)

print('Selected features:', list(selected_features))

import pandas as pd
from sklearn.feature_selection import f_regression
from sklearn.linear_model import LinearRegression

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
housing = pd.read_csv(url, sep='\s+', header=None)
housing.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
                   'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# Separate features and target variable
X = housing.iloc[:, :-1]  # features
y = housing.iloc[:, -1]   # target variable

# Perform backward feature elimination
n_features = 5  # number of features to select
estimator = LinearRegression()
selected_features = set(X.columns)

while len(selected_features) > n_features:
    worst_score = float('inf')
    worst_feature = None
    
    for feature in selected_features:
        selected_features.remove(feature)
        X_selected = X[list(selected_features)]
        scores, _ = f_regression(X_selected, y)
        score = scores.mean()
        
        if score < worst_score:
            worst_score = score
            worst_feature = feature
                
        selected_features.add(feature)
            
    selected_features.remove(worst_feature)

print('Selected features:', list(selected_features))

import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
housing = pd.read_csv(url, sep='\s+', header=None)
housing.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
                   'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# Separate features and target variable
X = housing.iloc[:, :-1]  # features
y = housing.iloc[:, -1]   # target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Fit the LASSO regression model
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)

# Print the coefficients of the features
coef = pd.Series(lasso.coef_, index=X.columns)
print('Selected features:\n', coef[coef != 0])

import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
housing = pd.read_csv(url, sep='\s+', header=None)
housing.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
                   'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# Separate features and target variable
X = housing.iloc[:, :-1]  # features
y = housing.iloc[:, -1]   # target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Fit the Ridge regression model
ridge = Ridge(alpha=0.1)
ridge.fit(X_train, y_train)

# Print the coefficients of the features
coef = pd.Series(ridge.coef_, index=X.columns)
print('Selected features:\n', coef)

import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(url, header=None)
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Separate features and target variable
X = housing.iloc[:, :-1]  # features
y = housing.iloc[:, -1]   # target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Fit the LASSO regression model
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)

# Print the coefficients of the features
coef = pd.Series(lasso.coef_, index=X.columns)
print('Selected features:\n', coef[coef != 0])

import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split

# Load the dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(url, header=None)
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Separate features and target variable
X = housing.iloc[:, :-1]  # features
y = housing.iloc[:, -1]   # target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Fit the LASSO regression model
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)

# Print the coefficients of the features
coef = pd.Series(lasso.coef_, index=X.columns)
print('Selected features:\n', coef[coef != 0])