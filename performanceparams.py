import numpy as np
import cmath
from constants import *

def voltage_gradient_mat(cc_mat,r,R,N):
    multiplier = ((1/r)+(N-1)*(1/(R)))/N
    return cc_mat*multiplier*1e-2 # Kv/cm
