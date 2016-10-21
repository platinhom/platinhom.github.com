---
layout: post
title: 碎裂小分子到3原子以上片段
date: 2015-08-30 13:36:27
categories: CompCB
tags: CompChem Python src
---

小分子分隔成最少3原子的片段脚本.

~~~python
#! /usr/bin/env python
from copy import deepcopy
import math
import os
import sys
import glob
import shutil

def sortlen(f1,f2):
    if len(f1)<len(f2):return -1
    else:return 0

def sort_list_0(f1,f2):
    if int(f1[0])<int(f2[0]):return -1
    else:return 0

class Conect:
    ##The connect information of molecule.Nothing to initial.To copy this object,use deepcopy.
    ##Defect:from conect,the molecules that containing single atom could not be identified.
    ##Need:from copy import deepcopy
    def __init__(self):
        self.conects=[]
        self.atom_conects={}#atoms and their conects
        self.atoms=[]
        self.ends=[]#atoms at the end of the sidechain
        self.bonds={}
        self.ring_atoms=[]#atoms in the rings
        self.ring_linkers=[]#atoms link the ring together as the core.
        self.ring_link_atoms={}#the atoms that link to the ring atoms.
        self.biring_atoms=[]#the ring atoms that link two ring directly. 
        self.sidechain_atoms=[]#atoms in the sidechain
        self.rings=[]#search rings based on [0] information,non-chemical sense..
        self.lonely_ring=[]#non-fused ring
        self.fragments=[]#save the >=3 fragments.
        self.fragments_conects={}
        self.fragment_rings=[]#the big ring fragment.
        self.atoms_index={}#the link between atom num and index of atom{atom:index}

    ##restart the atoms,end points,and the atom_conect attributes from conects.
    def restart(self):
        self.atoms=[]
        self.ends=[]
        for i in self.conects:
            self.atoms.append(i[0])
            self.atom_conects[i[0]]=i[1:]
            if len(i)==2:
                self.ends.append(i[0])

    ##read the CONECT information from pdb file.    
    def read_conects_PDB(self,pdbfile,lines=''):
        if lines=='':
            f=open(pdbfile,'r')
            lines=f.readlines()
            f.close()
        elif pdbfile=='' or pdbfile==None:lines=lines
        conects=[]
        for line in lines:
            if line[0:6]=='CONECT':
                items=[]
                for i in range(len(line)/5+1):
                    if i!=0:
                        items.append(line[i*5+1:i*5+6])
                conects.append(items)
        self.conects=conects[:]
        self.restart()
        self.find_ring_atoms()
        return conects

    ##read @<TRIPOS>BOND in mol2.
    def read_conects_MOL2(self,mol2file):
        f=open(mol2file,'r')
        lines=f.readlines()
        f.close()
        atom_conects={}
        bonds={}
        save=False
        for line in lines:
            if '@<TRIPOS>BOND' in line:
                save=True
                continue
            if save:
                if line[0]=='@'or line=='\n' or line=='':break
                items=line.split()#bond in mol2:num atom1 atom2 bond_level
                if items[1] not in atom_conects:atom_conects[items[1]]=[]
                if items[2] not in atom_conects:atom_conects[items[2]]=[]
                atom_conects[items[1]].append(items[2])
                atom_conects[items[2]].append(items[1])
                bonds[(items[1],items[2])]=items[3]
                bonds[(items[2],items[1])]=items[3]                                       
        conects=[]
        for i in atom_conects:
            conect=[i]
            for j in atom_conects[i]:
                conect.append(j)
            conects.append(conect)
        conects.sort(sort_list_0)
        self.conects=conects[:]
        self.bonds=deepcopy(bonds)
        self.restart()
        self.find_ring_atoms()
        return bonds

    ##cut a bond, offer two atoms, even the conects.
    def cut(self,atom1,atom2,conects=''):
        if conects=='':
            if atom2 in self.atom_conects[atom1]:self.atom_conects[atom1].remove(atom2)
            if atom1 in self.atom_conects[atom2]:self.atom_conects[atom2].remove(atom1)
        else:
            if atom2 in conects[atom1]:conects[atom1].remove(atom2)                
            if atom1 in conects[atom2]:conects[atom2].remove(atom1)

    ##refit a bond, offer two atoms, even the conects.
    def rebond(self,atom1,atom2,conects=''):
        if conects=='':
            self.atom_conects[atom1].append(atom2)
            self.atom_conects[atom2].append(atom1)
        else:
            conects[atom1].append(atom2)
            conects[atom2].append(atom1)

    ##remove the sidechain, conserve the rings and their linker
    def remove_sidechain(self):
        allatoms=self.atoms[:]
        for end_atom in self.ends:
            startp=end_atom
            while True:
                if len(self.atom_conects[startp])==1:
                    reach=self.atom_conects[startp][0]##move to and return next atom
                    self.cut(reach,startp)
                    startp=reach
                else:break
                
        temp=deepcopy(self.atom_conects)#remove the blank atom
        for i in temp:            
            if len(temp[i])==0:
                del self.atom_conects[i]
                self.atoms.remove(i)
        self.sidechain_atoms=list(set(allatoms)-set(self.atoms))
        self.ends=[]
        return

    ##To find the ring atoms and return some rings.
    def find_ring_atoms(self,startpoint=''):
        if self.ends!=[]:self.remove_sidechain()##remove sidechain
        if len(self.atoms)==0:
            print "It's a chain molecule!!"
            self.restart()
            return #It's a chain molecule!
        if startpoint=='':startpoint=self.atoms[0]
        ringcore=self.atoms[:] # the non-sidechain atoms
        ring=[]#temp ring
        ringstart=''#record the start point of ring
        ringend=''
        ring_switch=False
        save_ring=False
        restore=self.atom_conects
        connect=deepcopy(restore)
        startp=startpoint
        breakpoint=[startp,self.atom_conects[startp][0]]#(point_stand,point_goto)
        while True:
            reach=connect[startp][0]#move and delete start point. 
            del connect[startp]
            if reach not in connect: reach=('Ring',startp,reach)#Key for judgement of ring.
            else: connect[reach].remove(startp)

            if startp==ringstart:#save the rings and ring atoms.
                if ring_switch==True:
                    save_ring=True
            if save_ring==True:
                ring.append(startp)
            if reach==ringend:
                ring.append(reach)
                self.rings.append(ring)
                for i in ring:
                    if i not in self.ring_atoms:self.ring_atoms.append(i)
                ring_switch=False
                save_ring=False

            #when find a ring,restore the start point and save the ring information.
            if 'Ring' in reach or len(connect[reach])==0:
                if 'Ring' in reach:
                    self.cut(reach[1],reach[2])
                    ring_switch=True
                    ring=[]
                    ringstart=reach[2]
                    ringend=reach[1]
                #If find a end point of the chain.Breakpoint is use to cut the sidechain.
                elif len(connect[reach])==0:
                    self.cut(breakpoint[0],breakpoint[1],restore)
                    if len(restore[startpoint])==0:break #end of the finding!!
                breakpoint=[startpoint,restore[startpoint][0]]
                connect=deepcopy(restore)
                startp=startpoint
                continue

            if len(connect[reach])>=2:
                breakpoint=[reach,connect[reach][0]]#save the breakpoint!
            startp=reach
            
        self.ring_linkers=list(set(ringcore)-set(self.ring_atoms))
        self.restart()#refit the bond,atoms and ends.        
        for ra in self.ring_atoms: #find the atoms link to the rings
            for link in self.atom_conects[ra]:
                if (link not in self.ring_atoms):
                    if link not in self.ring_link_atoms:self.ring_link_atoms[link]=[]
                    self.ring_link_atoms[link].append(ra)

        ##To find the fused ring fragment and fused atoms.
        fragment_rings=self.rings[:]
        lonely=self.rings[:]
        loop=True
        count=1
        while loop:
            loop=False
            if len(fragment_rings)<=1:break
            further_rings=fragment_rings[:]
            for i in fragment_rings[:-1]:
                for j in fragment_rings[fragment_rings.index(i)+1:]:
                    if list(set(i)&set(j))!=[]:  #key in finding fused ring.                      
                        if count==1:#the first time to change the lonely ring.
                            if i in lonely:lonely.remove(i)
                            if j in lonely:lonely.remove(j)
                        loop=True #need to further loop
                        fused=list(set(i)|set(j))
                        if i in further_rings:further_rings.remove(i)
                        if j in further_rings:further_rings.remove(j)
                        if fused not in further_rings:further_rings.append(fused)
            fragment_rings=further_rings[:]
            count+=1
        self.lonely_ring=lonely[:]
        self.fragment_rings=fragment_rings[:]
