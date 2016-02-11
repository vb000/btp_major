from Tkinter import *
import numpy as np
import cmath
from lineparams_gui import *
from lineparams import *
from constants import *
from performanceparams import *
import matplotlib.pyplot as plt
import matplotlib,sys
matplotlib.use('TkAgg')	
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class performanceparams_gui(lineparams_gui):
    def __init__(self,parent):
       lineparams_gui.__init__(self,parent)
       self.phase_voltage = float(self.entries[30].get())/np.sqrt(3)
       self.v_mat = np.array([[cmath.rect(self.phase_voltage,np.pi*0/180)],\
                              [cmath.rect(self.phase_voltage,np.pi*-120/180)],\
                              [cmath.rect(self.phase_voltage,np.pi*120/180)]])
       self.voltagegradient_button = Button(self.output_frame,text="Compute Surface Voltage"\
                              "Gradient",font=("Fixedsys",9,"bold"),command=self.display_vg)
       self.voltagegradient_button.pack(side=LEFT,padx=5)
       
       self.corona_button=Button(self.output_frame,text="Corona performance",\
                                 font=("Fixedsys",9,"bold"),command=self.display_corona)
       self.corona_button.pack(side=LEFT,padx=5)
       
       self.Electricfield_button = Button(self.output_frame,text="Electric field",\
                                     font=("Fixedsys",9,"bold"),command=self.compute_display_ef)
       self.Electricfield_button.pack(side=LEFT,padx=5)
       
       
    def compute_vg(self):
       self.phase_voltage = float(self.entries[30].get())/np.sqrt(3)
       self.v_mat = np.array([[cmath.rect(self.phase_voltage,np.pi*0/180)],\
                              [cmath.rect(self.phase_voltage,np.pi*-120/180)],\
                              [cmath.rect(self.phase_voltage,np.pi*120/180)]])
       self.compute_lineobj()
       if self.groundconductors_no.get() != 0:
           self.ncp= float(self.entries[5].get())#No of conductors in a phase bundle
           self.ncg= float(self.entries[10].get())#No of conductors in a ground bundle
      
           self.phase_svg_mat = voltage_gradient_mat(abs(self.lineobj.pcc_mat(self.v_mat)),float(self.entries[1].get()),\
                                            float(self.entries[2].get()),self.ncp)
           self.ground_svg_mat = voltage_gradient_mat(abs(self.lineobj.gcc_mat(self.v_mat)),float(self.entries[6].get()),\
                                            float(self.entries[7].get()),self.ncg)
           
           self.lineobj.phase_svg_mat  = self.phase_svg_mat
           self.lineobj.ground_svg_mat = self.ground_svg_mat
       else:
           self.ncp= float(self.entries[5].get())#No of conductos in a phase bundle
           
           self.phase_svg_mat = voltage_gradient_mat(abs(self.lineobj.pcc_mat(self.v_mat)),float(self.entries[1].get()),\
                                            float(self.entries[2].get()),self.ncp)
           
           self.lineobj.phase_svg_mat  = self.phase_svg_mat

    def compute_corona(self):
        self.compute_lineobj()
        self.compute_vg()
        
        a = () # conductor coordinates
        if self.line_type.get() == "Single line configuration":
            a = (self.lineobj.a1, self.lineobj.a2, self.lineobj.a3)
        elif self.line_type.get() == "Double line configuration":
            a = (self.lineobj.a1, self.lineobj.a2, self.lineobj.a3, self.lineobj.a4, self.lineobj.a5, self.lineobj.a6)

        Np = self.lineobj.Np # no. of conductors in the bundle
        d  = 2*100*self.lineobj.conductor_p.r # diameter of condcutor in cm

        # audio noise
        h = 0   # fixme: place a entry here
        self.corona_axis = list(range(-30, 30, 1))
        self.an_vals = [audio_noise(a, x, h, d, Np, self.phase_svg_mat) for x in self.corona_axis] # audio noise values in dB
       
        # TODO: radio noise



    def display_vg(self):
        self.compute_vg()
        if self.groundconductors_no.get() != 0:
            pcc = "Charge coefficient matrix of phase conductors in KV=\n" \
                   + str(abs(self.lineobj.pcc_mat(self.v_mat))) + "\n"
            gcc = "Charge coefficient matrix of ground conductors in KV=\n" \
                   + str(abs(self.lineobj.gcc_mat(self.v_mat))) + "\n"

            phase_svg="Surface voltage gradient of phase conductors =\n" \
                      + str(self.lineobj.phase_svg_mat) + "kv/cm\n"
            ground_svg="Surface voltage gradient of ground conductors =\n" \
                      + str(self.lineobj.ground_svg_mat) + "kv/cm\n" 
            np.set_printoptions(precision=3)
            self.text.config(state=NORMAL)
            self.text.delete(1.0, END)
            self.text.insert(END, "\n"+pcc+"\n")
            self.text.insert(END, "\n"+gcc+"\n")
            self.text.insert(END, "\n"+phase_svg+"\n")
            self.text.insert(END, "\n"+ground_svg+"\n")
            self.text.config(state=DISABLED)
        else:
            pcc = "Charge coefficient matrix of phase conductors in KV=\n" \
                   + str(abs(self.lineobj.pcc_mat(self.v_mat))) + "\n"
            phase_svg="Surface voltage gradient of phase conductors =\n" \
                      + str(self.lineobj.phase_svg_mat) + "kv/cm\n"

            np.set_printoptions(precision=3)
            self.text.config(state=NORMAL)
            self.text.delete(1.0, END)
            self.text.insert(END, "\n"+pcc+"\n")
            self.text.insert(END, "\n"+phase_svg+"\n")
            self.text.config(state=DISABLED)

    def display_corona(self):
        self.ep= (21.4/1.3)*(1+0.301/np.sqrt(float(self.entries[1].get())*1e2))
        self.eg= (21.4/1.3)*(1+0.301/np.sqrt(float(self.entries[6].get())*1e2))

        pcig="corona inception gradient of phase conductors =\n" \
               + "{0:.03f}".format(self.ep) + " kv/cm\n"
        gcig="corona inception gradient of ground conductor =\n" \
               + "{0:.03f}".format(self.eg) + " kv/cm\n"

        self.compute_corona()

        np.set_printoptions(precision=3)
        self.text.config(state=NORMAL)
        self.text.delete(1.0,  END)
        self.text.insert(END, "\n"+pcig+"\n")
        self.text.insert(END, "\n"+gcig+"\n")
        self.text.config(state=DISABLED)  

        plt.plot(self.corona_axis, self.an_vals, label="Audio Noise due to corona")
        plt.legend(loc='best')
        plt.show()

    def compute_display_ef(self):
        #ground conductors excluded..as charge on them is usually very small
        cp=constants.ACSR(float(self.entries[4].get()),float(self.entries[1].get()),float(self.entries[3].get()))  
        self.phase_voltage = float(self.entries[30].get())/np.sqrt(3)
        self.v_mat = np.array([[cmath.rect(self.phase_voltage,np.pi*0/180)],\
                              [cmath.rect(self.phase_voltage,np.pi*-120/180)],\
                              [cmath.rect(self.phase_voltage,np.pi*120/180)]])                      
        if self.line_type.get()=="Single line configuration":
           self.lineobj = lineparams.Single_circuit(a1=(float(self.entries[22].get()),float(self.entries[23].get()))\
                                              ,a2=(float(self.entries[32].get()),float(self.entries[33].get()))\
                                              ,a3=(float(self.entries[42].get()),float(self.entries[43].get()))\
                                              ,Np=float(self.entries[5].get())\
                                              ,Rbp=float(self.entries[2].get()),conductor_p=cp)
           self.a = (self.lineobj.a1,self.lineobj.a2,self.lineobj.a3)
           self.p = (float(self.entries[101].get()),float(self.entries[102].get()))
           self.sef = electric_field_single(self.lineobj.pcc_mat(self.v_mat).transpose(),self.a,self.p)
           self.text.config(state=NORMAL)
           self.text.delete(1.0, END)
           self.text.insert(END, "\nElectric field at given coordinates is:\n"+str(self.sef)+" Kv/m\n")
           self.text.config(state=DISABLED)  
           h = float(self.entries[103].get())
           x = list(range(-30,30,1))
           f = []
           for i in x:
               f.append(electric_field_single(self.lineobj.pcc_mat(self.v_mat).transpose(),self.a,(i,h))[0][0])
           m = [float(i) for i in x]
           ax = plt.gca()
           ax.spines['left'].set_position(('data',0))
           plt.plot(np.array(m),np.array(f),label="Electric field-I in Kv/m")
           plt.legend(loc='best')
           plt.show()
           
        else:
           self.lineobj = lineparams.Double_circuit(a1=(float(self.entries[22].get()),float(self.entries[23].get()))\
                                              ,a2=(float(self.entries[32].get()),float(self.entries[33].get()))\
                                              ,a3=(float(self.entries[42].get()),float(self.entries[43].get()))\
                                              ,a4=(float(self.entries[52].get()),float(self.entries[53].get()))\
                                              ,a5=(float(self.entries[62].get()),float(self.entries[63].get()))\
                                              ,a6=(float(self.entries[72].get()),float(self.entries[73].get()))\
                                              ,Np=float(self.entries[5].get())\
                                              ,Rbp=float(self.entries[2].get()),conductor_p=cp)
           self.a = (self.lineobj.a1,self.lineobj.a2,self.lineobj.a3,\
                     self.lineobj.a4,self.lineobj.a5,self.lineobj.a6)
           self.p = (float(self.entries[101].get()),float(self.entries[102].get()))
           self.sef = electric_field_double(self.lineobj.pcc_mat(self.v_mat).transpose(),self.a,self.p)
           self.text.config(state=NORMAL)
           self.text.delete(1.0, END)
           self.text.insert(END, "\nElectric field at given coordinates is:\n"+str(self.sef)+" Kv/m\n")
           self.text.config(state=DISABLED)
           h = float(self.entries[103].get())
           x = list(range(-30,30,1))
           f = []
           for i in x:
               f.append(electric_field_double(self.lineobj.pcc_mat(self.v_mat).transpose(),self.a,(i,h))[0][0])
           m = [float(i) for i in x]
           ax = plt.gca()
           ax.spines['left'].set_position(('data',0))
           plt.plot(np.array(m),np.array(f),label="Electric field-II in Kv/m")
           plt.legend(loc='best')
           plt.show()
       
if __name__ == "__main__":
    root = Tk()
    root.title("EHV AC Transmission Line GUI")
    gui  = performanceparams_gui(root)
    root.mainloop()
        
