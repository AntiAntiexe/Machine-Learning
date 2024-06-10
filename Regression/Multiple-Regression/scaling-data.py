import pandas
from sklearn.preprocessing import StandardScaler

# Assign the standard scaler to a variable for ease of use
scale = StandardScaler()


# Read the csv file
df = pandas.read_csv('car_data2.csv')


# Define the indepedent variable or the variables you want to scale
X = df[['Weight', 'Volume']]


# Scale the data
scaledX = scale.fit_transform(X)


# Print the scaled data
print(scaledX)
