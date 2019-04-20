import math
import csv
import numpy as np
import matplotlib.pyplot as plt

def plotcycl():


    poly = np.zeros((0,2))
            
    with open('poly.csv', newline='') as csvfile:
         reader = csv.reader(csvfile, delimiter=',', quotechar='|')
         for row in reader:
            poly = np.append(poly,[[float(row[0]),float(row[1])]], axis = 0)
            
   
      
         plt.plot(poly[:,0],poly[:,1],markersize=0,c='k', marker='o')
         plt.plot([poly[0,0],poly[-1,0]],[poly[0,1],poly[-1,1]],markersize=0,c='k', marker='o')
         plt.axes().set_aspect('equal', 'datalim')
         plt.show()
                        