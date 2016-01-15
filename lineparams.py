import numpy as np
from conductor import *
from constants import *

def P1(a1, a2, a3, N, Rb):
    gmr = Rb*((N*conductor.reff/Rb)**(1.0/N))

    P_mat = np.zeros((5,5))
    
    P_mat[1,1] = np.log(2*a1[1]/gmr)
    P_mat[2,2] = np.log(2*a2[1]/gmr) 
    P_mat[3,3] = np.log(2*a3[1]/gmr)
    P_mat[1,2] = np.log( np.sqrt(((a1[0]-a2[0])**2.0) + ((a1[1]+a2[1])**2.0))\
                         /np.sqrt(((a1[0]-a2[0])**2.0) + ((a1[1]-a2[1])**2.0))\
                       ) # ln(I12/A12)
    P_mat[2,3] = np.log( np.sqrt(((a2[0]-a3[0])**2.0) + ((a2[1]+a3[1])**2.0))\
                         /np.sqrt(((a2[0]-a3[0])**2.0) + ((a2[1]-a3[1])**2.0))\
                       ) # ln(I23/A23)
    P_mat[1,3] = np.log( np.sqrt(((a1[0]-a3[0])**2.0) + ((a1[1]+a3[1])**2.0))\
                         /np.sqrt(((a1[0]-a3[0])**2.0) + ((a1[1]-a3[1])**2.0))\
                       ) # ln(I13/A13)
    P_mat[2,1] = P_mat[1,2]
    P_mat[3,2] = P_mat[2,3]
    P_mat[3,1] = P_mat[1,3]
    
    return P_mat[1:4,1:4]

def L1(a1,a2,a3,N,Rb):
    return 0.2 * P1(a1,a2,a3,N,Rb) # mH/km

def C1(a1,a2,a3,N,Rb):
    Linv = np.linalg.inv(L1(a1,a2,a3,N,Rb))
    return (Linv/(g**2))*1e12 # nF/km

print C1((-11.0,15.0), (0.0,15.0), (11.0,15.0), 10, 10)
