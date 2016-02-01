import numpy as np
from constants import *

class Single_circuit:
   def __init__(self,a1,a2,a3,Np,Rbp,conductor_p):
       self.a1 = a1
       self.a2 = a2
       self.a3 = a3
       self.Np = Np
       self.Rbp = Rbp
       self.conductor_p=conductor_p
   def P(self):
      gmr = self.Rbp*((self.Np*self.conductor_p.Reff/self.Rbp)**(1.0/self.Np))
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
   
   def pcc_mat(self,v_mat):
      #pcc_mat is phase charge coefficient matrix used in the calculation of voltage gradient
      return abs(np.dot(np.linalg.inv(self.P()),v_mat)) # Kv"""
   def gcc_mat(self,v_mat):
      return "Not Valid"

class Single_circuit_1g:
   def __init__(self,a1,a2,a3,a4,Np,Ng,Rbp,Rbg,conductor_p,conductor_g):
       self.a1 = a1
       self.a2 = a2
       self.a3 = a3
       self.a4 = a4
       self.Np = Np
       self.Ng = Ng
       self.Rbp = Rbp
       self.Rbg = Rbg
       self.conductor_p=conductor_p
       self.conductor_g=conductor_g
   def P(self):
      gmr_p = self.Rbp*((self.Np*self.conductor_p.Reff/self.Rbp)**(1.0/self.Np))
      gmr_g = self.Rbg*((self.Ng*self.conductor_g.Reff/self.Rbg)**(1.0/self.Ng))
      
      x   = [0,self.a1[0],self.a2[0],self.a3[0],self.a4[0]] # x-coordinates
      y   = [0,self.a1[1],self.a2[1],self.a3[1],self.a4[1]] # y-coordinates
    
      P_mat = np.zeros((5,5))
    
      for i in range(1,4):
          P_mat[i,i] = np.log(2*y[i]/gmr_p)

      P_mat[4,4] = np.log(2*y[4]/gmr_g)
    
      for i in range(1,5):
          for j in range(i+1,5):
              P_mat[i,j] = np.log( np.sqrt(((x[i]-x[j])**2.0) + ((y[i]+y[j])**2.0))\
                                     /np.sqrt(((x[i]-x[j])**2.0) + ((y[i]-y[j])**2.0))\
                                   ) # ln(I12/A12)
              P_mat[j,i]=P_mat[i,j]
    
      return P_mat[1:5,1:5]

   def Ppp(self):
       return self.P()[0:3,0:3]
   def Pgp(self):
       return self.P()[3:4,0:3]
   def Ppg(self):
       return self.P()[0:3,3:4]
   def Pgg(self):
       return self.P()[3:4,3:4]
   def P_red(self):
       return self.Ppp()-reduce(np.dot,[self.Ppg(),np.linalg.inv(self.Pgg()),self.Pgp()])    
   def L(self):
      return 0.2 * self.P_red() # mH/km

   def C(self):
      Linv = np.linalg.inv(self.L())
      return (Linv/(g**2))*1e12 # nF/km
   
   def pcc_mat(self,v_mat):
       return abs(np.dot(np.linalg.inv(self.P_red()),v_mat)) # Kv"""
   def gcc_mat(self,v_mat):
       return abs(reduce(np.dot,[np.linalg.inv(self.Pgg()),self.Pgp(),np.dot(np.linalg.inv(self.P_red()),v_mat)])) # Kv"""

