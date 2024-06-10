import numpy
import matplotlib.pyplot as plt

# Creates data set of 100000 floats with a mean value of 5.0 and a standard deviation is 1.0.
data = numpy.random.normal(loc=5.0, scale=1.0, size=100000)

plt.hist(data, bins=100)  # Creates histogram with 100 bars

plt.show()  # Displays the histogram