##        print "Run",count-1,"times to find all the fused fragment!"
        self.conect_of_ring()

    ##find the conect of the ring in fragment.It need to offer the fragment information.
    def conect_of_ring(self,conects={},ring_atoms=[],fragment_rings=[[]]):
        if conects=={}:conects=self.atom_conects
        if ring_atoms==[]:ring_atoms=self.ring_atoms
        if fragment_rings==[[]]:fragment_rings=self.fragment_rings
        elif fragment_rings==[]:fragment_rings=[ring_atoms]
        conects_ring={}
        for i in ring_atoms:
            conects_ring[i]=[]
            for frag in fragment_rings:
                if i in frag:
                    ring_frag=frag
                    break
            for j in conects[i]:
                if j in ring_frag:
                    conects_ring[i].append(j)
                elif j not in self.ring_link_atoms:
                    biring=[i,j]
                    biring.sort()
                    if biring not in self.biring_atoms:
                        self.biring_atoms.append(biring)
        return conects_ring

    ##count the atom numbers in fragment of the assigned atom.
    def count_atoms(self,atom,conect):
        count_atom=set([atom])
        no_proc=set([atom])
        need_proc=set([])
        proc=set([])
        connect=deepcopy(conect)
        while True:
            count=deepcopy(count_atom)
            for i in no_proc:
                count.update(connect[i])
                for j in connect[i]:
                    if j not in no_proc and j not in proc: need_proc.add(j)
                proc.add(i)
            if count==count_atom:break
            count_atom=deepcopy(count)
            no_proc=need_proc
            need_proc=set([])
        return count_atom

    ##count the fragment in the conects.
    def count_fragment(self,conects):
        fragment_set=[]
        processed=set([])
        for atom in conects:
            if atom not in processed:
                fragment=self.count_atoms(atom,conects)
                fragment_set.append(fragment)
                processed.update(fragment)
        return fragment_set

    ##judge whether the fragment contains ring
    def judge_ring_fragment(self,fragment):
        for i in fragment:
            if i in self.ring_atoms:
                return True
        return False

    ##fragmentate the molecule to fragment larger>3. One atom molecule dont contain conect information.
    def fragmentation(self,fragnum):
        #exclude the molecule<3/4 atoms. Retain its conect.
        for i in self.count_fragment(self.atom_conects):
            if len(i)<fragnum:####
                self.fragments.append(set(i))
                for j in i:
                    self.fragments_conects[j]=self.atom_conects[j]
                    del self.atom_conects[j]
        conects_origin=deepcopy(self.atom_conects)#as reference
        reconects=deepcopy(self.conect_of_ring())#initial the saved conects.Ring retain.
        conects=self.atom_conects      
        for i in conects:
            if i not in self.ring_atoms:reconects[i]=[]
        for i in self.ring_link_atoms:#cut the bond link to the rings.
            for j in self.ring_link_atoms[i]:
                self.cut(i,j)
        for i in self.ring_atoms:del conects[i]
        lonely={}
        fragments=self.count_fragment(conects)#fragments after del the ring.
        for i in fragments:
            if len(i)==fragnum:#directly retain the small fragment.#####
                for j in i:
                    reconects[j]=conects[j][:]
                    del conects[j]                    
            elif len(i)<fragnum:#the small fragment<3/4 atoms keep to last to process.#####
                for j in i:
                    if j in self.sidechain_atoms: #the small fragment linked to ring firstly processed.
                        reconects[j]=conects_origin[j][:]
                        for k in reconects[j]:
                            if k in self.ring_atoms:
                                reconects[k].append(j)
                    else:lonely[j]=conects[j][:]
                    del conects[j]
        fragments=self.count_fragment(conects)


        while conects!={}:#all atoms have been processed/
            startpoint=[]
            temp=deepcopy(conects)
            for i in temp:
                if len(temp[i])==1: #save the end point to restart.
                    startpoint.append(i)
                elif len(temp[i])==0: #at the end of some loop, single atoms form.
                    del conects[i]

            for i in startpoint:
                start=i
                if conects[i]==[]:pass #the end of the fragment.
                else:
                    reach=conects[i][0]
                    self.cut(start,reach)#cut the bond and del start point.
                    #if start point's fragment less than 3 atoms,conect to next atoms.
                    if len(self.count_atoms(start,reconects))<fragnum: #####
                        self.rebond(start,reach,reconects)
                del conects[start]                    
        #some new small fragment<3/4 generated during fragmentation.
        for i in self.count_fragment(reconects):
            if len(i)<fragnum:#####
                for j in i:
                    if j not in lonely:
                        reconects[j]=[] #del its conect(2 atom fragment)
                        lonely[j]=[] #save to lonely atoms.
        loop=True
        while loop:
            loop=False
            lonely_copy=deepcopy(lonely)
            for i in lonely:
                frag_min=250
                for j in conects_origin[i]: #the nearby atoms and their fragment volume.
                    frag_len=len(self.count_atoms(j,reconects))
                    if frag_len>=fragnum:#######
                        if frag_len<frag_min: #link to the smallest fragment.
                                    frag_min=len(self.count_atoms(j,reconects))
                                    reach=j
                if frag_min==250: #the nearby is too small,to exclude the non-process middle atom in fragment containing 3 atoms.
                    loop=True #Need further loop.
                    continue                                      
                self.rebond(i,reach,reconects)
                del lonely_copy[i]
            lonely=deepcopy(lonely_copy)
        fragments_set=self.count_fragment(reconects)
        fragments_set.sort(sortlen)
        self.restart()
        self.fragments.extend(fragments_set)
        self.fragments_conects.update(reconects)
        return reconects
               
