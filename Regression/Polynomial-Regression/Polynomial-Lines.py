import matplotlib.pyplot as plt
import numpy


# Create the arrays
x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]


# NumPy's method of creating a polynomial model
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))


# Specify how the line will display, it starts at x pos 1 and finishes at x pos 22
myline = numpy.linspace(1, 22, 100)


plt.scatter(x, y)  # Draw the original scatter plot
plt.plot(myline, mymodel(myline))  # Draw the line of polynomial regression
plt.show()
