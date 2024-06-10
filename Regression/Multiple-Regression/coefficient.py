import pandas
from sklearn import linear_model

# Read the csv file
df = pandas.read_csv('car_data.csv')


# Create the independent and dependant variables
X = df[['Weight', 'Volume']]
y = df['CO2']


# Creates the linear regression object
regr = linear_model.LinearRegression()

# Fits it with the two x and y parameters
regr.fit(X, y)


# Prints the coefficient of the regression object
print(regr.coef_)
