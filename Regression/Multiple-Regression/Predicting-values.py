import pandas
from sklearn import linear_model


# Read the csv file
df = pandas.read_csv('car_data.csv')

# Create the independent and dependent variables
X = df[['Weight', 'Volume']]
y = df['CO2']

# Creates the linear regression object
regr = linear_model.LinearRegression()
# Fits it with the two x and y parameters
regr.fit(X, y)

# Predict the CO2 emission of a car where the weight is 2300 kg, and the volume is 1300cm3
predictedCO2 = regr.predict([[2300, 1300]])

# Prints the predicted CO2 value
print(predictedCO2)
