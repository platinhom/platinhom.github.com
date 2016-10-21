#! /usr/bin/env python
#file pdb_mol2_to_gjf.py
#Author: Platinhom, Last: 2012.5.2
'''
############################################################################
This script could turn the mol2 and pdb files to gif file as Gaussian input.
It could be used by command as "To_gjf.py abc.mol2 abc.gjf" or used in GUI by command"To_gjf.py".
It could extract the Gibbs energy from output file and read the gjf file in GUI.
Enjoy it.
#############################################################################
'''

import os,sys,gc
if len(sys.argv)==1:
    from Tkinter import *
    import tkFileDialog
print __doc__
#In general, the gjf file must contain the element,coordination. Read them...
def CreateGJFLine(element,coordx,coordy,coordz):
    output = element.rjust(2)+' '*14
    output = output + ("%.8f" % coordx).rjust(14)
    output = output + ("%.8f" % coordy).rjust(14)
    output = output + ("%.8f" % coordz).rjust(14)+'\n'
    return output

#parsing the PDB line to gjf format
def ReadPDBLine(Line):
    line = Line
    atomname = Line[12:16].strip()
    if len(atomname)==1: # redo using rjust
        atomname = atomname + "  "
    elif len(atomname)==2:
        atomname = atomname + " "
    elif len(atomname)==3:
        atomname = atomname + " " # This line is necessary for babel to work, though many PDBs in the PDB would have this line commented out

    coordinates = (float(Line[30:38]), float(Line[38:46]), float(Line[46:54]))

    if len(Line) >= 79:
        element = Line[76:78].strip().upper() # element specified explicitly at end of life
        charge = Line [78:80].strip()
    elif element == "": # try to guess at element from name
        two_letters = atomname[0:2].strip().upper()
        if two_letters=='BR':
            element='BR'
        elif two_letters=='CL':
            element='CL'
        elif two_letters=='BI':
            element='BI'
        elif two_letters=='AS':
            element='AS'
        elif two_letters=='AG':
            element='AG'
        elif two_letters=='LI':
            element='LI'
        elif two_letters=='HG':
            element='HG'
        elif two_letters=='MG':
            element='MG'
        elif two_letters=='RH':
            element='RH'
        elif two_letters=='ZN':
            element='ZN'
        else: #So, just assume it's the first letter.
            element = atomname[0:1].strip().upper()

    # Any number needs to be removed from the element name
    element = element.replace('0','')
    element = element.replace('1','')
    element = element.replace('2','')
    element = element.replace('3','')
    element = element.replace('4','')
    element = element.replace('5','')
    element = element.replace('6','')
    element = element.replace('7','')
    element = element.replace('8','')
    element = element.replace('9','')

    lineout=CreateGJFLine(element,coordinates[0],coordinates[1],coordinates[2])
    return lineout

#parsing the MOL2 line to gjf format    
def ReadMOL2Line(Line):
    line = Line
    items=Line.split()
    coordinates =(float(items[2]), float(items[3]), float(items[4]))
    element=items[5][0:2].strip('.')
    lineout=CreateGJFLine(element,coordinates[0],coordinates[1],coordinates[2])
    return lineout

#parsing the MOL2 line to gjf format,note that the multiline need to translate
#to one atom a line when use this function.
def ReadMOELine(Line):
    items=Line.split()
    coordinates =(float(items[4]), float(items[5]), float(items[6]))
    element=items[2]
    lineout=CreateGJFLine(element,coordinates[0],coordinates[1],coordinates[2])
    return lineout

#load the pdb file and return the molecule as gjf format.            
def LoadPDB(FileName):
    gjf=''
    pdbfile = open(FileName,"r")
    for line in pdbfile:
        if len(line) >= 7:
            if line[0:4]=="ATOM" or line[0:6]=="HETATM": 
                gjfline=ReadPDBLine(line)
                gjf=gjf+gjfline
    pdbfile.close()
    return gjf