##Point is used to stand for the point in 3D space
class Point:
    x=99999.0
    y=99999.0
    z=99999.0    
    def __init__ (self, x, y ,z):
        self.x = x
        self.y = y
        self.z = z
        
    def coors(self):
        coor=(self.x,self.y,self.z)
        return coor
        
    def dist_to(self,apoint):
        return math.sqrt(math.pow(self.x - apoint.x,2) + math.pow(self.y - apoint.y,2) + math.pow(self.z - apoint.z,2))

    def CopyOf(self):
        return point(self.x, self.y, self.z)
    
    def average_with(self, other_point):
        return point((self.x + other_point.x) / 2.0, (self.y + other_point.y) / 2.0, (self.z + other_point.z) / 2.0)
    
    def dot_product_with(self, other_point):
        return self.x * other_point.x + self.y * other_point.y + self.z * other_point.z
    
    def length(self):
        return self.dist_to(point(0.0,0.0,0.0))
    
    def minus(self, other_point):
        return point(self.x - other_point.x, self.y - other_point.y, self.z - other_point.z)
    
    def CreatePDBLine(self):
        #if len(self.atomname) > 1: self.atomname = self.atomname[:1].upper() + self.atomname[1:].lower()
        output = "ATOM "
        #output = output + str(index).rjust(6) + self.atomname.rjust(5) + self.residue.rjust(4)
        output = output + "5".rjust(6) + "X".rjust(5) + "XXX".rjust(4)
        output = output + ("%.3f" % self.x).rjust(18)
        output = output + ("%.3f" % self.y).rjust(8)
        output = output + ("%.3f" % self.z).rjust(8)
        output = output + "X".rjust(24) # + "   " + str(uniqueID) #This last part must be removed
        return output
    
