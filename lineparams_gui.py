from Tkinter import *
import numpy as np
import constants,lineparams
        
class lineparams_gui():
   """calculates transmission line parameters"""
   def __init__(self,parent):

       self.line_type = StringVar()
       self.line_type.set("Double line configuration")
    
       self.main_window = parent
       self.main_window.geometry("1400x720")
     
       self.lineselection_frame = Frame(parent,relief=RIDGE,borderwidth=2,height=50)
       self.lineselection_frame.pack(side=TOP,expand=NO,fill=X)

       self.input_frame = Frame(parent,relief=RIDGE,borderwidth=2,height=200)
       self.input_frame.pack(side=TOP,expand=NO,fill=BOTH)
       
       self.output_frame = Frame(parent,relief=RIDGE,borderwidth=2,height=50)
       self.output_frame.pack(side=TOP,expand=NO,fill=X)
     
       self.linegeometry_frame=Frame(self.input_frame,relief=RIDGE,borderwidth=1,height=300)
       self.linegeometry_frame.pack(side=LEFT,expand=NO,fill=BOTH,padx=10,pady=5,ipadx=5,ipady=5)

       self.result_frame=Frame(self.input_frame,relief=RIDGE,borderwidth=1,height=400)
       self.result_frame.pack(side=LEFT,expand=YES,fill=BOTH,padx=10,pady=5,ipadx=5,ipady=5)
       
     
       self.op_frame=Frame(self.result_frame,borderwidth=1,height=400)
       self.op_frame.pack(side=LEFT,expand=YES,fill=BOTH)
       
       self.power_frame=Frame(self.op_frame,relief=RIDGE,borderwidth=1)
       self.power_frame.pack(side=TOP,expand=NO,fill=BOTH)
       
       self.em_frame=Frame(self.op_frame,relief=RIDGE,borderwidth=1)
       self.em_frame.pack(side=TOP,expand=YES,fill=BOTH,pady=10)
       
       self.labelpower_frame=Frame(self.power_frame)
       self.labelpower_frame.pack(side=LEFT,expand=YES,fill=BOTH,padx=5)
     
       self.entrypower_frame=Frame(self.power_frame,padx=3,pady=3)
       self.entrypower_frame.pack(side=TOP,expand=YES,fill=BOTH)
       
       self.labelem_frame=Frame(self.em_frame)
       self.labelem_frame.pack(side=LEFT,expand=YES,fill=BOTH,padx=5)
     
       self.entryem_frame=Frame(self.em_frame,padx=3,pady=3)
       self.entryem_frame.pack(side=LEFT,expand=YES,fill=BOTH)
      
       self.entries = {}
       Label(self.labelpower_frame, text="Power Rating(in MW):",\
             font=("Times",11,"bold"),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[20]=Entry(self.entrypower_frame,width=12,justify=CENTER)
       self.entries[20].pack(side=TOP,anchor=W)
       self.entries[20].insert(0,float(1000))

       Label(self.labelpower_frame, text="Voltage Rating(in KV):",\
            font=("Times",11,"bold"),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[30]=Entry(self.entrypower_frame,width=12,justify=CENTER)
       self.entries[30].pack(side=TOP,anchor=W)
       self.entries[30].insert(0,float(420))
       
       Label(self.labelpower_frame, text="Phase current(in kA):",\
            font=("Times",11,"bold"),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[50]=Entry(self.entrypower_frame,width=12,justify=CENTER)
       self.entries[50].pack(side=TOP,anchor=W)
       self.entries[50].insert(0,float(1.5))


       Label(self.labelpower_frame, text="Length of Transmission Line(in kM):",\
            font=("Times",11,"bold"),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[40]=Entry(self.entrypower_frame,width=12,justify=CENTER)
       self.entries[40].pack(side=TOP,anchor=W)
       self.entries[40].insert(0,float(200))
       
       Label(self.labelem_frame, text="Plot Audible Noise at height(in m):",\
            font=("Times",11),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[107]=Entry(self.entryem_frame,width=12,justify=CENTER)
       self.entries[107].pack(side=TOP,anchor=W)
       self.entries[107].insert(0,float(0.0))
       
       Label(self.labelem_frame, text="Plot Radio Noise at height(in m):",\
            font=("Times",11),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[108]=Entry(self.entryem_frame,width=12,justify=CENTER)
       self.entries[108].pack(side=TOP,anchor=W)
       self.entries[108].insert(0,float(0.0))
       
       Label(self.labelem_frame, text="Measure Electricfield at x coordinate:",\
             font=("Times",11),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[101]=Entry(self.entryem_frame,width=12,justify=CENTER)
       self.entries[101].pack(side=TOP,anchor=W)
       self.entries[101].insert(0,float(0))

       Label(self.labelem_frame, text="                                     y coordinate:",\
            font=("Times",11),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[102]=Entry(self.entryem_frame,width=12,justify=CENTER)
       self.entries[102].pack(side=TOP,anchor=W)
       self.entries[102].insert(0,float(2))
       
       Label(self.labelem_frame, text="Plot Electric field at height(in m):",\
            font=("Times",11),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[103]=Entry(self.entryem_frame,width=12,justify=CENTER)
       self.entries[103].pack(side=TOP,anchor=W)
       self.entries[103].insert(0,float(0.0))
       
       Label(self.labelem_frame, text="Measure Magnetic field at x coordinate:",\
             font=("Times",11),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[104]=Entry(self.entryem_frame,width=12,justify=CENTER)
       self.entries[104].pack(side=TOP,anchor=W)
       self.entries[104].insert(0,float(0))

       Label(self.labelem_frame, text="                                        y coordinate:",\
            font=("Times",11),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[105]=Entry(self.entryem_frame,width=12,justify=CENTER)
       self.entries[105].pack(side=TOP,anchor=W)
       self.entries[105].insert(0,float(2))


       Label(self.labelem_frame, text="Plot Magnetic field at height(in m):",\
            font=("Times",11),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[106]=Entry(self.entryem_frame,width=12,justify=CENTER)
       self.entries[106].pack(side=TOP,anchor=W)
       self.entries[106].insert(0,float(0.0))

       Label(self.lineselection_frame, text="Transmission line configuration type:",
            font=("Courier New",14,"bold"),padx=3,pady=3, justify=LEFT).pack(side=LEFT, anchor=W)
       
       line_types = ["Single line configuration","Double line configuration"]
       
       for option in line_types:
           button = Radiobutton(self.lineselection_frame, text=str(option),font=12,value=option, 
               command=self.refresh_entries, variable=self.line_type).pack(side=LEFT,padx=5,pady=3)
       self.coordinate_frame=Frame(self.linegeometry_frame)
       self.coordinate_frame.pack(side=TOP,expand=YES,fill=BOTH,padx=5,pady=5,ipadx=5,ipady=5)
       
       self.conductorno_frame=Frame(self.coordinate_frame)
       self.conductorno_frame.pack(side=LEFT,expand=NO,fill=Y)
       self.x_frame=Frame(self.coordinate_frame)
       self.x_frame.pack(side=LEFT,expand=NO,fill=Y)
       self.y_frame=Frame(self.coordinate_frame)
       self.y_frame.pack(side=LEFT,expand=NO,fill=Y)

       Label(self.lineselection_frame, text="Number of ground conductors:",\
             font=("Times",14,"bold"),padx=10,pady=0, justify=LEFT).pack(side=LEFT, anchor=W)
       self.groundconductors_no=IntVar()
       self.groundconductors_no.set(2)
       for option in (0,1,2):
           button = Radiobutton(self.lineselection_frame, text=str(option),font=10,value=option,\
           variable=self.groundconductors_no,command=self.refresh_groundno).pack(side=LEFT,padx=5,pady=3)

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
      
       for i in range(8):
           self.entries[(i+2)*10+1]=Entry(self.conductorno_frame,width=12,justify=CENTER,fg='red')
           self.entries[(i+2)*10+1].pack(side=TOP,anchor=N)
	   if i<=5:
               self.entries[(i+2)*10+1].insert(0,str(i+1))
	   else:
	       self.entries[(i+2)*10+1].insert(0,str(i-5))

           self.entries[(i+2)*10+1].configure(state='readonly')
     
       for i in range(8):
           self.entries[(i+2)*10+2]=Entry(self.x_frame,width=20,justify=CENTER)
           self.entries[(i+2)*10+2].pack(side=TOP,anchor=N)
       self.entries[22].insert(0,float(-11.3))
       self.entries[32].insert(0,float(0.0))
       self.entries[42].insert(0,float(11.3))
       self.entries[52].insert(0,float(-11.3))
       self.entries[62].insert(0,float(0.0))
       self.entries[72].insert(0,float(11.3))
       self.entries[82].insert(0,float(-8.0))
       self.entries[92].insert(0,float(8.0))
      
       for i in range(8):
           self.entries[(i+2)*10+3]=Entry(self.y_frame,width=20,justify=CENTER)
           self.entries[(i+2)*10+3].pack(side=TOP,anchor=N)
       self.entries[23].insert(0,float(9.81))
       self.entries[33].insert(0,float(9.81))
       self.entries[43].insert(0,float(9.81))
       self.entries[53].insert(0,float(12.0))
       self.entries[63].insert(0,float(12.0))
       self.entries[73].insert(0,float(12.0))
       self.entries[83].insert(0,float(20.875))
       self.entries[93].insert(0,float(20.875))

       self.phaseconductor_frame=Frame(self.linegeometry_frame)
       self.phaseconductor_frame.pack(side=TOP,fill=BOTH,expand=YES)
      
       Label(self.phaseconductor_frame, text="Phase conductor and bundle parameters",\
             font=("Helvetica",12,"bold"),fg="blue",padx=3,pady=3, justify=LEFT).pack(side=TOP, anchor=W)
      
       self.bundle_frame=Frame(self.linegeometry_frame,relief=SUNKEN,borderwidth=2)
       self.bundle_frame.pack(side=TOP,fill=BOTH,expand=YES,padx=3,pady=3,ipadx=3,ipady=3)
     
      
       self.label_frame=Frame(self.bundle_frame)
       self.label_frame.pack(side=LEFT,expand=YES,fill=BOTH,padx=5)
     
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
       
       Label(self.label_frame, text="Number of strands in a conductor:",
            font=("Times",11,"bold"),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[15]=Entry(self.entry_frame,width=12,justify=CENTER)
       self.entries[15].pack(side=TOP,anchor=W)
       self.entries[15].insert(0,float(26))
       
       Label(self.label_frame, text="Diameter of the strand(in M):",
            font=("Times",11,"bold"),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[25]=Entry(self.entry_frame,width=12,justify=CENTER)
       self.entries[25].pack(side=TOP,anchor=W)
       self.entries[25].insert(0,float(0.00444))
       
       Label(self.label_frame, text="Resistivity of each strand(in Ohm-M):",
            font=("Times",11,"bold"),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[35]=Entry(self.entry_frame,width=12,justify=CENTER)
       self.entries[35].pack(side=TOP,anchor=W)
       self.entries[35].insert(0,float(2.7e-8))
       
       self.groundconductor_frame=Frame(self.linegeometry_frame)
       self.groundconductor_frame.pack(side=TOP,fill=BOTH,expand=YES)
       
       Label(self.groundconductor_frame, text="Ground conductor and bundle parameters",\
             font=("Helvetica",12,"bold"),padx=3,pady=3,fg="blue", justify=LEFT).pack(side=TOP, anchor=W)
 
       self.bundleg_frame=Frame(self.linegeometry_frame,relief=SUNKEN,borderwidth=2)
       self.bundleg_frame.pack(side=TOP,fill=BOTH,expand=YES,padx=3,pady=3,ipadx=5,ipady=5)
     
      
       self.labelg_frame=Frame(self.bundleg_frame)
       self.labelg_frame.pack(side=LEFT,expand=YES,fill=BOTH,padx=5)
     
       self.entryg_frame=Frame(self.bundleg_frame,padx=3,pady=3)
       self.entryg_frame.pack(side=TOP,expand=YES,fill=BOTH)

      
       Label(self.labelg_frame, text="Radius of the conductor(in M):",\
             font=("Times",11,"bold"),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[6]=Entry(self.entryg_frame,width=12,justify=CENTER)
       self.entries[6].pack(side=TOP,anchor=W)
       self.entries[6].insert(0,float(0.004725))

       Label(self.labelg_frame, text="Bundle Radius(in M):",\
            font=("Times",11,"bold"),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[7]=Entry(self.entryg_frame,width=12,justify=CENTER)
       self.entries[7].pack(side=TOP,anchor=W)
       self.entries[7].insert(0,float(.288))


       Label(self.labelg_frame, text="Effective Radius(in M):",\
            font=("Times",11,"bold"),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[8]=Entry(self.entryg_frame,width=12,justify=CENTER)
       self.entries[8].pack(side=TOP,anchor=W)
       self.entries[8].insert(0,float(0.004725))

       Label(self.labelg_frame, text="DC Resistance of the conductor(in M):",\
            font=("Times",11,"bold"),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[9]=Entry(self.entryg_frame,width=12,justify=CENTER)
       self.entries[9].pack(side=TOP,anchor=W)
       self.entries[9].insert(0,float(0.035))
    
       Label(self.labelg_frame, text="Number of conductors in the bundle:",
            font=("Times",11,"bold"),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[10]=Entry(self.entryg_frame,width=12,justify=CENTER)
       self.entries[10].pack(side=TOP,anchor=W)
       self.entries[10].insert(0,float(1.0))

       Label(self.labelg_frame, text="Number of strands in a conductor:",
            font=("Times",11,"bold"),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[16]=Entry(self.entryg_frame,width=12,justify=CENTER)
       self.entries[16].pack(side=TOP,anchor=W)
       self.entries[16].insert(0,float(26))
      
       Label(self.labelg_frame, text="Diameter of the strand(in M):",
            font=("Times",11,"bold"),padx=0,pady=0, justify=LEFT).pack(side=TOP, anchor=W)
       self.entries[26]=Entry(self.entryg_frame,width=12,justify=CENTER)
       self.entries[26].pack(side=TOP,anchor=W)
       self.entries[26].insert(0,float(0.00444))
       
       self.computeRLC_button=Button(self.output_frame,text="Compute RLC parameters",\
                                     font=("Fixedsys",9,"bold"),command=self.display)
       self.computeRLC_button.pack(side=LEFT)
       
       #self.display_frame=(self.result_frame)
       #self.display_frame.pack(side=LEFT,expand=0, fill=BOTH)
       

       self.text=Text(self.result_frame)
       self.text.pack(side=TOP,expand=1, fill=BOTH)


   def compute_lineobj(self,ground_wires):# ground_wires  is whether to consider ground wires or not. 
       self.lineobj = None
       cp=constants.ACSR(float(self.entries[4].get()),float(self.entries[1].get()),float(self.entries[3].get()))
       cg=constants.ACSR(float(self.entries[9].get()),float(self.entries[6].get()),float(self.entries[8].get()))
       if self.groundconductors_no.get()==1 and ground_wires == True :
           if self.line_type.get()=="Single line configuration":
               self.lineobj = lineparams.Single_circuit_1g(a1=(float(self.entries[22].get()),float(self.entries[23].get()))\
                                                  ,a2=(float(self.entries[32].get()),float(self.entries[33].get()))\
                                                  ,a3=(float(self.entries[42].get()),float(self.entries[43].get()))\
                                                  ,a4=(float(self.entries[82].get()),float(self.entries[83].get()))\
                                                  ,Np=float(self.entries[5].get())\
                                                  ,Ng=float(self.entries[10].get())\
                                                  ,Rbp=float(self.entries[2].get())\
                                                  ,Rbg=float(self.entries[7].get()),conductor_p=cp,conductor_g=cg)
           else:
               self.lineobj = lineparams.Double_circuit_1g(a1=(float(self.entries[22].get()),float(self.entries[23].get()))\
                                                 ,a2=(float(self.entries[32].get()),float(self.entries[33].get()))\
                                                 ,a3=(float(self.entries[42].get()),float(self.entries[43].get()))\
                                                 ,a4=(float(self.entries[52].get()),float(self.entries[53].get()))\
                                                 ,a5=(float(self.entries[62].get()),float(self.entries[63].get()))\
                                                 ,a6=(float(self.entries[72].get()),float(self.entries[73].get()))\
                                                 ,a7=(float(self.entries[82].get()),float(self.entries[83].get()))\
                                                 ,Np=float(self.entries[5].get())\
                                                 ,Ng=float(self.entries[10].get())\
                                                 ,Rbp=float(self.entries[2].get())\
                                                 ,Rbg=float(self.entries[7].get()),conductor_p=cp,conductor_g=cg)

       elif self.groundconductors_no.get()==2 and ground_wires == True :
           if self.line_type.get()=="Single line configuration":
               self.lineobj = lineparams.Single_circuit_2g(a1=(float(self.entries[22].get()),float(self.entries[23].get()))\
                                                  ,a2=(float(self.entries[32].get()),float(self.entries[33].get()))\
                                                  ,a3=(float(self.entries[42].get()),float(self.entries[43].get()))\
                                                  ,a4=(float(self.entries[82].get()),float(self.entries[83].get()))\
                                                  ,a5=(float(self.entries[92].get()),float(self.entries[93].get()))\
                                                  ,Np=float(self.entries[5].get())\
                                                  ,Ng=float(self.entries[10].get())\
                                                  ,Rbp=float(self.entries[2].get())\
                                                  ,Rbg=float(self.entries[7].get()),conductor_p=cp,conductor_g=cg)
           else:
               self.lineobj = lineparams.Double_circuit_2g(a1=(float(self.entries[22].get()),float(self.entries[23].get()))\
                                                 ,a2=(float(self.entries[32].get()),float(self.entries[33].get()))\
                                                 ,a3=(float(self.entries[42].get()),float(self.entries[43].get()))\
                                                 ,a4=(float(self.entries[52].get()),float(self.entries[53].get()))\
                                                 ,a5=(float(self.entries[62].get()),float(self.entries[63].get()))\
                                                 ,a6=(float(self.entries[72].get()),float(self.entries[73].get()))\
                                                 ,a7=(float(self.entries[82].get()),float(self.entries[83].get()))\
                                                 ,a8=(float(self.entries[92].get()),float(self.entries[93].get()))\
                                                 ,Np=float(self.entries[5].get())\
                                                 ,Ng=float(self.entries[10].get())\
                                                 ,Rbp=float(self.entries[2].get())\
                                                 ,Rbg=float(self.entries[7].get()),conductor_p=cp,conductor_g=cg)
       else:
           if self.line_type.get()=="Single line configuration":
               self.lineobj = lineparams.Single_circuit(a1=(float(self.entries[22].get()),float(self.entries[23].get()))\
                                              ,a2=(float(self.entries[32].get()),float(self.entries[33].get()))\
                                              ,a3=(float(self.entries[42].get()),float(self.entries[43].get()))\
                                              ,Np=float(self.entries[5].get())\
                                              ,Rbp=float(self.entries[2].get()),conductor_p=cp)
           else:
               self.lineobj = lineparams.Double_circuit(a1=(float(self.entries[22].get()),float(self.entries[23].get()))\
                                              ,a2=(float(self.entries[32].get()),float(self.entries[33].get()))\
                                              ,a3=(float(self.entries[42].get()),float(self.entries[43].get()))\
                                              ,a4=(float(self.entries[52].get()),float(self.entries[53].get()))\
                                              ,a5=(float(self.entries[62].get()),float(self.entries[63].get()))\
                                              ,a6=(float(self.entries[72].get()),float(self.entries[73].get()))\
                                              ,Np=float(self.entries[5].get())\
                                              ,Rbp=float(self.entries[2].get()),conductor_p=cp)
          
   def display(self):
       self.compute_lineobj(True)    
       np.set_printoptions(precision=3)

       p0 = float(self.entries[35].get())
       ds = float(self.entries[25].get())
       ns = float(self.entries[15].get())
       Rout = "R=\n" + "{0:.3f}".format(1337*p0/(ds*ds*ns)) + " Ohm/km\n"
       
       Lout = "L=\n" + str(self.lineobj.L()) + " mH/km\n"
       Cout = "C=\n" + str(self.lineobj.C()) + " nF/km\n"
       #print(self.obj.L())
       self.text.config(state=NORMAL)
       self.text.delete(1.0, END)
       self.text.insert(END, Rout+"\n"+Lout+"\n"+Cout)
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
   
   def refresh_groundno(self):
       if self.groundconductors_no.get()==0:
           self.entries[82]["state"]=DISABLED
           self.entries[92]["state"]=DISABLED
           self.entries[83]["state"]=DISABLED
           self.entries[93]["state"]=DISABLED
       elif self.groundconductors_no.get()==1:
           self.entries[82]["state"]=NORMAL
           self.entries[83]["state"]=NORMAL
           self.entries[92]["state"]=DISABLED
           self.entries[93]["state"]=DISABLED
       else:
           self.entries[82]["state"]=NORMAL
           self.entries[92]["state"]=NORMAL
           self.entries[83]["state"]=NORMAL
           self.entries[93]["state"]=NORMAL

        
if __name__ == "__main__":
    root = Tk()
    root.title("EHV AC Transmission Line GUI")
    gui  = lineparams_gui(root)
    root.mainloop()