#load the mol2 file and return the molecule as gjf format. Note that only the first molecule will be read.
def LoadMOL2(FileName):
    gjf=''
    mol2file = open(FileName,"r")
    save_atoms=False
    for line in mol2file:
        if '@<TRIPOS>ATOM' in line:
            save_atoms=True #the next line to save.
            continue
        if save_atoms:
            if line[0]!='@' and line!='\n' and line!='':
                gjfline=ReadMOL2Line(line)
                gjf=gjf+gjfline
            else:
                save_atoms=False #reach the end.
                break
    mol2file.close()
    return gjf

def LoadMOE(FileName):
    gjf=''
    moefile=open(FileName,"r")
    moemol=''
    atom_num=0
    save_atoms=False
    for line in moefile:
        if '#attr' in line and 'ID i aName t aElement t aGeometry t aPosX r aPosY r aPosZ r' not in line:
            break
        if save_atoms:
            moemol+=line
        if '#attr' in line and 'ID i aName t aElement t aGeometry t aPosX r aPosY r aPosZ r' in line:
            save_atoms=True
            atom_num=int(line.split()[1])
    moemol=moemol.replace('\n',' ')
    moemol=moemol.replace('\r','')
    moeitem=moemol.split()
    for i in range(atom_num):
        atomitem=moeitem[(i*7):(i*7+7)]
        line=' '.join(atomitem)
        gjf+=ReadMOELine(line)
    return gjf
        
#This is the foreword in the gjf file,describing the parameters.
global prefile
prefile='''%nproc=8
%mem=4000mb
%chk=otakuPig.chk
%nosave
#p b3lyp/6-31g(d,p) opt=modredundant freq

Molecule_Name

0 1
'''

#Click the 'Open file' button, read the file and show in the text.
def func_buttonfile():
    global filenamevar,initdir,initfile
    global textwidget
    gc.collect()
    filename=tkFileDialog.askopenfilename(title='Select the mol2 or pdb file.',initialdir=initdir.get(),
            filetypes=[('MOL', '*.mol2 *.pdb *.moe'),('GJF', '*.gjf'),('Gaussian output', '*.log *.out'),('all file', '*.*')])
    if filename=='':return
    filenamevar.set(filename)
    initdir.set(os.path.dirname(filename))
    initfile.set(os.path.basename(filename))
    gjf=prefile
    textwidget.delete(1.0,END)    
    if filename[-4:].lower()=='.pdb':
        gjf=gjf+LoadPDB(filename)
    if filename[-5:].lower()=='.mol2':
        gjf=gjf+LoadMOL2(filename)
    if filename[-4:].lower()=='.moe':
        gjf=gjf+LoadMOE(filename)
    if filename[-4:].lower()=='.gjf':
        f=open(filename)
        gjf=f.read()
        f.close()
    if filename[-4:].lower()=='.out' or filename[-4:].lower()=='.log':
        gjf=''
        f=open(filename)
        count=0;readenergy=False
        for line in f:
            if readenergy and count<9:
                gjf+=line
                count+=1
            elif readenergy and count>=9:
                break
            if 'Zero-point correction=' in line and '(Hartree/Particle)' in line:
                readenergy=True
                gjf+=line
                count+=1
        f.close()
    textwidget.insert(END,gjf+'\n')

#Click the 'Save file' button, save the content file in the text to the gjf file.    
def func_savefile():
    global textwidget,initdir,initfile
    gjffile=textwidget.get(1.0,END)
    filename=tkFileDialog.asksaveasfilename(title='Save the gjf file',initialdir=initdir.get(),initialfile=initfile.get(),
                                            defaultextension='.gjf',filetypes=[('GJF', '*.gjf'),('all file', '*.*')])
    if filename=='':return
    f=open(filename,'w')
    f.write(gjffile+'\n')
    f.close()

def delta_Hartree(E0=0,E1=1,accurancy=2):
    delta_hartree=E1-E0
    delta_kcal=delta_hartree*627.510
    return round(delta_kcal,accurancy)

def func_button_calc():
    global entry_E0,entry_E1,deltaE_var,accurancy_var
    if not entry_E0.get() or not entry_E1.get():return
    E0=float(entry_E0.get())
    E1=float(entry_E1.get())
    accurancy=int(accurancy_var.get())
    if E0 and E1:
        deltaE=delta_Hartree(E0,E1,accurancy)
        deltaE_var.set(deltaE)