class Atom:
    def __init__(self):
        self.name=''
        self.element=''
        self.resname=''
        self.resid=0
        self.chain=''
        self.coordinates = Point(99999, 99999, 99999)
        self.x=self.coordinates.coors()[0]
        self.y=self.coordinates.coors()[1]
        self.z=self.coordinates.coors()[2]
        self.undo_coordinates = Point(99999, 99999, 99999)
        self.line=""
        self.PDBIndex = ""
        self.MOL2Index =""
        self.type=''
        self.charge=''
        self.IndeciesOfAtomsConnecting=[]
        self.in_ring=False
		
    def atom_radius(self):
        element=self.element.upper()
        if element=="H": return 1.2
        if element=="C": return 1.7
        if element=="N": return 1.55
        if element=="O": return 1.52
        if element=="F": return 1.47
        if element=="P": return 1.8
        if element=="S": return 1.8
        return 1.0 # the default
    
    # function to determine if the atom belongs to a protein
    # returns true or false
    def belongs_to_protein(self):
        protein_residues = ["ALA", "ARG", "ASN", "ASP", "CYS", "GLN", "GLU", "GLY", "HIS", "ILE", "LEU", "LYS", "MET", "PHE", "PRO", "SER", "THR", "TRP", "TYR", "VAL"]
        if self.resname.strip() in protein_residues: return True
        else: return False

    def CopyOf(self):
        newatom = Atom()
        newatom.chain = self.chain
        newatom.resid = self.resid
        newatom.atomname = self.atomname
        newatom.resname = self.resname
        newatom.coordinates = self.coordinates.CopyOf()
        newatom.undo_coordinates = self.undo_coordinates.CopyOf()
        newatom.element = self.element
        newatom.PDBIndex = self.PDBIndex
        newatom.line = self.line
        for index in self.IndeciesOfAtomsConnecting:
            newatom.IndeciesOfAtomsConnecting.append(index)
        return newatom

    # Reads text (PDB format) into an atom object
    # Requires: A string containing the PDB line
    def ReadPDBLine(self, Line):
        self.line = Line
        self.atomname = Line[12:16].strip()
        self.chain = Line[21:22]
        if Line[22:26].strip() != "":
            self.resid = int(Line[22:26])
        else:
            self.resid = 0
        
        if len(self.atomname)==1: # redo using rjust
            self.atomname = self.atomname + "  "
        elif len(self.atomname)==2:
            self.atomname = self.atomname + " "
        elif len(self.atomname)==3:
            self.atomname = self.atomname + " " # This line is necessary for babel to work, though many PDBs in the PDB would have this line commented out
        
        self.coordinates = Point(float(Line[30:38]), float(Line[38:46]), float(Line[46:54]))
        
        if len(Line) >= 79:
            self.element = Line[76:78].strip().upper() # element specified explicitly at end of life
            self.charge = Line [78:80].strip()
        elif self.element == "": # try to guess at element from name
            two_letters = self.atomname[0:2].strip().upper()
            if two_letters=='BR':
                self.element='BR'
            elif two_letters=='CL':
                self.element='CL'
            elif two_letters=='BI':
                self.element='BI'
            elif two_letters=='AS':
                self.element='AS'
            elif two_letters=='AG':
                self.element='AG'
            elif two_letters=='LI':
                self.element='LI'
            elif two_letters=='HG':
                self.element='HG'
            elif two_letters=='MG':
                self.element='MG'
            elif two_letters=='RH':
                self.element='RH'
            elif two_letters=='ZN':
                self.element='ZN'
            else: #So, just assume it's the first letter.
                self.element = self.atomname[0:1].strip().upper()
                
        # Any number needs to be removed from the element name
        self.element = self.element.replace('0','')
        self.element = self.element.replace('1','')
        self.element = self.element.replace('2','')
        self.element = self.element.replace('3','')
        self.element = self.element.replace('4','')
        self.element = self.element.replace('5','')
        self.element = self.element.replace('6','')
        self.element = self.element.replace('7','')
        self.element = self.element.replace('8','')
        self.element = self.element.replace('9','')

        self.PDBIndex = Line[6:11].strip()
        self.resname = Line[17:20]
        if self.resname.strip() == "": self.resname = " MOL"
        
    # Creates a PDB line from the atom object
    # Returns: PDB String
    def CreatePDBLine(self):
        output = "ATOM".ljust(6)
        output = output + self.PDBIndex.rjust(5) + ' '
        if len(self.element)==2:output = output + self.atomname.ljust(5) #the strang atom name rule...' C1 'and 'Si  '
        elif len(self.element)==1:output = output + ' ' + self.atomname.ljust(4)
        output = output + self.resname.rjust(3)+self.chain.rjust(2)+str(self.resid).rjust(4)
        output = output + ("%.3f" % self.coordinates.x).rjust(12)
        output = output + ("%.3f" % self.coordinates.y).rjust(8)
        output = output + ("%.3f" % self.coordinates.z).rjust(8)
        output = output + self.element.rjust(24)+ self.charge.ljust(2)# + "   " + str(uniqueID) #This last part must be removed
        return output

    def ReadMOL2Line(self, Line):
        self.line = Line
        items=Line.split()
        self.MOL2Index = items[0]
        self.atomname = items[1]
        self.chain = ''
        self.coordinates = Point(float(items[2]), float(items[3]), float(items[4]))
        self.type=items[5]
        self.element=self.type[0:2].strip('.')
        if len(items)==9:
            self.resid = int(items[6])
            self.resname = items[7]
            self.charge = items[8]

    def CreateMOL2Line(self, mol2):
        if mol2.len_atom==0:
            len_atom=4
            len_resid=3
            len_resname=6
        else:
            len_atom=mol2.len_atom
            len_resid=mol2.len_resid
            len_resname=mol2.len_resid
        output=self.MOL2Index.rjust(len_atom)+ ' ' +self.atomname.ljust(5)
        output=output+("%.4f" % self.coordinates.x).rjust(10) + ("%.4f" % self.coordinates.y).rjust(11)+ ("%.4f" % self.coordinates.z).rjust(11)+ ' '
        output=output+self.type.ljust(6)+str(self.resid).rjust(len_resid)+ ' ' + self.resname.ljust(len_resname)+ self.charge.rjust(9)+ '\n'
        return output
    
