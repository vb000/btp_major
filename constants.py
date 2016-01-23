import numpy as np

U0 = 4*(np.pi)*(1e-7)
Ur = 1
g = 3e5


class ACSR:
    def __init__(self,Rdc = 0.35,r = 0.0159,Reff = 0.01272):
        self.Rdc  = Rdc       # Ohm/km
        self.r    = r         # m
        self.Reff = Reff      # m
    def __str__(self):
        return str("R_dc = "+str(self.Rdc)+"\n"+"r = "+str(self.r)+"\n"+"reff = "+str(self.Reff))

if __name__=="__main__":
 conductor=ACSR()
 print(conductor)