class Single_circuit_2g:
   def __init__(self,a1,a2,a3,a4,a5,Np,Ng,Rbp,Rbg,conductor_p,conductor_g):
       self.a1 = a1
       self.a2 = a2
       self.a3 = a3
       self.a4 = a4
       self.a5 = a5
       self.Np = Np
       self.Ng = Ng
       self.Rbp = Rbp
       self.Rbg = Rbg
       self.conductor_p=conductor_p
       self.conductor_g=conductor_g
   def P(self):
      gmr_p = self.Rbp*((self.Np*self.conductor_p.Reff/self.Rbp)**(1.0/self.Np))
      gmr_g = self.Rbg*((self.Ng*self.conductor_g.Reff/self.Rbg)**(1.0/self.Ng))
      x   = [0,self.a1[0],self.a2[0],self.a3[0],self.a4[0],self.a5[0]] # x-coordinates
      y   = [0,self.a1[1],self.a2[1],self.a3[1],self.a4[1],self.a5[1]] # y-coordinates
    
      P_mat = np.zeros((6,6))
    
      for i in range(1,4):
          P_mat[i,i] = np.log(2*y[i]/gmr_p)
    
      for i in range(4,6):
          P_mat[i,i] = np.log(2*y[i]/gmr_g)
      
      for i in range(1,6):
          for j in range(i+1,6):
              P_mat[i,j] = np.log( np.sqrt(((x[i]-x[j])**2.0) + ((y[i]+y[j])**2.0))\
                                     /np.sqrt(((x[i]-x[j])**2.0) + ((y[i]-y[j])**2.0))\
                                   ) # ln(I12/A12)
              P_mat[j,i]=P_mat[i,j]
    
      return P_mat[1:6,1:6]
   
   def Ppp(self):
       return self.P()[0:3,0:3]
   def Pgp(self):
       return self.P()[3:5,0:3]
   def Ppg(self):
       return self.P()[0:3,3:5]
   def Pgg(self):
       return self.P()[3:5,3:5]
   def P_red(self):
       return self.Ppp()-reduce(np.dot,[self.Ppg(),np.linalg.inv(self.Pgg()),self.Pgp()])
   
   def L(self):
      return 0.2 * self.P_red() # mH/km

   def C(self):
      Linv = np.linalg.inv(self.L())
      return (Linv/(g**2))*1e12 # nF/km
   def pcc_mat(self,v_mat):
       return abs(np.dot(np.linalg.inv(self.P_red()),v_mat)) # Kv"""
   def gcc_mat(self,v_mat):
       return abs(reduce(np.dot,[np.linalg.inv(self.Pgg()),self.Pgp(),np.dot(np.linalg.inv(self.P_red()),v_mat)])) # Kv"""

      

class Double_circuit:
   def __init__(self,a1,a2,a3,a4,a5,a6,Np,Rbp,conductor_p):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.a6 = a6
        self.Np  = Np
        self.Rbp = Rbp
        self.conductor_p=conductor_p
   def P(self):
        gmr = self.Rbp*((self.Np*self.conductor_p.Reff/self.Rbp)**(1.0/self.Np))
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
   def pcc_mat(self,v_mat):
      #pcc_mat is phase charge coefficient matrix used in the calculation of voltage gradient
      return abs(np.dot(np.linalg.inv(self.P()),np.concatenate((v_mat,v_mat),axis=0))) # Kv"""
   def gcc_mat(self,v_mat):
      return "Not Valid"

class Double_circuit_1g:
   def __init__(self,a1,a2,a3,a4,a5,a6,a7,Np,Ng,Rbp,Rbg,conductor_p,conductor_g):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.a6 = a6
        self.a7 = a7
        self.Np = Np
        self.Ng = Ng
        self.Rbp = Rbp
        self.Rbg = Rbg
        self.conductor_p=conductor_p
        self.conductor_g=conductor_g
   def P(self):
        gmr_p = self.Rbp*((self.Np*self.conductor_p.Reff/self.Rbp)**(1.0/self.Np))
        gmr_g = self.Rbg*((self.Ng*self.conductor_g.Reff/self.Rbg)**(1.0/self.Ng))
        x   = [0,self.a1[0],self.a2[0],self.a3[0],self.a4[0],self.a5[0],self.a6[0],self.a7[0]] # x-coordinates
        y   = [0,self.a1[1],self.a2[1],self.a3[1],self.a4[1],self.a5[1],self.a6[1],self.a7[1]] # y-coordinates
    
        P_mat = np.zeros((8,8))
    
        for i in range(1,7):
            P_mat[i,i] = np.log(2*y[i]/gmr_p)
        P_mat[7,7] = np.log(2*y[7]/gmr_g)
   
        for i in range(1,8):
            for j in range(i+1,8):
                P_mat[i,j] = np.log( np.sqrt(((x[i]-x[j])**2.0) + ((y[i]+y[j])**2.0))\
                                     /np.sqrt(((x[i]-x[j])**2.0) + ((y[i]-y[j])**2.0))\
                                   ) # ln(I12/A12)
                P_mat[j,i]=P_mat[i,j]
    
        return P_mat[1:8,1:8]
   
   def Ppp(self):
       return self.P()[0:6,0:6]
   def Pgp(self):
       return self.P()[6:7,0:6]
   def Ppg(self):
       return self.P()[0:6,6:7]
   def Pgg(self):
       return self.P()[6:7,6:7]
   def P_red(self):
       return self.Ppp()-reduce(np.dot,[self.Ppg(),np.linalg.inv(self.Pgg()),self.Pgp()])
   
   def L(self):
        return 0.2*self.P_red() # mH/km

   def C(self):
        Linv = np.linalg.inv(self.L())
        return (Linv/(g**2))*1e12 # nF/km
   
   def pcc_mat(self,v_mat):
       return abs(np.dot(np.linalg.inv(self.P_red()),np.concatenate((v_mat,v_mat),axis=0))) # Kv"""
   def gcc_mat(self,v_mat):
       return abs(reduce(np.dot,[np.linalg.inv(self.Pgg()),self.Pgp(),\
                  np.dot(np.linalg.inv(self.P_red()),np.concatenate((v_mat,v_mat),axis=0))])) # Kv"""


