import matplotlib.pyplot as plt
import numpy

x = numpy.random.normal(5.0, 1.0, 1000)
# Creates normal data distribution array with mean of 5.0 and a standard deviation of 1.0

y = numpy.random.normal(10.0, 2.0 , 1000)
# Creates normal data distribution array with mean of 10.0 and a standard deviation of 2.0

plt.scatter(x, y)

plt.show()
