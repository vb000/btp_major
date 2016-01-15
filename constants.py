import numpy as np

U0 = 4*(np.pi)*(1e-7)
Ur = 1
g = 3e5


class ACSR:
    def __init__(self):
        self.R_dc = 0.35   # Ohm/km
        self.r = 0.0159    # m
        self.reff = 0.0853 # m

conductor = ACSR()