# PDB class
class PDB:
    def __init__ (self):
        self.AllAtoms={}
        self.Conects=Conect()
        self.heavy_atoms_Conects=Conect()
        self.hydrogens=[]
        self.non_hydrogens=[]
        self.filename=''

    # Loads a PDB from a file
    # Requires: FileName, a string containing the filename
    def LoadPDB(self, FileName):
        autoindex = 1
        self.__init__()
        # Now load the file into a list
        file = open(FileName,"r")
        lines = file.readlines()
        file.close()
        self.filename=FileName
        conects=[]
        for t in range(0,len(lines)):
            line=lines[t]
            if len(line) >= 7:
                if line[0:4]=="ATOM" or line[0:6]=="HETATM": # Load atom data (coordinates, etc.)
                    TempAtom = Atom()
                    TempAtom.ReadPDBLine(line)
                    self.AllAtoms[autoindex] = TempAtom # because points files have no indecies
                    autoindex = autoindex + 1
            items=line.split()
            if items[0]=='CONECT':
                conects.append(items[1:])
        self.Conects.conects=conects[:]
        self.Conects.restart()
        self.Conects.find_ring_atoms()
        if len(self.AllAtoms)>len(self.Conects.atoms): #molecule only single atom will loss his conects.
            for i in self.AllAtoms:
                if self.AllAtoms[i].PDBIndex not in self.Conects.atoms:
                    self.Conects.fragments.append(set(self.AllAtoms[i].PDBIndex))#firstly add to fragment lib.
                    self.heavy_atoms_Conects.fragments.append(set([self.AllAtoms[i].PDBIndex]))
                    self.Conects.atoms_index[self.AllAtoms[i].PDBIndex]=i #add to atom-Allatom_index
                    self.heavy_atoms_Conects.atoms_index[self.AllAtoms[i].PDBIndex]=i
                    print 'Atom',self.AllAtoms[i].PDBIndex,'is a single atom!!'
        heavyconects=[]
        hydrogens={}
        for i in self.Conects.conects: #build the atoms_index and find the non-hydrogen atoms.
            for j in self.AllAtoms:
                if i[0]==self.AllAtoms[j].PDBIndex:
                    self.Conects.atoms_index[i[0]]=j
                    if self.AllAtoms[j].element!='H':
                        heavyconects.append(i)
                        self.heavy_atoms_Conects.atoms_index[i[0]]=j
                    elif self.AllAtoms[j].element=='H':
                        hydrogens[i[0]]=j
        copy_heavy=deepcopy(heavyconects)
        for i in copy_heavy:
            for j in i:
                if j in hydrogens:
                    heavyconects[copy_heavy.index(i)].remove(j)
        self.heavy_atoms_Conects.conects=heavyconects[:]
        self.heavy_atoms_Conects.restart()
        self.heavy_atoms_Conects.find_ring_atoms()        
        
    # Save the fragments to each file at the directory of the molecule.
    def savefragments_each(self):
        count=1
        if not os.path.exists(self.filename[:-4]+os.sep):os.mkdir(self.filename[:-4]+os.sep)
        for i in self.heavy_atoms_Conects.fragments:
            if len(i)==1: #special case when mol contains only one atom
                filepdb = open(self.filename[:-4]+os.sep+os.path.basename(self.filename)[:-4]+'_'+'Single_'+str(count).rjust(4,'0')+'.pdb',"w")
                filepdb.write(self.AllAtoms[self.heavy_atoms_Conects.atoms_index[list(i)[0]]].CreatePDBLine() + '\n')
                filepdb.close()
                count+=1
                continue
            if self.heavy_atoms_Conects.judge_ring_fragment(i):RingOrChain='Ring' #identify the fragment containing ring or not.
            else:RingOrChain='Chain'
            filepdb = open(self.filename[:-4]+os.sep+os.path.basename(self.filename)[:-4]+'_'+ RingOrChain + '_' +str(count).rjust(4,'0')+'.pdb',"w")
            for j in i:
                filepdb.write(self.AllAtoms[self.heavy_atoms_Conects.atoms_index[j]].CreatePDBLine() + '\n')
            for j in i:
                filepdb.write('CONECT'+j.rjust(5))
                for k in self.heavy_atoms_Conects.fragments_conects[j]:
                    filepdb.write(k.rjust(5))
                filepdb.write('\n')
            filepdb.close()
            count+=1

