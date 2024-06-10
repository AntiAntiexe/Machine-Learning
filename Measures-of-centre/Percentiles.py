import numpy

ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39,
        80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

percentile = numpy.percentile(ages, 75)  # Input the list and the percentile you wish to find with NumPy.

print('The .75 percentile is: ', percentile)  # Answer is 43 meaning that 75% of the people are 43 or younger.
