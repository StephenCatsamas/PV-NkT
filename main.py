import math
import csv
import numpy as np
import pfit
import matplotlib.pyplot as plt


stpS = np.array([0.01,0.01]) ##cubic meters, pascals

##for reference (V,P) tuple notation
N = 1E26
f= 5
kB = 1.38E-23

poly = np.zeros((0,2))


with open('poly.csv', newline='') as csvfile:
     reader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in reader:
        poly = np.append(poly,[[float(row[0]),float(row[1])]], axis = 0)

poly = np.append(poly, [poly[0,:]], axis = 0)  
smallstp = np.array([poly[0,:]])      
pactv = np.array(poly[0,:])
DUWQlst = np.zeros((0,5))

     

def lincalc(pb):
    global stpS
    global pactv
    global smallstp
    stpVec = pb-pactv
    stpVec = stpVec/np.linalg.norm(stpVec) * stpS[0]   
    if stpS[1] > stpVec[1]:
        stpVec / stpS[0] * stpS[1]
    while (abs(pb[0]-pactv[0]) > stpS[0]*0.8) or (abs(pb[1]-pactv[1]) > stpS[1]*0.8):
        pactv += stpVec
        smallstp = np.append(smallstp,[pactv], axis = 0)
#pfit.plotcycl()
for i in range(len(poly[:,0])):
    lincalc(poly[i,:])
   
def DUWQCalc():
    global smallstp
    global DUWQlst
    for i in range(len(smallstp[:,0])):
        V = smallstp[i,0]
        P = smallstp[i,1]
        dV = smallstp[i,0]-smallstp[i-1,0]
        dP = smallstp[i,1]-smallstp[i-1,1]
        DU = f/2 * (P*dV + V*dP + dP*dV)
        W = -(P + dP/2) * dV
        Q = DU - W
        DUWQlst = np.append(DUWQlst, [[V,P,DU,W,Q]], axis = 0)
        
DUWQCalc()
Qin = 0
for row in DUWQlst:
    if row[4] > 0:
        Qin += row[4]

Wtot = np.sum(DUWQlst[:,3]) 
eff = -Wtot/Qin
print(eff)
plt.plot(poly[:,0],poly[:,1],markersize=0,c='k', marker='o')
plt.plot(smallstp[:,0],smallstp[:,1],markersize=0,c='b', marker='o')
plt.axes().set_aspect('equal', 'datalim')
plt.grid(color='g', linestyle='-', linewidth=0.5)
plt.show()