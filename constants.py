import numpy as np

U0 = 4*(np.pi)*(1e-7)
Ur = 1
g = 3e5


class ACSR:
    def __init__(self,Dc_resistance = 0.35,radius_conductor = 0.0159,eff_res = 0.0853):
        self.R_dc = Dc_resistance       # Ohm/km
        self.r    = radius_conductor    # m
        self.reff = eff_res             # m
    def __str__(self):
        return str("R_dc = "+str(self.R_dc)+"\n"+"r = "+str(self.r)+"\n"+"reff = "+str(self.reff))

conductor = ACSR()
if __name__=="__main__":
 print(conductor)

