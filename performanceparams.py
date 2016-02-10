import numpy as np
import cmath
from constants import *
from lineparams import *
from main_gui import *

def voltage_gradient_mat(cc_mat,r,R,N):
    multiplier = ((1/r)+(N-1)*(1/(R)))/N
    return cc_mat*multiplier*1e-2 # Kv/cm

def J_mat_single(a,p):#calculates J matrix used in the calculation of fields
    # a is the tuple of coordiante tuples
    # p is the measurement point cordinates
    J_mat = np.zeros((1,3))
    
    for i in range (0,3):
        D  = float(np.sqrt(((a[i][0]-p[0])**2.0)+((a[i][1]-p[1])**2.0)))
        Di = float(np.sqrt(((a[i][0]-p[0])**2.0)+((a[i][1]+p[1])**2.0)))
        J_mat[0][i] = (p[0]-a[i][0])*((1/D**2.0)-(1/Di**2.0))
    return J_mat.transpose()
    
def K_mat_single(a,p):#calculates k matrix used in the calculation of fields
    # a is the tuple of coordiante tuples
    # p is the measurement point cordinates
    K_mat = np.zeros((1,3))
    
    for i in range (0,3):
        D  = float(np.sqrt(((a[i][0]-p[0])**2.0)+((a[i][1]-p[1])**2.0)))
        Di = float(np.sqrt(((a[i][0]-p[0])**2.0)+((a[i][1]+p[1])**2.0)))
        K_mat[0][i] = (p[1]-a[i][1])*(1/D**2.0)-(p[1]+a[i][1])*(1/Di**2.0)
    return K_mat.transpose()

def electric_field_single(cc_mat,a,p):
        #cc_mat is charge coefficient matrix
        eh = abs(np.dot(cc_mat,J_mat_single(a,p)))
        ev = abs(np.dot(cc_mat,K_mat_single(a,p)))
        return np.sqrt(eh**2.0+ev**2.0)

def J_mat_double(a,p):#calculates J matrix used in the calculation of fields
    # a is the tuple of coordiante tuples
    # p is the measurement point cordinates
    J_mat = np.zeros((1,6))
    
    for i in range (0,6):
        D  = float(np.sqrt(((a[i][0]-p[0])**2.0)+((a[i][1]-p[1])**2.0)))
        Di = float(np.sqrt(((a[i][0]-p[0])**2.0)+((a[i][1]+p[1])**2.0)))
        J_mat[0][i] = (p[0]-a[i][0])*((1/D**2.0)-(1/Di**2.0))
    return J_mat.transpose()
    
def K_mat_double(a,p):#calculates k matrix used in the calculation of fields
    # a is the tuple of coordiante tuples
    # p is the measurement point cordinates
    K_mat = np.zeros((1,6))
    
    for i in range (0,6):
        D  = float(np.sqrt(((a[i][0]-p[0])**2.0)+((a[i][1]-p[1])**2.0)))
        Di = float(np.sqrt(((a[i][0]-p[0])**2.0)+((a[i][1]+p[1])**2.0)))
        K_mat[0][i] = (p[1]-a[i][1])*(1/D**2.0)-(p[1]+a[i][1])*(1/Di**2.0)
    return K_mat.transpose()

def electric_field_double(cc_mat,a,p):
        #cc_mat is charge coefficient matrix
        eh = abs(np.dot(cc_mat,J_mat_double(a,p)))
        ev = abs(np.dot(cc_mat,K_mat_double(a,p)))
        return np.sqrt(eh**2.0+ev**2.0)

