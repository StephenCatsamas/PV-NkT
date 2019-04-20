import math
import csv
import numpy as np
import pfit

poly = np.zeros((0,2))

with open('poly.csv', newline='') as csvfile:
     reader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in reader:
        poly = np.append(poly,[[float(row[0]),float(row[1])]], axis = 0)

pfit.plotcycl()