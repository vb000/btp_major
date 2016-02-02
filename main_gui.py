from Tkinter import *
import numpy as np
import cmath
from lineparams_gui import *
from lineparams import *
from constants import *
from performanceparams import *

class performanceparams_gui(lineparams_gui):
   def __init__(self,parent):
       lineparams_gui.__init__(self,parent)
       self.phase_voltage = float(self.entries[30].get())/np.sqrt(3)
       self.v_mat = np.array([[cmath.rect(self.phase_voltage,np.pi*0/180)],\
                              [cmath.rect(self.phase_voltage,np.pi*-120/180)],\
                              [cmath.rect(self.phase_voltage,np.pi*120/180)]])
       self.voltagegradient_button = Button(self.output_frame,text="Compute Surface Voltage"\
                                            "Gradient",command=self.display_vg)
       self.voltagegradient_button.pack(side=LEFT,padx=5)
       
       self.corona_button=Button(self.output_frame,text="Corona performance"\
                                                   ,command=self.display_corona)
       self.corona_button.pack(side=LEFT,padx=5)
   
   def compute_vg(self):
       self.phase_voltage = float(self.entries[30].get())/np.sqrt(3)
       self.v_mat = np.array([[cmath.rect(self.phase_voltage,np.pi*0/180)],\
                              [cmath.rect(self.phase_voltage,np.pi*-120/180)],\
                              [cmath.rect(self.phase_voltage,np.pi*120/180)]])
       self.compute_lineobj()
       if self.groundconductors_no.get() != 0:
           self.ncp= float(self.entries[5].get())#No of conductors in a phase bundle
           self.ncg= float(self.entries[10].get())#No of conductors in a ground bundle
      
           self.phase_svg_mat = voltage_gradient_mat(self.lineobj.pcc_mat(self.v_mat),float(self.entries[1].get()),\
                                            float(self.entries[2].get()),self.ncp)
           self.ground_svg_mat = voltage_gradient_mat(self.lineobj.gcc_mat(self.v_mat),float(self.entries[6].get()),\
                                            float(self.entries[7].get()),self.ncg)
           
           self.lineobj.phase_svg_mat  = self.phase_svg_mat
           self.lineobj.ground_svg_mat = self.ground_svg_mat
       else:
           self.ncp= float(self.entries[5].get())#No of conductos in a phase bundle
           
           self.phase_svg_mat = voltage_gradient_mat(self.lineobj.pcc_mat(self.v_mat),float(self.entries[1].get()),\
                                            float(self.entries[2].get()),self.ncp)
           
           self.lineobj.phase_svg_mat  = self.phase_svg_mat
   
   def display_vg(self):
       self.compute_vg()
       if self.groundconductors_no.get() != 0:
           pcc = "Charge coefficient matrix of phase conductors in KV=\n" \
                   + str((self.lineobj.pcc_mat(self.v_mat))) + "\n"
           gcc = "Charge coefficient matrix of ground conductors in KV=\n" \
                   + str((self.lineobj.gcc_mat(self.v_mat))) + "\n"
       
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
                   + str((self.lineobj.pcc_mat(self.v_mat))) + "\n"
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
           
           np.set_printoptions(precision=3)
           self.text.config(state=NORMAL)
           self.text.delete(1.0, END)
           self.text.insert(END, "\n"+pcig+"\n")
           self.text.insert(END, "\n"+gcig+"\n")
           self.text.config(state=DISABLED)  
        
if __name__ == "__main__":
    root = Tk()
    root.title("EHV AC Transmission Line GUI")
    gui  = performanceparams_gui(root)
    root.mainloop()
        
