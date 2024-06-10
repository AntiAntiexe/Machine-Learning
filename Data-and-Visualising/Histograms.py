import numpy
import matplotlib.pyplot as plt

data = numpy.random.uniform(low=0.0, high=5.0, size=250)  # Creates data set of 250 floats from 0.0 to 5.0.

plt.hist(data, bins=5)  # Creates histogram with 5 bars
plt.show()  # Displays the histogram
