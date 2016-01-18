import numpy as np
from constants import *

class Single_line:
   def __init__(self,a1,a2,a3,N,Rb):
       self.a1 = a1
       self.a2 = a2
       self.a3 = a3
       self.N  = N
       self.Rb = Rb
   def P(self):
      gmr = self.Rb*((self.N*conductor.reff/self.Rb)**(1.0/self.N))
      P_mat = np.zeros((5,5))
    
      P_mat[1,1] = np.log(2*self.a1[1]/gmr)
      P_mat[2,2] = np.log(2*self.a2[1]/gmr) 
      P_mat[3,3] = np.log(2*self.a3[1]/gmr)
      P_mat[1,2] = np.log( np.sqrt(((self.a1[0]-self.a2[0])**2.0) + ((self.a1[1]+self.a2[1])**2.0))\
                           /np.sqrt(((self.a1[0]-self.a2[0])**2.0) + ((self.a1[1]-self.a2[1])**2.0))\
                         ) # ln(I12/A12)
      P_mat[2,3] = np.log( np.sqrt(((self.a2[0]-self.a3[0])**2.0) + ((self.a2[1]+self.a3[1])**2.0))\
                           /np.sqrt(((self.a2[0]-self.a3[0])**2.0) + ((self.a2[1]-self.a3[1])**2.0))\
                         ) # ln(I23/A23)
      P_mat[1,3] = np.log( np.sqrt(((self.a1[0]-self.a3[0])**2.0) + ((self.a1[1]+self.a3[1])**2.0))\
                           /np.sqrt(((self.a1[0]-self.a3[0])**2.0) + ((self.a1[1]-self.a3[1])**2.0))\
                         ) # ln(I13/A13)
      P_mat[2,1] = P_mat[1,2]
      P_mat[3,2] = P_mat[2,3]
      P_mat[3,1] = P_mat[1,3]
    
      return P_mat[1:4,1:4]

   def L(self):
      return 0.2 * self.P() # mH/km

   def C(self):
      Linv = np.linalg.inv(self.L())
      return (Linv/(g**2))*1e12 # nF/km

class Double_line:
   def __init__(self,a1,a2,a3,a4,a5,a6,N,Rb):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.a6 = a6
        self.N  = N
        self.Rb = Rb
   def P(self):
        gmr = self.Rb*((self.N*conductor.reff/self.Rb)**(1.0/self.N))
        x   = [0,self.a1[0],self.a2[0],self.a3[0],self.a4[0],self.a5[0],self.a6[0]] # x-coordinates
        y   = [0,self.a1[1],self.a2[1],self.a3[1],self.a4[1],self.a5[1],self.a6[1]] # y-coordinates
    
        P_mat = np.zeros((7,7))
    
        for i in range(1,7):
            P_mat[i,i] = np.log(2*y[i]/gmr)
    
        for i in range(1,7):
            for j in range(i+1,7):
                P_mat[i,j] = np.log( np.sqrt(((x[i]-x[j])**2.0) + ((y[i]+y[j])**2.0))\
                                     /np.sqrt(((x[i]-x[j])**2.0) + ((y[i]-y[j])**2.0))\
                                   ) # ln(I12/A12)
                P_mat[j,i]=P_mat[i,j]
    
        return P_mat[1:7,1:7]

   def L(self):
        return 0.2*self.P() # mH/km

   def C(self):
        Linv = np.linalg.inv(self.L())
        return (Linv/(g**2))*1e12 # nF/km

if __name__=="__main__":
   line = Single_line((-11.0,15.0), (0.0,15.0), (11.0,15.0),10, 10)
   print(line.P())