class Double_circuit_2g:
   def __init__(self,a1,a2,a3,a4,a5,a6,a7,a8,Np,Ng,Rbp,Rbg,conductor_p,conductor_g):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.a6 = a6
        self.a7 = a7
        self.a8 = a8
        self.Np = Np
        self.Ng = Ng
        self.Rbp = Rbp
        self.Rbg = Rbg
        self.conductor_p=conductor_p
        self.conductor_g=conductor_g
   def P(self):
        gmr_p = self.Rbp*((self.Np*self.conductor_p.Reff/self.Rbp)**(1.0/self.Np))
        gmr_g = self.Rbg*((self.Ng*self.conductor_g.Reff/self.Rbg)**(1.0/self.Ng))
        
        x   = [0,self.a1[0],self.a2[0],self.a3[0],self.a4[0],self.a5[0],self.a6[0],self.a7[0],self.a8[0]] # x-coordinates
        y   = [0,self.a1[1],self.a2[1],self.a3[1],self.a4[1],self.a5[1],self.a6[1],self.a7[1],self.a8[1]] # y-coordinates
    
        P_mat = np.zeros((9,9))
    
        for i in range(1,7):
            P_mat[i,i] = np.log(2*y[i]/gmr_p)
    
        for i in range(7,9):
            P_mat[i,i] = np.log(2*y[i]/gmr_g)
        
        for i in range(1,9):
            for j in range(i+1,9):
                P_mat[i,j] = np.log( np.sqrt(((x[i]-x[j])**2.0) + ((y[i]+y[j])**2.0))\
                                     /np.sqrt(((x[i]-x[j])**2.0) + ((y[i]-y[j])**2.0))\
                                   ) # ln(I12/A12)
                P_mat[j,i]=P_mat[i,j]
    
        return P_mat[1:9,1:9]
   
   def Ppp(self):
       return self.P()[0:6,0:6]
   def Pgp(self):
       return self.P()[6:8,0:6]
   def Ppg(self):
       return self.P()[0:6,6:8]
   def Pgg(self):
       return self.P()[6:8,6:8]
   def P_red(self):
       return self.Ppp()-reduce(np.dot,[self.Ppg(),np.linalg.inv(self.Pgg()),self.Pgp()])

   def L(self):
        return 0.2*self.P_red() # mH/km

   def C(self):
        Linv = np.linalg.inv(self.L())
        return (Linv/(g**2))*1e12 # nF/km
   def pcc_mat(self,v_mat):
       return abs(np.dot(np.linalg.inv(self.P_red()),np.concatenate((v_mat,v_mat),axis=0))) # Kv"""
   def gcc_mat(self,v_mat):
       return abs(reduce(np.dot,[np.linalg.inv(self.Pgg()),self.Pgp(),\
                  np.dot(np.linalg.inv(self.P_red()),np.concatenate((v_mat,v_mat),axis=0))])) # Kv"""

def voltage_gradient_mat(cc_mat,r,R,N):
    multiplier = ((1/r)+(N-1)*(1/(R)))/N
    return cc_mat*multiplier*1e-2 # Kv/cm

if __name__=="__main__":
   conductor_p=ACSR(Reff=0.01585)
   conductor_g=ACSR(Reff=0.004725)
   line1 = Single_circuit((-11.0,15.0), (0.0,15.0), (11.0,15.0), 2, .288,conductor_p)
   line2 = Single_circuit_2g((-11.3,9.81), (0.0,9.81), (11.3,9.81),(-8.0,20.875), (8.0,20.875),2,1, .2288,0.004725,conductor_p,conductor_g)
   print(line1.P())
   print(line2.P())
