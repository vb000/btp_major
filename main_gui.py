from Tkinter import *
import numpy as np
import cmath
from lineparams_gui import *
from lineparams import *
from constants import *
from performanceparams import *
import matplotlib.pyplot as plt
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

        self.Magneticfield_button = Button(self.output_frame,text="Magnetic field",\
                                     font=("Fixedsys",9,"bold"),command=self.compute_display_mf)
        self.Magneticfield_button.pack(side=LEFT,padx=5)

        self.VolProfile_button = Button(self.output_frame,text="Voltage Profile",\
                                     font=("Fixedsys",9,"bold"),command=self.compute_display_volprof)
        self.VolProfile_button.pack(side=LEFT,padx=5)

    def compute_display_volprof(self):
        self.compute_lineobj(True)
        p0 = float(self.entries[35].get())
        ds = float(self.entries[25].get())
        ns = float(self.entries[15].get())
        R  = 1337*p0/(ds*ds*ns)
        phase_current = float(float(self.entries[20].get()) / \
                              (np.sqrt(3) * float(self.entries[30].get())))

        L = int(float(self.entries[40].get()))
        distance = range(L, -1, -1)

        es = []
        for d in range(L, 0, -1):
            abcd = ABCDparams(50, R, self.lineobj.L()*(1e-3), self.lineobj.C()*(1e-9), d)
            es.append(abs(abcd[0][0]*float(self.entries[30].get()) + abcd[0][1]*phase_current))
        es.append(float(self.entries[30].get()))
        es.reverse()

        plt.figure(1)
        plt.plot(distance, es, label="Vlotage Profile")
        plt.title('Voltage');
        plt.xlabel('Distance from sending end (km)');
        plt.legend(loc='best')
        plt.show()
       
    def compute_vg(self,ground_wires):
        self.phase_voltage = float(self.entries[30].get())/np.sqrt(3)
        self.v_mat = np.array([[cmath.rect(self.phase_voltage,np.pi*0/180)],\
                              [cmath.rect(self.phase_voltage,np.pi*-120/180)],\
                              [cmath.rect(self.phase_voltage,np.pi*120/180)]])
        self.compute_lineobj(ground_wires)
        if self.groundconductors_no.get() != 0 and ground_wires:
           self.ncp= float(self.entries[5].get()) #No of conductors in a phase bundle
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
        self.compute_vg(False)
        
        a = () # conductor coordinates
        if self.line_type.get() == "Single line configuration":
            a = (self.lineobj.a1, self.lineobj.a2, self.lineobj.a3)
        elif self.line_type.get() == "Double line configuration":
            a = (self.lineobj.a1, self.lineobj.a2, self.lineobj.a3, self.lineobj.a4, self.lineobj.a5, self.lineobj.a6)

        Np = self.lineobj.Np # no. of conductors in the bundle
        d  = 2*100*self.lineobj.conductor_p.r # diameter of condcutor in cm
        self.corona_axis = list(np.linspace(-30.0, 30.0, 100))

        # audio noise
        h_a = float(self.entries[107].get()) # height at which audio noise should be measured
        self.an_vals = [audio_noise(a, x, h_a, d, Np, self.phase_svg_mat) for x in self.corona_axis] # audio noise values in dB
       
        # radio noise
        h_r = float(self.entries[108].get()) # height at which radio noise should be measured
        self.rn_vals = [radio_noise(a, x, h_r, d, Np, self.phase_svg_mat) for x in self.corona_axis] # radio noise values in dB



    def display_vg(self):
        self.compute_vg(True)
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
                
        plt.figure(1)
        plt.plot(self.corona_axis, self.an_vals, label="Audio Noise due to corona")
        plt.title('Audio Noise due to corona');
        plt.xlabel('Distance from the tower (m)');
        plt.ylabel('Audio noise (dB)');
        
        plt.figure(2)
        plt.plot(self.corona_axis, self.rn_vals, label="Radio Noise due to corona")
        plt.title('Radio Noise due to corona');
        plt.xlabel('Distance from the tower (m)');
        plt.ylabel('Radio noise (dB)');
        plt.show()

    def compute_display_ef(self):
        #ground conductors excluded..as charge on them is usually very small
        self.compute_lineobj(False)  
        self.phase_voltage = float(self.entries[30].get())/np.sqrt(3)
        self.v_mat = np.array([[cmath.rect(self.phase_voltage,np.pi*0/180)],\
                              [cmath.rect(self.phase_voltage,np.pi*-120/180)],\
                              [cmath.rect(self.phase_voltage,np.pi*120/180)]])                      
        if self.line_type.get()=="Single line configuration":
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
       
            ax = plt.gca()
            ax.spines['left'].set_position(('data',0))
            plt.figure(1)
            plt.plot(np.array(x),np.array(f),label="Electric field-I(kv/m)")
            plt.title('Electric Field');
            plt.xlabel('Distance from the tower (m)');
            plt.legend(loc='best')
            plt.show()
           
        else:
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
            
            ax = plt.gca()
            ax.spines['left'].set_position(('data',0))
            plt.figure(1)
            plt.plot(np.array(x),np.array(f),label="Electric field-II(kv/m)")
            plt.title('Electric Field');
            plt.xlabel('Distance from the tower (m)');
            plt.legend(loc='best')
            plt.show()
   
    def compute_display_mf(self):
        #ground conductors excluded..as charge on them is usually very small
        self.compute_lineobj(False) 
        phase_current = float(float(self.entries[20].get()) / \
                              (np.sqrt(3) * float(self.entries[30].get())))
        self.phase_current = float(phase_current)*(1e+3)
        self.c_mat = np.array([[cmath.rect(self.phase_current,np.pi*0/180)],\
                              [cmath.rect(self.phase_current,np.pi*-120/180)],\
                              [cmath.rect(self.phase_current,np.pi*120/180)]])                      
        if self.line_type.get()=="Single line configuration":
            self.a = (self.lineobj.a1,self.lineobj.a2,self.lineobj.a3)
            self.p = (float(self.entries[104].get()),float(self.entries[105].get()))
            self.smf = magnetic_field_single(self.c_mat,self.a,self.p)
            self.text.config(state=NORMAL)
            self.text.delete(1.0, END)
            self.text.insert(END, "\nMagnetic field at given coordinates is:\n"+str(self.smf)+" mG\n")
            self.text.config(state=DISABLED)  
            h = float(self.entries[106].get())
            
            x = list(range(-30,30,1))
            f = []
            for i in x:
               f.append(magnetic_field_single(self.c_mat,self.a,(i,h))[0][0])
            
            ax = plt.gca()
            ax.spines['left'].set_position(('data',0))
            plt.figure(1)
            plt.plot(np.array(x),np.array(f),label="Magnetic field-I in mG")
            plt.title('Magnetic Field');
            plt.xlabel('Distance from the tower (m)');
            plt.legend(loc='best')
            plt.show()
           
        else:
            self.a = (self.lineobj.a1,self.lineobj.a2,self.lineobj.a3,\
                     self.lineobj.a4,self.lineobj.a5,self.lineobj.a6)
            self.p = (float(self.entries[104].get()),float(self.entries[105].get()))
            self.smf = magnetic_field_double(self.c_mat,self.a,self.p)
            self.text.config(state=NORMAL)
            self.text.delete(1.0, END)
            self.text.insert(END, "\nMagnetic field at given coordinates is:\n"+str(self.smf)+" mG\n")
            self.text.config(state=DISABLED)
            h = float(self.entries[106].get())
            x = list(range(-30,30,1))
            f = []
            for i in x:
               f.append(magnetic_field_double(self.c_mat,self.a,(i,h))[0][0])
            
            ax = plt.gca()
            ax.spines['left'].set_position(('data',0))
            plt.figure(1)
            plt.plot(np.array(x),np.array(f),label="Magnetic field-II in mG")
            plt.title('Magnetic Field');
            plt.xlabel('Distance from the tower (m)');
            plt.legend(loc='best')
            plt.show()
            
if __name__ == "__main__":
    root = Tk()
    root.title("EHV AC Transmission Line GUI")
    gui  = performanceparams_gui(root)
    root.mainloop()
        