#the button to call the interface to extract the done structure information from the out/log result to a new gjf.
def func_button_extractfromout():
    DoneTk=DoneToplevel(root)
    DoneTk.lift()
    DoneTk.title('Open the output and make the new gjf')
    root.wait_window(DoneTk)

#the class of the interface to extract the done structure information from the out/log result to a new gjf.    
class DoneToplevel(Toplevel):
    def __init__(self,parent,*argv):
        Toplevel.__init__(self,parent,*argv)
        self.focus_force()
        self.grab_set()
        self.DoneTk_out=StringVar()
        self.DoneTk_gjf=StringVar()
        self.lbDoneTk_out=Label(self,textvariable=self.DoneTk_out)
        self.lbDoneTk_out.pack(side=TOP)
        self.lbDoneTk_gjf=Label(self,textvariable=self.DoneTk_gjf)
        self.lbDoneTk_gjf.pack(side=TOP)
        self.btDoneTk_out=Button(self,text='Open Out file',command=self.openDoneTk_out)
        self.btDoneTk_out.pack(side=LEFT)
        self.btDoneTk_gjf=Button(self,text='Open gjf file',command=self.openDoneTk_gjf)
        self.btDoneTk_gjf.pack(side=LEFT)
        self.btDoneTk_sb=Spinbox(self,from_=1,to=10,width=3,wrap=True) #the spinbox to select which done structure to extract,default the second last.
        self.btDoneTk_sb.pack(side=LEFT)
        self.btDoneTk_process=Button(self,text='Process',command=self.DoneTk_process)
        self.btDoneTk_process.pack(side=LEFT)
        self.btDoneTk_quit=Button(self,text='Quit',command=self.destroy)
        self.btDoneTk_quit.pack(side=LEFT)

    #open the origin GJF file to copy its information
    def openDoneTk_gjf(self):
        self.DoneTk_gjf.set(tkFileDialog.askopenfilename())
        self.focus_force()
    #open the Gaussian output file to extract the SCF Done record and coordination.
    def openDoneTk_out(self):
        self.DoneTk_out.set(tkFileDialog.askopenfilename())
        stateDone=[]
        Done_count=0
        logfile=open(self.DoneTk_out.get())
        logfilew=open(self.DoneTk_out.get()+'_process.txt','w')
        orientation_control=False
        orientation_count=1
        SCFDone_control=False
        for line in logfile:
            if orientation_control:
                if orientation_count>=5:
                    if '-----------------------' in line:
                        orientation_control=False
                        orientation_count=1
                        continue
                    stateDone[Done_count][0].append(line)
                else:orientation_count+=1
            if 'Standard orientation:' in line:
                orientation_control=True
                stateDone.append([[],[]])
                continue
            if SCFDone_control:
                stateDone[Done_count][1].append(line)
                SCFDone_control=False
                Done_count+=1
            if ' SCF Done:' in line:
                SCFDone_control=True
                stateDone[Done_count][1].append(line)
        self.btDoneTk_sb.config(to=Done_count)
        self.btDoneTk_sb.delete(0,END)
        self.btDoneTk_sb.insert(0,str(Done_count-1))
        for i in range(len(stateDone)):
            logfilew.write('Done '+str(i+1)+':\n')
            for j in stateDone[i]:
                for line in j:
                    logfilew.write(line)
        logfilew.close()
        logfile.close()
        self.focus_force()

    #open the extracted file and generate the Gaussian new input file.
    def DoneTk_process(self): 
        fdone=open(self.DoneTk_out.get()+'_process.txt')
        forig=open(self.DoneTk_gjf.get())
        fout=open(self.DoneTk_gjf.get()+'_process.gjf','w')
        forig_blankline=0
        while True:
            line=forig.readline()
            fout.write(line)
            if forig_blankline<2:
                if line.strip()=='':
                    forig_blankline+=1
            else:break
        Done_num=self.btDoneTk_sb.get()
        readDone=False
        for i in fdone:
            if readDone:
                if ' SCF Done' in i:
                    break
                items=i.split()
                element=forig.readline().split()[0]
                outline=CreateGJFLine(element,float(items[3].strip()),float(items[4].strip()),float(items[5].strip()))
                fout.write(outline)
            if 'Done '+self.btDoneTk_sb.get()+':' in i:
                readDone=True
        fout.write('\n\n')
        fdone.close()
        forig.close()
        fout.close()
        self.focus_force()

