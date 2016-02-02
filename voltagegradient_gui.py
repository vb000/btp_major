from Tkinter import *
import numpy as np
import cmath
from lineparams_gui import *
from lineparams import *
from constants import *

class voltage_gradient():
   def __init__(self,parent):
       self.gui=Gui(parent)
       self.phase_voltage = float(self.gui.entries[30].get())/np.sqrt(3)
       self.v_mat = np.array([[cmath.rect(self.phase_voltage,np.pi*0/180)],\
                              [cmath.rect(self.phase_voltage,np.pi*-120/180)],\
                              [cmath.rect(self.phase_voltage,np.pi*120/180)]])
       self.voltagegradient_button=Button(self.gui.output_frame,text="Compute Surface Voltage"\
                                          "Gradient",command=self.compute_vg)
       self.voltagegradient_button.pack(side=LEFT,padx=5)
       
       self.corona_inceptiongradient_button=Button(self.gui.output_frame,text="Compute corona inception"\
                                                   "Gradient",command=self.compute_cig)
       self.corona_inceptiongradient_button.pack(side=LEFT,padx=5)
   
   def compute_vg(self):
       self.phase_voltage = float(self.gui.entries[30].get())/np.sqrt(3)
       self.v_mat = np.array([[cmath.rect(self.phase_voltage,np.pi*0/180)],\
                              [cmath.rect(self.phase_voltage,np.pi*-120/180)],\
                              [cmath.rect(self.phase_voltage,np.pi*120/180)]])
       self.gui.compute()
       if self.gui.groundconductors_no.get() != 0:
           pcc = "charge coefficient matrix of phase conductors in KV=\n" \
                   + str((self.gui.obj.pcc_mat(self.v_mat))) + "\n"
           gcc = "charge coefficient matrix of ground conductors in KV=\n" \
                   + str((self.gui.obj.gcc_mat(self.v_mat))) + "\n"
       
           self.ncp= float(self.gui.entries[5].get())#No of conductors in a phase bundle
           self.ncg= float(self.gui.entries[10].get())#No of conductors in a ground bundle
      
           phase_svg_mat = voltage_gradient_mat(self.gui.obj.pcc_mat(self.v_mat),float(self.gui.entries[1].get()),\
                                            float(self.gui.entries[2].get()),self.ncp)
           ground_svg_mat = voltage_gradient_mat(self.gui.obj.gcc_mat(self.v_mat),float(self.gui.entries[6].get()),\
                                            float(self.gui.entries[7].get()),self.ncg)
           phase_svg="surface voltage gradient of phase conductors =\n" \
                      + str(phase_svg_mat) + "kv/cm\n"
           ground_svg="surface voltage gradient of ground conductors =\n" \
                      + str(ground_svg_mat) + "kv/cm\n"
           
           np.set_printoptions(precision=3)
           self.gui.text.config(state=NORMAL)
           self.gui.text.delete(1.0, END)
           self.gui.text.insert(END, "\n"+pcc+"\n")
           self.gui.text.insert(END, "\n"+gcc+"\n")
           self.gui.text.insert(END, "\n"+phase_svg+"\n")
           self.gui.text.insert(END, "\n"+ground_svg+"\n")
           self.gui.text.config(state=DISABLED)
       else:
           pcc = "charge coefficient matrix of phase conductors in KV=\n" \
                   + str((self.gui.obj.pcc_mat(self.v_mat))) + "\n"
       
           self.ncp= float(self.gui.entries[5].get())#No of conductos in a phase bundle
           phase_svg_mat = voltage_gradient_mat(self.gui.obj.pcc_mat(self.v_mat),float(self.gui.entries[1].get()),\
                                            float(self.gui.entries[2].get()),self.ncp)
           phase_svg="surface voltage gradient of phase conductors =\n" \
                      + str(phase_svg_mat) + "kv/cm\n"
           
           np.set_printoptions(precision=3)
           self.gui.text.config(state=NORMAL)
           self.gui.text.delete(1.0, END)
           self.gui.text.insert(END, "\n"+pcc+"\n")
           self.gui.text.insert(END, "\n"+phase_svg+"\n")
           self.gui.text.config(state=DISABLED)   
   
   def compute_cig(self):
           ep= (21.4/1.3)*(1+0.301/np.sqrt(float(self.gui.entries[1].get())*1e2))
           eg= (21.4/1.3)*(1+0.301/np.sqrt(float(self.gui.entries[6].get())*1e2))
           pcig="corona inception gradient of phase conductors =\n" \
                   + "{0:.03f}".format(ep) + " kv/cm\n"
           gcig="corona inception gradient of ground conductor =\n" \
                   + "{0:.03f}".format(eg) + " kv/cm\n"
           
           np.set_printoptions(precision=3)
           self.gui.text.config(state=NORMAL)
           self.gui.text.delete(1.0, END)
           self.gui.text.insert(END, "\n"+pcig+"\n")
           self.gui.text.insert(END, "\n"+gcig+"\n")
           self.gui.text.config(state=DISABLED)  
if __name__ == "__main__":
    root = Tk()
    root.title("EHV AC Transmission Line GUI")
    gui  = voltage_gradient(root)
    root.mainloop()
        