class MOL2:
    def __init__(self):
        self.AllAtoms={}
        self.Conects=Conect()
        self.hydrogens=[]#the mol2index,not atom index
        self.non_hydrogens=[]
        self.heavy_atoms_Conects=Conect()
        self.bonds={}
        self.filename=''
        self.len_atom=0
        self.len_resid=0
        self.len_resname=0
        
    def LoadMOL2(self, FileName):
        autoindex = 1
        self.__init__()
        # Now load the file into a list
        file = open(FileName,"r")
        lines = file.readlines()
        file.close()
        self.filename=FileName
        save_atoms=False
        save_bonds=False
        bonds={}
        self.Conects.read_conects_MOL2(FileName)
        for line in lines:
            if '@<TRIPOS>ATOM' in line:
                save_atoms=True #the next line to save.
                continue
            if save_atoms:
                if line[0]!='@' and line!='\n' and line!='':
                    TempAtom = Atom()
                    TempAtom.ReadMOL2Line(line)
                    self.AllAtoms[autoindex] = TempAtom                
                    if TempAtom.element=='H':
                        self.hydrogens.append(TempAtom.MOL2Index)
                    else:
                        self.non_hydrogens.append(TempAtom.MOL2Index)                                        
                    autoindex = autoindex + 1
                else:save_atoms=False #reach the end.
            #read the non-hydrogen bond and save to    
            if '@<TRIPOS>BOND' in line:
                save_bonds=True
                continue
            if save_bonds:
                if line[0]!='@' and line!='\n' and line!='':
                    items=line.split()#bond in mol2:num atom1 atom2 bond_level
                    bonds[(items[1],items[2])]=items[3]
                    bonds[(items[2],items[1])]=items[3]
                    if items[1] not in self.hydrogens and items[2] not in self.hydrogens:
                        if items[1] not in self.heavy_atoms_Conects.atom_conects:self.heavy_atoms_Conects.atom_conects[items[1]]=[]
                        if items[2] not in self.heavy_atoms_Conects.atom_conects:self.heavy_atoms_Conects.atom_conects[items[2]]=[]
                        self.heavy_atoms_Conects.atom_conects[items[1]].append(items[2])
                        self.heavy_atoms_Conects.atom_conects[items[2]].append(items[1])
                else:
                    save_bonds=False
                    break #break for some mol2 containing more than one molecule.
        if len(self.AllAtoms)>len(self.Conects.atoms): #special case when molecules contain only one atom.
            for i in self.AllAtoms:
                if self.AllAtoms[i].MOL2Index not in self.Conects.atoms:
                    self.Conects.fragments.append(set(self.AllAtoms[i].MOL2Index))
                    self.heavy_atoms_Conects.fragments.append(set([self.AllAtoms[i].MOL2Index]))
                    self.Conects.atoms_index[self.AllAtoms[i].MOL2Index]=i
                    self.heavy_atoms_Conects.atoms_index[self.AllAtoms[i].MOL2Index]=i
                    print 'Atom',self.AllAtoms[i].MOL2Index,'is a single atom!!'
        heavyconects=[]
        for i in self.Conects.conects: #add to atom_index
            for j in self.AllAtoms:
                if i[0]==self.AllAtoms[j].MOL2Index:
                    self.Conects.atoms_index[i[0]]=j
        for i in self.heavy_atoms_Conects.atom_conects:
            conect=[i]
            conect.extend(self.heavy_atoms_Conects.atom_conects[i])
            heavyconects.append(conect)
        self.bonds=deepcopy(bonds)
        self.heavy_atoms_Conects.bonds=deepcopy(bonds)
        self.heavy_atoms_Conects.conects=deepcopy(heavyconects)
        self.heavy_atoms_Conects.restart()
        self.heavy_atoms_Conects.find_ring_atoms()

    def savefragments_each(self):
        count=1
        lenatom=self.len_atom
        RingOrChain=''
        if not os.path.exists(self.filename[:-5]+os.sep):os.mkdir(self.filename[:-5]+os.sep)                
        for i in self.heavy_atoms_Conects.fragments:
            if len(i)==1: #special case for mol contains only one atom
                filepdb = open(self.filename[:-4]+os.sep+os.path.basename(self.filename)[:-4]+'_'+'Single_'+str(count).rjust(4,'0')+'.pdb',"w")
                filepdb.write(self.AllAtoms[self.heavy_atoms_Conects.atoms_index[list(i)[0]]].CreatePDBLine() + '\n')
                filepdb.close()
                count+=1
                continue
            if self.heavy_atoms_Conects.judge_ring_fragment(i):RingOrChain='Ring'
            else:RingOrChain='Chain'
            frag_bond_num=0
            bonds=[]
            bond_lines=[]
            frag_atom_index={}
            atom_index=1
            for atom in i:
                frag_atom_index[atom]=atom_index
                atom_index+=1
            for j in i: #add to bond information
                for k in self.heavy_atoms_Conects.fragments_conects[j]:
                    if set([j,k]) not in bonds:
                        frag_bond_num+=1
                        bonds.append(set([j,k]))
                        bond_line=str(frag_bond_num).rjust(lenatom)+' '+str(frag_atom_index[j]).rjust(lenatom)+' '+ str(frag_atom_index[k]).rjust(lenatom)+' '+self.bonds[(k,j)].ljust(5)+'\n'
                        bond_lines.append(bond_line)
            filemol2 = open(self.filename[:-5]+os.sep+os.path.basename(self.filename)[:-5]+'_'+ RingOrChain + '_' + str(count).rjust(4,'0')+'.mol2',"w")
            filemol2.write('@<TRIPOS>MOLECULE\n'+os.path.basename(self.filename)[:-5]+'_'+ RingOrChain + '_' +str(count).rjust(4,'0')+'\n')
            filemol2.write(str(len(i))+'\t'+str(frag_bond_num)+'\t'+'0\t'+'0\t'+'0\n')
            filemol2.write('SMALL\nUSER_CHARGES\n')
            filemol2.write('@<TRIPOS>ATOM\n')
            for j in i:
                atom_line=self.AllAtoms[self.Conects.atoms_index[j]].CreateMOL2Line(self)
                atom_line=atom_line.replace(j,str(frag_atom_index[j]).rjust(len(j)),1)
                filemol2.write(atom_line)
            filemol2.write('@<TRIPOS>BOND\n')
            for line in bond_lines:
                filemol2.write(line)
            filemol2.write('\n')
            filemol2.close()
            count+=1

                
