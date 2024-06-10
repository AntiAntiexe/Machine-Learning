import numpy

speed = [90, 38, 80, 90, 70, 76, 100, 95]  # Data set of speeds

std = numpy.std(speed)  # Use NumPy to calculate standard deviation

print('The Standard Deviation is:', std)

variance = numpy.var(speed)

print('The Variance is:', variance)