if __name__ == '__main__':
    if len(sys.argv)==1:
        root=Tk()
        gjffilevar=StringVar()
        gjffilevar.set(prefile)
        filenamevar=StringVar()
        initdir=StringVar()
        initfile=StringVar()
        accurancy_var=StringVar()
        deltaE_var=StringVar() 
        root.title('Gaussian aided tools, by otaku_Pig')
        root.resizable(0,0)
        root.geometry('+10+10')
        scroll=Scrollbar(root)
        label_file=Label(root,text='Filename',relief=GROOVE)
        label_file.grid(row=0,column=0)
        label_filename=Label(root,textvariable=filenamevar,width=120)
        label_filename.grid(row=0,column=1,sticky=E+W)
        buttonfile=Button(root,text='Open file',command=func_buttonfile)
        buttonfile.grid(row=0,column=2)
        buttonsave=Button(root,text='Save file',command=func_savefile)
        buttonsave.grid(row=0,column=3)
        textwidget=Text(root,width=150,height=50,yscrollcommand=scroll.set)
        textwidget.grid(row=1,column=0,columnspan=4)
        textwidget.insert(1.0,gjffilevar.get())
        scroll.grid(row=0,column=4,rowspan=2,sticky=N+S)
        scroll.config(command=textwidget.yview)

        #This part is the calculation of the energy
        frame_calc=LabelFrame(root,text='Delta energy from Hartree to kcal/mol',labelanchor='nw') 
        frame_calc.grid(row=2,column=0,columnspan=5,sticky=W+E)
        label_E0=Label(frame_calc,text='E0',relief=GROOVE)
        label_E0.grid(row=0,column=0,padx=5)
        label_E1=Label(frame_calc,text='E1',relief=GROOVE)
        label_E1.grid(row=0,column=2,padx=5)
        label_deltaE=Label(frame_calc,text='delta E',relief=GROOVE)
        label_deltaE.grid(row=0,column=4,padx=5)
        label_accur=Label(frame_calc,text='Accurance',relief=GROOVE)
        label_accur.grid(row=0,column=6,padx=5)
        entry_E0=Entry(frame_calc,width=20)
        entry_E0.grid(row=0,column=1,padx=5)
        entry_E1=Entry(frame_calc,width=20)
        entry_E1.grid(row=0,column=3,padx=5)
        entry_deltaE=Entry(frame_calc,width=20,textvariable=deltaE_var)
        entry_deltaE.grid(row=0,column=5,padx=5)
        spinbox_accurancy=Spinbox(frame_calc,values=range(1,6),width=2,wrap=1,textvariable=accurancy_var)
        accurancy_var.set(2)
        spinbox_accurancy.grid(row=0,column=7,padx=5)
        button_calc=Button(frame_calc,text='Calculate',command=func_button_calc)
        button_calc.grid(row=0,column=8,padx=30)
        #below is the button for extract structure information from output.
        button_extractfromout=Button(frame_calc,text='Extract from out to gjf',command=func_button_extractfromout)
        button_extractfromout.grid(row=0,column=9,padx=30)        
        root.mainloop()
    else:
        if sys.argv[1][-4:].lower()=='.pdb':
            gjf=prefile+LoadPDB(sys.argv[1])
        elif sys.argv[1][-5:].lower()=='.mol2':
            gjf=prefile+LoadMOL2(sys.argv[1])
        elif sys.argv[1][-4:].lower()=='.moe':
            gjf=prefile+LoadMOE(sys.argv[1])
        else:
            print 'Input file must be pdb file or mol2 file.'
            sys.exit(0)
        f=open(sys.argv[2],'w')
        f.write(gjf+'\n\n')
        f.close()
        