# Load in command-line variables.
# Returns: a dictionary containing user-defined values
def get_commandline_parameters():
	# now get the defaults from the commandline
    print "Reading parameters from the commandline..."
    argv = {}
    keywords = ['-fragnum','files']
    argv['-fragnum']=3
    input_file=[]
    argv_used=[]
    for i in sys.argv[1:]:
        if i not in keywords and i not in argv_used:
            input_file.append(i)
        if i == '-fragnum':
            argv['-fragnum']=int(sys.argv[sys.argv.index('-fragnum')+1])
            print 'fragnum is set to',sys.argv[sys.argv.index('-fragnum')+1]
            argv_used.append(sys.argv[sys.argv.index('-fragnum')+1])
    molfiles=set([])
    for i in input_file:
        found=glob.glob(i)
        if len(found)==0: # does exist, so throw error
            print "ERROR The file doesn's exist! Please check it."
            sys.exit(0)
        else: molfiles.update(found)
    print "The following files will be handled:"
    for i in molfiles:
        print '"'+i+'"',
    raw_input('Please enter any key to confirm, or close the program by Ctrl+C')
    argv['files']=list(molfiles)
    return argv

argv=get_commandline_parameters()
molfiles=argv['files']
filep=os.path.dirname(os.path.abspath(molfiles[0]))
if not os.path.exists(filep+os.sep+'processed'):os.mkdir(filep+os.sep+'processed')
for i in molfiles:
    if i[-4:]=='.pdb':
        print 'PDB process',i
        pdb=PDB()
        pdb.LoadPDB(i)
        pdb.heavy_atoms_Conects.fragmentation(argv['-fragnum'])
        pdb.savefragments_each()
        shutil.move(i,filep+os.sep+'processed')
    elif i[-5:]=='.mol2':
        print 'MOL2 process',i
        mol2=MOL2()
        mol2.LoadMOL2(i)
        mol2.heavy_atoms_Conects.fragmentation(argv['-fragnum'])
        mol2.savefragments_each()
        shutil.move(i,filep+os.sep+'processed')

##i="D:\Documents and Settings\zhaozx\Desktop\ligand_test-2.pdb"
##pdb=PDB()
##pdb.LoadPDB(i)
##pdb.heavy_atoms_Conects.fragmentation(3)
##pdb.savefragments_each()

##f=r'C:\Users\Hom\Desktop\single.mol2'
##mol2=MOL2()
##mol2.LoadMOL2(f)
##mol2.heavy_atoms_Conects.fragmentation()
##mol2.savefragments_each()
    
##f='C:\Users\Hom\Desktop\ligand_ring2.mol2'
##b=Conect()
##b.read_conects_MOL2(f)
##b.fragmentation()
    
print 'OK!'
raw_input('Finished,press any key to exit.')
~~~

------
