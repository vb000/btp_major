from Tkinter import *
import numpy as np
import constants
import lineparams
        
class Gui:
   """calculates transmission line parameters"""
   def __init__(self,parent):

       self.line_type = StringVar()
       self.line_type.set("Double line configuration")
    
       self.main_window = parent
       self.main_window.geometry("1200x540")
     
       self.lineselection_frame = Frame(parent,relief=RIDGE,borderwidth=2,height=50)
       self.lineselection_frame.pack(side=TOP,expand=NO,fill=X)

       self.input_frame = Frame(parent,relief=RIDGE,borderwidth=2,height=300)
       self.input_frame.pack(side=TOP,expand=NO,fill=BOTH)
       
       self.output_frame = Frame(parent,relief=RIDGE,borderwidth=2,height=50)
       self.output_frame.pack(side=TOP,expand=NO,fill=X)
     
       self.linegeometry_frame=Frame(self.input_frame,relief=RIDGE,borderwidth=1,height=300)
       self.linegeometry_frame.pack(side=LEFT,expand=NO,fill=BOTH,padx=10,pady=5,ipadx=5,ipady=5)

       self.result_frame=Frame(self.input_frame,relief=RIDGE,borderwidth=1,height=400)
       self.result_frame.pack(side=LEFT,expand=YES,fill=BOTH,padx=10,pady=5,ipadx=5,ipady=5)

       Label(self.lineselection_frame, text="Select the transmission line configuration type:",
            font=("Times",16,"bold italic"),padx=3,pady=3, justify=LEFT).pack(side=LEFT, anchor=W)
       
       line_types = ["Single line configuration","Double line configuration"]
       
       for option in line_types:
           button = Radiobutton(self.lineselection_frame, text=str(option),font=12,value=option, 
               command=self.refresh_entries, variable=self.line_type).pack(side=LEFT,padx=5,pady=3)
       self.coordinate_frame=Frame(self.linegeometry_frame)
       self.coordinate_frame.pack(side=TOP,expand=YES,fill=BOTH,padx=10,pady=10,ipadx=10,ipady=10)
       
       self.entries={}
       self.conductorno_frame=Frame(self.coordinate_frame)
       self.conductorno_frame.pack(side=LEFT,expand=NO,fill=Y)
       self.x_frame=Frame(self.coordinate_frame)
       self.x_frame.pack(side=LEFT,expand=NO,fill=Y)
       self.y_frame=Frame(self.coordinate_frame)
       self.y_frame.pack(side=LEFT,expand=NO,fill=Y)
      
       self.entries[11]=Entry(self.conductorno_frame,width=12,justify=CENTER)
       self.entries[11].pack(side=TOP,anchor=N)
       self.entries[11].insert(0,"Conductor No")
       self.entries[11].configure(state='readonly')
      
       self.entries[12]=Entry(self.x_frame,width=18,justify=CENTER)
       self.entries[12].pack(side=TOP,anchor=N)
       self.entries[12].insert(0,"X-Coordinate(in M)")
       self.entries[12].configure(state='readonly')
      
       self.entries[13]=Entry(self.y_frame,width=18,justify=CENTER)
       self.entries[13].pack(side=TOP,anchor=N)
       self.entries[13].insert(0,"Y-Coordinate(in M)")
       self.entries[13].configure(state='readonly')
      
       for i in range(6):
           self.entries[(i+2)*10+1]=Entry(self.conductorno_frame,width=12,justify=CENTER,fg='red')
           self.entries[(i+2)*10+1].pack(side=TOP,anchor=N)
           self.entries[(i+2)*10+1].insert(0,str(i+1))
           self.entries[(i+2)*10+1].configure(state='readonly')
     
       for i in range(6):
           self.entries[(i+2)*10+2]=Entry(self.x_frame,width=20,justify=CENTER)
           self.entries[(i+2)*10+2].pack(side=TOP,anchor=N)
       self.entries[22].insert(0,float(-11.0))
       self.entries[32].insert(0,float(0.0))
       self.entries[42].insert(0,float(11.0))
       self.entries[52].insert(0,float(-11.0))
       self.entries[62].insert(0,float(0.0))
       self.entries[72].insert(0,float(11.0))
      
       for i in range(6):
           self.entries[(i+2)*10+3]=Entry(self.y_frame,width=20,justify=CENTER)
           self.entries[(i+2)*10+3].pack(side=TOP,anchor=N)
       self.entries[23].insert(0,float(15.0))
       self.entries[33].insert(0,float(15.0))
       self.entries[43].insert(0,float(15.0))
       self.entries[53].insert(0,float(10.0))
       self.entries[63].insert(0,float(10.0))
       self.entries[73].insert(0,float(10.0))
      
       self.bundle_frame=Frame(self.linegeometry_frame,relief=SUNKEN,borderwidth=2)
       self.bundle_frame.pack(side=TOP,fill=BOTH,expand=YES)
      
      
       self.label_frame=Frame(self.bundle_frame)
       self.label_frame.pack(side=LEFT,expand=YES,fill=BOTH)
     
       self.entry_frame=Frame(self.bundle_frame,padx=3,pady=3)
       self.entry_frame.pack(side=TOP,expand=YES,fill=BOTH)

      
       Label(self.label_frame, text="Radius of the conductor(in M):",\
             font=("Times",11,"bold"),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[1]=Entry(self.entry_frame,width=12,justify=CENTER)
       self.entries[1].pack(side=TOP,anchor=W)
       self.entries[1].insert(0,float(0.0159))

       Label(self.label_frame, text="Bundle Radius(in M):",\
            font=("Times",11,"bold"),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[2]=Entry(self.entry_frame,width=12,justify=CENTER)
       self.entries[2].pack(side=TOP,anchor=W)
       self.entries[2].insert(0,float(.288))


       Label(self.label_frame, text="Effective Radius(in M):",\
            font=("Times",11,"bold"),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[3]=Entry(self.entry_frame,width=12,justify=CENTER)
       self.entries[3].pack(side=TOP,anchor=W)
       self.entries[3].insert(0,float(0.01272))

       Label(self.label_frame, text="DC Resistance of the conductor(in M):",\
            font=("Times",11,"bold"),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[4]=Entry(self.entry_frame,width=12,justify=CENTER)
       self.entries[4].pack(side=TOP,anchor=W)
       self.entries[4].insert(0,float(0.035))
    
       Label(self.label_frame, text="Number of conductors in the bundle:",
            font=("Times",11,"bold"),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[5]=Entry(self.entry_frame,width=12,justify=CENTER)
       self.entries[5].pack(side=TOP,anchor=W)
       self.entries[5].insert(0,float(2.0))

       self.computeRLC_button=Button(self.output_frame,text="Compute RLC parameters",command=self.compute)
       self.computeRLC_button.pack(side=LEFT)
       
       self.text=Text(self.result_frame)
       self.text.pack(expand=TRUE, fill='both')


   def compute(self):
       obj = None
       if self.line_type.get()=="Single line configuration":
           obj = lineparams.Single_circuit(a1=(float(self.entries[22].get()),float(self.entries[23].get()))\
                                          ,a2=(float(self.entries[32].get()),float(self.entries[33].get()))\
                                          ,a3=(float(self.entries[42].get()),float(self.entries[43].get()))\
                                          ,N=float(self.entries[5].get())\
                                          ,Rb=float(self.entries[2].get()))
       else:
           obj = lineparams.Double_circuit(a1=(float(self.entries[22].get()),float(self.entries[23].get()))\
                                          ,a2=(float(self.entries[32].get()),float(self.entries[33].get()))\
                                          ,a3=(float(self.entries[42].get()),float(self.entries[43].get()))\
                                          ,a4=(float(self.entries[52].get()),float(self.entries[53].get()))\
                                          ,a5=(float(self.entries[62].get()),float(self.entries[63].get()))\
                                          ,a6=(float(self.entries[72].get()),float(self.entries[73].get()))\
                                          ,N=float(self.entries[5].get())\
                                          ,Rb=float(self.entries[2].get()))
       np.set_printoptions(precision=3)
       Lout = "L=\n" + str(obj.L()) + " mH/km\n"
       Cout = "C=\n" + str(obj.C()) + " nF/km\n"
       #print(obj.L())
       self.text.config(state=NORMAL)
       self.text.delete(1.0, END)
       self.text.insert(END, "\n"+Lout+"\n"+Cout)
       self.text.config(state=DISABLED)
      
    
   def refresh_entries(self):
       if self.line_type.get() == "Single line configuration":
          self.entries[52]["state"]=DISABLED
          self.entries[62]["state"]=DISABLED
          self.entries[72]["state"]=DISABLED
          self.entries[53]["state"]=DISABLED
          self.entries[63]["state"]=DISABLED
          self.entries[73]["state"]=DISABLED

       else: 
          self.entries[52]["state"]=NORMAL
          self.entries[62]["state"]=NORMAL
          self.entries[72]["state"]=NORMAL
          self.entries[53]["state"]=NORMAL
          self.entries[63]["state"]=NORMAL
          self.entries[73]["state"]=NORMAL

        
if __name__ == "__main__":
    root = Tk()
    root.title("EHV AC Transmission Line GUI")
    gui  = Gui(root)
    root.mainloop()
