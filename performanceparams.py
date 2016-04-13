import numpy as np
import cmath
from constants import *
from lineparams import *
from main_gui import *

def ABCDparams(f, r, l, c, L):
    diagsuml = 0
    for i in range(len(l)):
        diagsuml = (diagsuml + l[i][i])
    uppersuml = (l.sum() - diagsuml)/2

    ls = diagsuml / len(l)
    lm = (2*uppersuml) / ((len(l)*len(l)) - len(l))
    lp = ls - lm

    diagsumc = 0
    for i in range(len(c)):
        diagsumc = (diagsumc + c[i][i])
    uppersumc = (c.sum() - diagsumc)/2

    cs = diagsumc / len(c)
    cm = (2*uppersumc) / ((len(c)*len(c)) - len(c))
    cp = cs - cm

    Z = (r + 1j * (2*np.pi*f) * lp) * L
    Y = (1j*(2*np.pi*f)*cp) * L

    A = np.cosh(np.sqrt(Z*Y))
    B = np.sqrt(Z/Y) * np.sinh(np.sqrt(Z*Y))
    C = np.sqrt(Y/Z) * np.sinh(np.sqrt(Z*Y))
    D = A
    
    #print A,B,C,D,Z,Y
    return np.array([[A, B], [C, D]])

def audio_noise(a, x, h, d, Np, Vg):
    n = len(a)
    
    ANi = np.zeros(n) # initialize ANi  
    for i in range(n):
        D = float(np.sqrt((a[i][0]-x)**2.0 + (a[i][1]-h)**2.0))
        ANi[i] = ((120*np.log(Vg[i]) + 55*np.log(d) - 11.4*np.log(D)) / np.log(10)) +\
                  (-115.4 if (Np<3) else (26.4*np.log(Np)/np.log(10) - 128.4))

    return 10 * np.log(np.sum(10**(0.1*ANi))) / np.log(10) # dB


def radio_noise(a, x, h, d, Np, Vg):
    n = len(a)

    RIi = np.zeros(n)
    for i in range(n):
        D = float(np.sqrt((a[i][0]-x)**2.0 + (a[i][1]-h)**2.0))
        RIi[i] = (3.5*Vg[i] + 6*d - 33*np.log(D/20)/np.log(10) - 30)

    if n==6:
        RIi = 10**(RIi/20) # dB to uV/m
        for i in range(3):
            RIi[i] = 20*np.log( (RIi[i]**2 + RIi[i+3]**2)**0.5 )

    RIi.sort()
    return RIi[2] if (RIi[2]-RIi[1] >= 3) else ((RIi[2]+RIi[1])/2 + 1.5) # dB


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

def magnetic_field_single(c_mat,a,p):
    #c_mat is phase current matrix
    mh = abs(np.dot(c_mat.transpose(),K_mat_single(a,p)))
    mv = abs(np.dot(c_mat.transpose(),J_mat_single(a,p)))
    return 2*(np.sqrt(mh**2.0+mv**2.0)) # in milli Gauss.Gauss=10^-4 Tesla
        

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

def magnetic_field_double(c_mat,a,p):
    #c_mat is phase current matrix
    mh = abs(np.dot((np.concatenate((c_mat,c_mat),axis=0)).transpose(),K_mat_double(a,p)))
    mv = abs(np.dot((np.concatenate((c_mat,c_mat),axis=0)).transpose(),J_mat_double(a,p)))
    return 2*(np.sqrt(mh**2.0+mv**2.0)) # in milli Gauss.Gauss=10^-4 Tesla

