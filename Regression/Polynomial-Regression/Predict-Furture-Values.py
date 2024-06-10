import numpy

x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

# Create the polynomial line of regression
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# Input the desired x value
speed = mymodel(17)
print(speed)
