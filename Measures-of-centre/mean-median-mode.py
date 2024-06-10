import numpy
from scipy import stats

speed = [90, 38, 80, 90, 70, 76, 100, 95]  # Data set of speeds
mean = numpy.mean(speed)  # Use NumPy to calculate mean

print('The mean is:', mean)

median = numpy.median(speed)  # Use NumPy to calculate median

print('The median is:', median)

mode = stats.mode(speed)  # Use NumPy to calculate mode

print('The mode is:', mode)  # This prints the mode as well as the count
