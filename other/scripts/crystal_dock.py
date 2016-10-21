# CrystalDock is released under the GNU General Public License (see http://www.gnu.org/licenses/gpl.html).
# If you have any questions, comments, or suggestions, please don't hesitate to contact me,
# Jacob Durrant, at jdurrant [at] ucsd [dot] edu.
#
# If you use CrystalDock in your work, please cite [REFERENCE HERE]
 
import math
import sys
import time
import glob
import os
import scipy.optimize
import numpy
from operator import itemgetter, attrgetter
import multiprocessing 
import cPickle
import multiprocessing #import Process
import shutil
import textwrap
import platform
 
starttime = time.time()
 
version = "1.0.0"
#database_dir = "/u1/jdurrant/crystal_dock/whole_pdb/withligands/3.4_angstroms_v2/9.database_2" # database_dir is a string showing the directory with all fragments
#if database_dir[-1:] != os.sep: database_dir = database_dir + os.sep 
 
start_time = time.time()
 
def reference(before=""):
    global version
    print before + "CrystalDock " + version
    print before + "================="
    print ""
    print before + "If you use CrystalDock in your research, please cite the following reference:"
    print before + "  {REFERENCE HERE}"
 
# Requires: String containing element name
# Returns: VDW radius
def get_vdw(element):
        if element=="H": return 1.2
        if element=="C": return 1.7
        if element=="N": return 1.55
        if element=="O": return 1.52
        if element=="F": return 1.47
        if element=="P": return 1.8
        if element=="S": return 1.8
    return 1.0 # the default
 
# a geometric point
class point:
    x=99999.0
    y=99999.0
    z=99999.0
     
    def __init__ (self, x, y ,z):
        self.x = x
        self.y = y
        self.z = z
 
    def print_coors(self):
        print str(self.x)+"\t"+str(self.y)+"\t"+str(self.z)
         
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
     
# an atom object
class atom:
         
    def __init__ (self):
        self.atomname = ""
        self.resid = 0
        self.chain = ""
        self.resname = ""
        self.coordinates = point(99999, 99999, 99999)
        self.undo_coordinates = point(99999, 99999, 99999)
        self.element = ""
        self.PDBIndex = ""
        self.line=""
        self.IndeciesOfAtomsConnecting=[]
 
    # function to determine if the atom belongs to a protein
    # returns true or false
    def belongs_to_protein(self):
        protein_residues = ["ALA", "ARG", "ASN", "ASP", "CYS", "GLN", "GLU", "GLY", "HIS", "ILE", "LEU", "LYS", "MET", "PHE", "PRO", "SER", "THR", "TRP", "TYR", "VAL"]
        if self.resname.strip() in protein_residues: return True
    else: return False
 
    def CopyOf(self):
        newatom = atom()
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
        self.atomname = Line[11:16].strip()
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
         
        self.coordinates = point(float(Line[30:38]), float(Line[38:46]), float(Line[46:54]))
         
        if len(Line) >= 79:
            self.element = Line[76:79].strip().upper() # element specified explicitly at end of life
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
 
        self.PDBIndex = Line[6:12].strip()
        self.resname = Line[16:20]
        if self.resname.strip() == "": self.resname = " MOL"
 
    # Creates a PDB line from the atom object
    # Returns: PDB String
    def CreatePDBLine(self):
 
        #if len(self.atomname) > 1: self.atomname = self.atomname[:1].upper() + self.atomname[1:].lower()
 
        output = "ATOM "
        #output = output + str(index).rjust(6) + self.atomname.rjust(5) + self.residue.rjust(4)
        output = output + self.PDBIndex.rjust(6) + self.atomname.rjust(5) + self.resname.rjust(4)
        output = output + ("%.3f" % self.coordinates.x).rjust(18)
        output = output + ("%.3f" % self.coordinates.y).rjust(8)
        output = output + ("%.3f" % self.coordinates.z).rjust(8)
        output = output + self.element.rjust(24) # + "   " + str(uniqueID) #This last part must be removed
        return output
 
    # Sets the undo point for later undoing
    def SetUndoPoint(self):
        self.undo_coordinates = self.coordinates.CopyOf()
         
    # Resets coordinate values after translations or rotations ("Undo")
    def Undo(self):
        self.coordinates = self.undo_coordinates.CopyOf()
    
# PDB class
class PDB:
 
    def __init__ (self):
        self.AllAtoms={}
 
    # Loads a PDB from a file
    # Requires: FileName, a string containing the filename
    def LoadPDB(self, FileName):
 
        autoindex = 1
 
        self.__init__()
         
        # Now load the file into a list
        file = open(FileName,"r")
        lines = file.readlines()
        file.close()
         
        for t in range(0,len(lines)):
            line=lines[t]
            if len(line) >= 7:
                if line[0:4]=="ATOM" or line[0:6]=="HETATM": # Load atom data (coordinates, etc.)
                    TempAtom = atom()
                    TempAtom.ReadPDBLine(line)
                     
                    self.AllAtoms[autoindex] = TempAtom # because points files have no indecies
                    autoindex = autoindex + 1
 
    # Saves the PDB object to a PDB file
    # Requires: filename to be saved
    def SavePDB(self, filename):
 
        if len(self.AllAtoms) > 0: # so the pdb is not empty (if it is empty, don't save)
 
            file = open(filename,"w")
 
            # write coordinates
            for atomindex in self.AllAtoms:
                file.write(self.AllAtoms[atomindex].CreatePDBLine() + "\n")
 
            file.close()
 
    # identifies the greatest distance between any two atoms of the PDB
    # Used for quickly comparing two PDBs so RMSD alignment not necessary if they're different
    # Returns float = distance
    def farthest_away_atoms_dist(self):
    dist_max = 0.0
    keys = self.AllAtoms.keys()
    for key_index1 in range(0,len(keys)-1):
        key1 = keys[key_index1]
        atom1 = self.AllAtoms[key1]
        for key_index2 in range(key_index1+1,len(keys)):
        key2 = keys[key_index2]
        atom2 = self.AllAtoms[key2]
        dist = atom1.coordinates.dist_to(atom2.coordinates)
        if dist > dist_max: dist_max = dist
    self.max_inter_atom_distance = dist_max
    return dist_max
 
    # identifies the smallest distance between any two atoms of the PDB
    # Used for quickly comparing two PDBs so RMSD alignment not necessary if they're different
    # Returns float = distance
    def closest_atoms_dist(self):
    dist_min = 999999999.99
    keys = self.AllAtoms.keys()
    for key_index1 in range(0,len(keys)-1):
        key1 = keys[key_index1]
        atom1 = self.AllAtoms[key1]
        for key_index2 in range(key_index1+1,len(keys)):
        key2 = keys[key_index2]
        atom2 = self.AllAtoms[key2]
        dist = atom1.coordinates.dist_to(atom2.coordinates)
        if dist < dist_min: dist_min = dist
    self.min_inter_atom_distance = dist_min
    return dist_min
    
    # Creates a "distance fingerprint" so PDB's can be quickly compared w/o RMSD alignment
    # Returns: a list containing sorted distances
    def distance_fingerprint(self):
    fingerprint = []
    keys = self.AllAtoms.keys()
    for key_index1 in range(0,len(keys)-1):
        key1 = keys[key_index1]
        atom1 = self.AllAtoms[key1]
        for key_index2 in range(key_index1+1,len(keys)):
        key2 = keys[key_index2]
        atom2 = self.AllAtoms[key2]
        dist = atom1.coordinates.dist_to(atom2.coordinates)
        fingerprint.append(dist)
    fingerprint.sort()
    self.distance_fingerprint = fingerprint
    return fingerprint
 
    # To detect if two distance fingerprints are sufficiently similar
    # Requires: Two fingerprints (lists) and a tolerance (float)
    # Returns: True or False
    def fingerprint_same_as(self, fingerprint, tol):
        if len(self.distance_fingerprint) <> len(fingerprint): return False
     
        for index in range(len(self.distance_fingerprint)):
            item1 = self.distance_fingerprint[index]
            item2 = fingerprint[index]
            if math.fabs(item1-item2) > tol: return False
        return True
 
    # Print out info about the PDB
    def print_out_info(self):
        for index in self.AllAtoms:
            print self.AllAtoms[index].CreatePDBLine()
 
    # Translate the molecule
    def TranslateMolecule(self, x, y, z):
        for atomindex in self.AllAtoms:
            self.AllAtoms[atomindex].coordinates.x = self.AllAtoms[atomindex].coordinates.x + x
        self.AllAtoms[atomindex].coordinates.y = self.AllAtoms[atomindex].coordinates.y + y
        self.AllAtoms[atomindex].coordinates.z = self.AllAtoms[atomindex].coordinates.z + z
 
    # Rotate the PDB around it's center.
    # Requires: degrees to rotate, as float
    def RotatePDB(self, thetax, thetay, thetaz):
         
    # first, identify the geometric center
    x = 0.0
    y = 0.0
    z = 0.0
    count = 0
    for index in self.AllAtoms:
        if self.AllAtoms[index].element != "H":
            count = count + 1
            x = x + self.AllAtoms[index].coordinates.x
            y = y + self.AllAtoms[index].coordinates.y
            z = z + self.AllAtoms[index].coordinates.z
    x = x / count
    y = y / count
    z = z / count
     
    # now, move the pdb to the origin
    self.TranslateMolecule(-x, -y, -z)
     
        # now rotate
        sinx = math.sin(thetax)
        siny = math.sin(thetay)
        sinz = math.sin(thetaz)
        cosx = math.cos(thetax)
        cosy = math.cos(thetay)
        cosz = math.cos(thetaz)
 
        cosy_cosz = cosy * cosz
        sinx_siny_cosz_plus_cosx_sinz = sinx * siny * cosz + cosx * sinz
        sinx_sinz_minus_cosx_siny_cosz = sinx * sinz - cosx * siny * cosz
        cosy_sinz = cosy * sinz
        cosx_cosz_minus_sinx_siny_sinz = cosx * cosz - sinx * siny * sinz
        cosx_siny_sinz_plus_sinx_cosz = cosx * siny * sinz + sinx * cosz
        sinx_cosy = sinx * cosy
    cosx_cosy = cosx * cosy
         
 
        for atomindex in self.AllAtoms: 
            vector = self.AllAtoms[atomindex].coordinates
             
            new_x = vector.x * cosy_cosz + vector.y * sinx_siny_cosz_plus_cosx_sinz + vector.z * sinx_sinz_minus_cosx_siny_cosz
            new_y = -vector.x * cosy_sinz + vector.y * cosx_cosz_minus_sinx_siny_sinz + vector.z * cosx_siny_sinz_plus_sinx_cosz
            new_z = vector.x * siny - vector.y * sinx_cosy + vector.z * cosx_cosy
     
            self.AllAtoms[atomindex].coordinates = point(new_x, new_y, new_z)
         
    # now move it back from the origin
    self.TranslateMolecule(x, y, z)
 
    # Same as with the atom class
    def SetUndoPoint(self): # you can restore all atom positions to some undo point. This sets that point.
        for atomindex in self.AllAtoms:
            self.AllAtoms[atomindex].SetUndoPoint()
             
    def Undo(self):
        for atomindex in self.AllAtoms:
            self.AllAtoms[atomindex].Undo()
 
# Load in command-line variables.
# Returns: a dictionary containing user-defined values
def get_commandline_parameters():
     
    # set the commandline-variable defaults
    vars = {}
    keywords = ['microenvironment_database_directory', 'use_microenvironments_of_3_residues', 'use_microenvironments_of_4_residues', 'use_microenvironments_of_5_residues', 'filter_step_four_side_chain_angle_cutoff', 'num_processors', 'filter_steps_one_and_two_tolerance', 'filter_step_three_CA_rmsd_cutoff', 'filter_step_five_rmsd_cutoff', 'filter_step_six_steric_clash_cutoff', 'receptor_pdb_file', 'user_specified_residue', 'pocket_center_x', 'pocket_center_y', 'pocket_center_z', 'pocket_radius', 'output_directory']
    vars['num_processors'] = multiprocessing.cpu_count()
    vars['filter_steps_one_and_two_tolerance'] = 2.0
    vars['filter_step_three_CA_rmsd_cutoff'] = 2.5
    vars['filter_step_four_side_chain_angle_cutoff'] = 100.0
    vars['filter_step_five_rmsd_cutoff'] = 1.5
    vars['filter_step_six_steric_clash_cutoff'] = 2.0
    vars['receptor_pdb_file'] = ''
    #vars['user_specified_residue'] = '371_ARG_A 118_ARG_A 292_ARG_A 406_TYR_A 347_TYR_A'
    vars['user_specified_residue'] = ''
    vars['pocket_center_x'] = 0.0
    vars['pocket_center_y'] = 0.0
    vars['pocket_center_z'] = 0.0
    vars['pocket_radius'] = 5 # must be integer
    vars['output_directory'] = '.' + os.sep
    vars['microenvironment_database_directory'] = sys.path[0] + os.sep + 'microenvironment_database' + os.sep
     
     
    vars['use_microenvironments_of_3_residues'] = "TRUE"
    vars['use_microenvironments_of_4_residues'] = "TRUE"
    vars['use_microenvironments_of_5_residues'] = "TRUE"
 
    # now get the defaults from the commandline
    print "Reading parameters from the commandline..."
    for index in range(1,len(sys.argv)):
        key = sys.argv[index].lower()
        while '-' in key: key = key.replace('-','')
 
        if key == 'microenvironment_database_directory': 
            vars['microenvironment_database_directory'] = sys.argv[index+1]
            keywords.remove('microenvironment_database_directory')
            if vars['microenvironment_database_directory'][-1:] != os.sep: vars['microenvironment_database_directory'] = vars['microenvironment_database_directory'] + os.sep
            print "     " + sys.argv[index] + " set to " + str(vars['microenvironment_database_directory'])
            sys.argv[index] = ""
            sys.argv[index+1] = ""
        if key == 'use_microenvironments_of_3_residues': 
            vars['use_microenvironments_of_3_residues'] = sys.argv[index+1].upper()
            print "     " + sys.argv[index] + " set to " + str(vars['use_microenvironments_of_3_residues'])
            if vars['use_microenvironments_of_3_residues'] != "TRUE" and vars['use_microenvironments_of_3_residues'] != "FALSE":
                print "WARNING           The commandline parameter \"-use_microenvironments_of_3_residues\" must be either \"TRUE\" or \"FALSE\". Setting it to \"TRUE\"."
                vars['use_microenvironments_of_3_residues'] = "TRUE"
            keywords.remove('use_microenvironments_of_3_residues')
            sys.argv[index] = ""
            sys.argv[index+1] = ""
        if key == 'use_microenvironments_of_4_residues': 
            vars['use_microenvironments_of_4_residues'] = sys.argv[index+1].upper()
            print "     " + sys.argv[index] + " set to " + str(vars['use_microenvironments_of_4_residues'])
            if vars['use_microenvironments_of_4_residues'] != "TRUE" and vars['use_microenvironments_of_4_residues'] != "FALSE":
                print "WARNING           The commandline parameter \"-use_microenvironments_of_4_residues\" must be either \"TRUE\" or \"FALSE\". Setting it to \"TRUE\"."
                vars['use_microenvironments_of_4_residues'] = "TRUE"
            keywords.remove('use_microenvironments_of_4_residues')
            sys.argv[index] = ""
            sys.argv[index+1] = ""
        if key == 'use_microenvironments_of_5_residues': 
            vars['use_microenvironments_of_5_residues'] = sys.argv[index+1].upper()
            print "     " + sys.argv[index] + " set to " + str(vars['use_microenvironments_of_5_residues'])
            if vars['use_microenvironments_of_5_residues'] != "TRUE" and vars['use_microenvironments_of_5_residues'] != "FALSE":
                print "WARNING           The commandline parameter \"-use_microenvironments_of_5_residues\" must be either \"TRUE\" or \"FALSE\". Setting it to \"TRUE\"."
                vars['use_microenvironments_of_5_residues'] = "TRUE"
            keywords.remove('use_microenvironments_of_5_residues')
            sys.argv[index] = ""
            sys.argv[index+1] = ""
        if key == 'filter_step_four_side_chain_angle_cutoff': 
            vars['filter_step_four_side_chain_angle_cutoff'] = float(sys.argv[index+1])
            keywords.remove('filter_step_four_side_chain_angle_cutoff')
            print "     " + sys.argv[index] + " set to " + str(vars['filter_step_four_side_chain_angle_cutoff'])
            sys.argv[index] = ""
            sys.argv[index+1] = ""
        if key == 'output_directory': 
            vars['output_directory'] = sys.argv[index+1]
            keywords.remove('output_directory')
            if vars['output_directory'][-1:] != os.sep: vars['output_directory'] = vars['output_directory'] + os.sep
            print "     " + sys.argv[index] + " set to " + str(vars['output_directory'])
            sys.argv[index] = ""
            sys.argv[index+1] = ""
        if key == 'num_processors': 
            vars['num_processors'] = int(sys.argv[index+1])
            keywords.remove('num_processors')
            print "     " + sys.argv[index] + " set to " + str(vars['num_processors'])
            sys.argv[index] = ""
            sys.argv[index+1] = ""
        if key == 'filter_steps_one_and_two_tolerance': 
            vars['filter_steps_one_and_two_tolerance'] = float(sys.argv[index+1])
            keywords.remove('filter_steps_one_and_two_tolerance')
            print "     " + sys.argv[index] + " set to " + str(vars['filter_steps_one_and_two_tolerance'])
            sys.argv[index] = ""
            sys.argv[index+1] = ""
        if key == 'filter_step_three_ca_rmsd_cutoff':
            vars['filter_step_three_CA_rmsd_cutoff'] = float(sys.argv[index+1])
            keywords.remove('filter_step_three_CA_rmsd_cutoff')
            print "     " + sys.argv[index] + " set to " + str(vars['filter_step_three_CA_rmsd_cutoff'])
            sys.argv[index] = ""
            sys.argv[index+1] = ""
        if key == 'filter_step_five_rmsd_cutoff':
            vars['filter_step_five_rmsd_cutoff'] = float(sys.argv[index+1])
            keywords.remove('filter_step_five_rmsd_cutoff')
            print "     " + sys.argv[index] + " set to " + str(vars['filter_step_five_rmsd_cutoff'])
            sys.argv[index] = ""
            sys.argv[index+1] = ""
        if key == 'filter_step_six_steric_clash_cutoff':
            vars['filter_step_six_steric_clash_cutoff'] = float(sys.argv[index+1])
            keywords.remove('filter_step_six_steric_clash_cutoff')
            print "     " + sys.argv[index] + " set to " + str(vars['filter_step_six_steric_clash_cutoff'])
            sys.argv[index] = ""
            sys.argv[index+1] = ""
        if key == 'receptor_pdb_file':
            vars['receptor_pdb_file'] = sys.argv[index+1]
            keywords.remove('receptor_pdb_file')
            print "     " + sys.argv[index] + " set to " + vars['receptor_pdb_file']
            sys.argv[index] = ""
            sys.argv[index+1] = ""
        if key == 'pocket_radius':
            error = ""
            try:
                vars['pocket_radius'] = int(sys.argv[index+1]) # note that this has to be an integer
            except ValueError:
                vars['pocket_radius'] = int(round(float(sys.argv[index+1]))) # change float to int
                error = "WARNING           The pocket radius must be an integer! The radius has been rounded..."
            keywords.remove('pocket_radius')
            print "     " + sys.argv[index] + " set to " + str(vars['pocket_radius'])
            if error != "": print error
            sys.argv[index] = ""
            sys.argv[index+1] = ""
        if key == 'user_specified_residue':
            vars['user_specified_residue'] = vars['user_specified_residue'] + sys.argv[index+1] + ' '
            if 'user_specified_residue' in keywords: keywords.remove('user_specified_residue')
            sys.argv[index] = ""
            sys.argv[index+1] = ""
        if key == 'pocket_center_x':
            vars['pocket_center_x'] = float(sys.argv[index+1])
            keywords.remove('pocket_center_x')
            print "     " + sys.argv[index] + " set to " + str(vars['pocket_center_x'])
            sys.argv[index] = ""
            sys.argv[index+1] = ""
        if key == 'pocket_center_y':
            vars['pocket_center_y'] = float(sys.argv[index+1])
            keywords.remove('pocket_center_y')
            print "     " + sys.argv[index] + " set to " + str(vars['pocket_center_y'])
            sys.argv[index] = ""
            sys.argv[index+1] = ""
        if key == 'pocket_center_z':
            vars['pocket_center_z'] = float(sys.argv[index+1])
            keywords.remove('pocket_center_z')
            print "     " + sys.argv[index] + " set to " + str(vars['pocket_center_z'])
            sys.argv[index] = ""
            sys.argv[index+1] = ""
 
    vars['user_specified_residue'] = vars['user_specified_residue'].strip()
    if vars['user_specified_residue'] != "": print "     -user_specified_residue set to " + vars['user_specified_residue']
 
    # Let the user know which commandline parameters were not specified and so were set to default values.
    if len(keywords) != 0:
        print "The following parameters were not specified and so were set to default values:"
        for keyword in keywords:
            print "     -" + keyword + ": " + str(vars[keyword])
 
    # Let the user know if any command-line parameters were not recognized
    args_not_used = ''
    for index in range(1,len(sys.argv)):
        key = sys.argv[index]
        if key != '': args_not_used = args_not_used + key.strip() + ", "
    if args_not_used != '': print "The following commandline paramters were not recognized: " + args_not_used[:-2]
 
    # check to see if the directory exists
    d = os.path.dirname(vars['output_directory'])
    if not os.path.exists(d):
        os.makedirs(d) # doesn't exist, so make it.
    else: # does exist, so throw error
        print "ERROR The output directory \""  + vars['output_directory'] + "\" already exists. Please specify an output directory that does not yet exist."
        sys.exit(0)
 
    return vars
 
# a funciton to identify the active-site residues
# Requires: the user-specified, command-line parameters
# Returns: A list containing all the active-site residues
def id_active_site_residues(vars):
    print "Identifying active-site residues..."
 
    active_site_residues = []
 
    if vars['user_specified_residue'] != '': # so the user has specified the residues to consider
        residues = vars['user_specified_residue'].split(" ")
        for residue in residues:
                residue = residue.split('_')
                active_site_residues.append((int(residue[0]), ' ' + residue[1], residue[2]))
    else: # so determine by binding-site center and radius
 
        tobreak = False
 
        for angle1 in range(0,181,10): # so rays are 10 degrees apart.
                angle1_rad = math.pi * float(angle1) / 180.0
            sin_angle1_rad = math.sin(angle1_rad)
            cos_angle1_rad = math.cos(angle1_rad)
            for angle2 in range(0,361,10):
                    angle2_rad = math.pi * float(angle2) / 180.0
                cos_angle2_rad = math.cos(angle2_rad)
                sin_angle2_rad = math.sin(angle2_rad)
                sin_angle1_rad_cos_angle2_rad = sin_angle1_rad * cos_angle2_rad
                sin_angle1_rad_sin_angle2_rad = sin_angle1_rad * sin_angle2_rad
 
                    for r in range(1,2 * vars['pocket_radius'] + 1):
                    r2 = r / 2.0 # so going out 0.5 A at a time
                            x = float(r2) * sin_angle1_rad_cos_angle2_rad + vars['pocket_center_x']
                            y = float(r2) * sin_angle1_rad_sin_angle2_rad + vars['pocket_center_y']
                            z = float(r2) * cos_angle1_rad + vars['pocket_center_z']
                    apt = point(x,y,z)
                    # now go through all the atoms in the pdb and see if there are any clashes.
                    for index in pdb.AllAtoms:
                        anatom = pdb.AllAtoms[index]
                        if math.fabs(x - anatom.coordinates.x) <=  vars['pocket_radius'] and math.fabs(y - anatom.coordinates.y) <=  vars['pocket_radius'] and math.fabs(z - anatom.coordinates.z) <=  vars['pocket_radius']:
                            dist = apt.dist_to(anatom.coordinates)
                            if dist <= get_vdw(anatom.element):
                                toadd = (anatom.resid, anatom.resname, anatom.chain)
                                if not toadd in active_site_residues: active_site_residues.append(toadd)
                                tobreak = True
                                break
                    if tobreak == True: # break out of expanding ray loop too
                        tobreak = False
                        break
 
    print "     Number of active-site residues: " + str(len(active_site_residues))
 
    #count = 0
    for count, residue in enumerate(active_site_residues):
    #for residue in active_site_residues:
    #   count = count + 1
        print "     Active-site residue #" + str(count+1) + ": resid " + str(residue[0]) + ", resname " + residue[1].strip() + ", chain " + residue[2]
 
    return active_site_residues
 
# identify all possible combinations of microenvironments from the active-site
# Requires: active_site_residues, a list of all active-site residues
# Returns: microenvironments, a list of all active-site microenvironments
def combinations_of_micro_environments(active_site_residues):
     
    global vars
     
    print "Identifying all possible microenvironments..."
 
    # get all combinations of active_site_residues
    microenvironments = []
 
    print "Identifying potential microenvironments in the active site..."
 
    # look up itertools to make this more elegant. *****
 
    # Thing to think about more: Maybe only consider groups of active-site residues that are close to each other.
 
    if vars['use_microenvironments_of_3_residues'] == "TRUE":
        if len(active_site_residues) >=3:
        print "     Finding all combinations of three protein residues..."
        for index1 in range(0, len(active_site_residues)-2):
            micro1 = active_site_residues[index1]
            for index2 in range(index1 + 1, len(active_site_residues)-1):
            micro2 = active_site_residues[index2]
            for index3 in range(index2 + 1, len(active_site_residues)):
                micro3 = active_site_residues[index3]
             
                # now go through the similarities
                for one in SIMILAR[micro1[1]]:
                for two in SIMILAR[micro2[1]]:
                    for three in SIMILAR[micro3[1]]:
                    micro1_new = (micro1[0], one, micro1[2])
                    micro2_new = (micro2[0], two, micro2[2])
                    micro3_new = (micro3[0], three, micro3[2])
                    if one == micro1[1] and two == micro2[1] and three == micro3[1]:
                        microenvironments.append((micro1_new, micro2_new, micro3_new, "EXACT")) # do these need to be alphabetized or something???
                    else:
                        #print one, two, three, micro1[1], micro2[1], micro3[1]
                        microenvironments.append((micro1_new, micro2_new, micro3_new, "SIMILAR"))
 
    if vars['use_microenvironments_of_4_residues'] == "TRUE":
        if len(active_site_residues) >=4:
        print "     Finding all combinations of four protein residues..."
        for index1 in range(0, len(active_site_residues)-3):
            micro1 = active_site_residues[index1]
            for index2 in range(index1 + 1, len(active_site_residues)-2):
            micro2 = active_site_residues[index2]
            for index3 in range(index2 + 1, len(active_site_residues)-1):
                micro3 = active_site_residues[index3]
                for index4 in range(index3 + 1, len(active_site_residues)):
                micro4 = active_site_residues[index4]
             
                # now go through the similarities
                for one in SIMILAR[micro1[1]]:
                    for two in SIMILAR[micro2[1]]:
                    for three in SIMILAR[micro3[1]]:
                        for four in SIMILAR[micro4[1]]:
                        micro1_new = (micro1[0], one, micro1[2])
                        micro2_new = (micro2[0], two, micro2[2])
                        micro3_new = (micro3[0], three, micro3[2])
                        micro4_new = (micro4[0], four, micro4[2])
                        if one == micro1[1] and two == micro2[1] and three == micro3[1] and four == micro4[1]:
                            microenvironments.append((micro1_new, micro2_new, micro3_new, micro4_new, "EXACT"))
                        else:
                            microenvironments.append((micro1_new, micro2_new, micro3_new, micro4_new, "SIMILAR"))
 
    if vars['use_microenvironments_of_5_residues'] == "TRUE":
        if len(active_site_residues) >=5:
        print "     Finding all combinations of five protein residues..."
        for index1 in range(0, len(active_site_residues)-4):
            micro1 = active_site_residues[index1]
            for index2 in range(index1 + 1, len(active_site_residues)-3):
            micro2 = active_site_residues[index2]
            for index3 in range(index2 + 1, len(active_site_residues)-2):
                micro3 = active_site_residues[index3]
                for index4 in range(index3 + 1, len(active_site_residues)-1):
                micro4 = active_site_residues[index4]
                for index5 in range(index4 + 1, len(active_site_residues)):
                    micro5 = active_site_residues[index5]
         
                    # now go through the similarities
                    for one in SIMILAR[micro1[1]]:
                    for two in SIMILAR[micro2[1]]:
                        for three in SIMILAR[micro3[1]]:
                        for four in SIMILAR[micro4[1]]:
                            for five in SIMILAR[micro5[1]]:
                            micro1_new = (micro1[0], one, micro1[2])
                            micro2_new = (micro2[0], two, micro2[2])
                            micro3_new = (micro3[0], three, micro3[2])
                            micro4_new = (micro4[0], four, micro4[2])
                            micro5_new = (micro5[0], five, micro5[2])
                            if one == micro1[1] and two == micro2[1] and three == micro3[1] and four == micro4[1] and five == micro5[1]:
                                microenvironments.append((micro1_new, micro2_new, micro3_new, micro4_new, micro5_new, "EXACT"))
                            else:
                                microenvironments.append((micro1_new, micro2_new, micro3_new, micro4_new, micro5_new, "SIMILAR"))
 
    return microenvironments
 
# A function to identify potential matching microenvironments from the database
# Requires: microenvironments, a list containing the potential microenvironments of the active site
# Returns: micros_and_filenames, a list indicated which filenames from the database correspond
#    to which microenvironments of the active-site.
def id_matching_microenvironments_from_database(microenvironments):
     
    global vars
     
    print "Identifying potential matching microenvironments from the database..."
 
    micros_and_filenames = []
    #index = 0
    total = len(microenvironments)
    #print "     Step 0 of " + str(total) + "... 0.00%"
 
    for index, micro in enumerate(microenvironments):
    #for micro in microenvironments:
    #    index = index + 1
        if index % 1000 == 0: print "     Step " + str(index) + " of " + str(total) + "... " + str(round(100.0 * float(index)/float(total),1)) + "%" # print out every 1000 steps.
        size = str(len(micro)-1) # -1 because last one was either "EXACT" or "SIMILAR"
         
        resnames = []
        for tuple in micro[:-1]: # -1 because the last one is either "EXACT" or "SIMILAR"
        resnames.append(tuple[1].strip())
        resnames.sort()
        dirname = "_".join(resnames)
         
        files = glob.glob(vars['microenvironment_database_directory'] + str(len(resnames)) + os.sep + dirname + os.sep + "full" + os.sep + "*.pickle")
         
        if len(files) > 0: micros_and_filenames.append((micro, files))
    return micros_and_filenames
 
# The function to calculate the rmsd between two ligands
# Requirements: x, a numpy array of the parameters to be optimized, and args, a tuple containing fixed parameters.
# Output: The RMSD alignment between the two proteins, a float
def calculate_rmsd(x,*args):
 
    if len(x) == 6: rotate_too = True # so it's a full alignment, rotation and translation
    else: rotate_too = False
 
    trans_x = x[0]
    trans_y = x[1]
    trans_z = x[2]
     
    if rotate_too == True:
    theta_x = x[3]
    theta_y = x[4]
    theta_z = x[5]
     
    #global pdb_to_move, pdb_to_move_CA, pdb_orig, pdb_orig_CA, JustAlphaCarbons, SIMILAR
    pdb_to_move = args[0]
    pdb_orig = args[1]
    SIMILAR = args[2]
     
    pdb_to_move.Undo()
    pdb_to_move.TranslateMolecule(trans_x, trans_y, trans_z)
     
    if rotate_too == True: pdb_to_move.RotatePDB(theta_x, theta_y, theta_z)
     
    total_dist_squared = 0.0
     
    count = 0
    for index1 in pdb_to_move.AllAtoms:
        to_move_atom = pdb_to_move.AllAtoms[index1]
        if to_move_atom.element != "H": # so ignoring hydrogens
        best_dist = 999999999.9
        for index2 in pdb_orig.AllAtoms:
            orig_atom = pdb_orig.AllAtoms[index2]
            if orig_atom.element != "H":
                if " " + to_move_atom.resname.strip() in SIMILAR[" " + orig_atom.resname.strip()] and to_move_atom.atomname.strip() == orig_atom.atomname.strip():
                    #print " " + to_move_atom.resname.strip(), SIMILAR[" " + orig_atom.resname.strip()]
                    dist = to_move_atom.coordinates.dist_to(orig_atom.coordinates)
                    if best_dist > dist:
                        best_dist = dist
 
        if best_dist != 999999999.9:
        count = count + 1
        total_dist_squared = total_dist_squared + math.pow(best_dist,2)
     
    if count == 0:
    global micro_and_filename, filename
    print micro_and_filename[0], filename
    rmsd = math.pow(total_dist_squared / count,0.5)
 
    return rmsd
 
def divide_micros_and_filenames_into_separate_lists(num_processors):
    files_per_chunck = math.floor(float(total)/float(num_processors)) + 1
    chunks = []
    for i in range(num_processors): chunks.append([])
    current_index = 0
    num_files = 0
    for micro_and_filename in micros_and_filenames:
        chunks[current_index].append(micro_and_filename)
        num_files = num_files + len(micro_and_filename[1])
        if num_files > files_per_chunck:
            num_files = 0
            current_index = current_index + 1
    return chunks
 
# the class representing a thread that can run docking jobs. Multiple threads = multiprocessing
class docking_thread:
    def __init__(self): self.dockings_so_far = 0
 
    # This is the actual function that runs the dockings
    # Required: running, mutex, a are required for multiprocessing. chunk is a list containing
    #    active-site microenvironments and associated files from the database. pdb is a pdb object
    #    of the original protein target. simplified_geometry is a large dictionary containing 
    #    information about the microenvironments from the database to allow quick comparison
    #    without the need for an RMSD alignment. SIMILAR is a dictionary containing information about
    #    which amino acids are similar to one another. vars is a dictionary containing the command-line
    #    user-specified variables.
    def value_func(self, running, mutex, chunk, pdb, simplified_geometry, SIMILAR, vars, a, show_progress = False):
 
        #print "HERE1"
 
                count_lines = 0
                total = len(chunk)
                last_percent = "0.0"
 
        for micro_and_filename in chunk:
 
                    if show_progress == True:
                        #print "moose"
                        count_lines = count_lines + 1
                        #if count_lines % 10 == 0:
                        new_percent = str(round(100*count_lines/total,1))
                        if new_percent != last_percent: print "     Step " + str(count_lines) + " of " + str(total) + "... " + new_percent + "%"
                        last_percent = str(round(100*count_lines/total,1))
 
             
            # load in the static PDB, derived from the protein PDB
            pdb_orig = PDB()
            pdb_orig_CA = PDB()
             
            count = 0
            for index in pdb.AllAtoms: # go through each of the atoms in the big pdb
            an_atom = pdb.AllAtoms[index]
            # now see if this atom is one of the ones in the identified microenvironment
            for res in micro_and_filename[0]:
                #if an_atom.resid == res[0] and an_atom.resname.strip() == res[1].strip() and an_atom.chain == res[2]:
                if an_atom.resid == res[0] and an_atom.chain == res[2]:
                count = count + 1
                if an_atom.atomname.strip() != "CA":
                    pdb_orig.AllAtoms[count] = an_atom.CopyOf()
                else:
                    toadd = an_atom.CopyOf()
                    pdb_orig.AllAtoms[count] = toadd
                    pdb_orig_CA.AllAtoms[count] = toadd
                     
            pdb_orig_max_distance = pdb_orig.farthest_away_atoms_dist() 
            pdb_orig_CA_fingerprint = pdb_orig_CA.distance_fingerprint()
 
            # now load in each of the database files, and align
            for filename in micro_and_filename[1]:
     
            self.dockings_so_far = self.dockings_so_far + 1
            a[0] = self.dockings_so_far
 
            key = os.path.basename(filename).strip()[:-7] + ".CA.pickle"
             
            data = simplified_geometry[key]
            pdb_to_move_CA_fingerprint = data[0]
            pdb_to_move_max_inter_atom_distance = data[1]
 
            # in the final version, combine them with and statement *******
            if math.fabs(pdb_to_move_max_inter_atom_distance - pdb_orig_max_distance) < vars['filter_steps_one_and_two_tolerance']: # again trying to avoid unnecessary RMSD alignments
                if pdb_orig_CA.fingerprint_same_as(pdb_to_move_CA_fingerprint, vars['filter_steps_one_and_two_tolerance']):
 
                # So do an RMSD aligment by the alpha carbons only.
 
                pdb_to_move_CA=PDB()
                f = open(os.path.dirname(filename) + os.sep + ".." + os.sep + "CA" + os.sep + os.path.basename(filename)[:-7] + ".CA.pickle", 'r')
                pdb_to_move_CA = cPickle.load(f)
                f.close()
 
                initial = numpy.ndarray(shape=(3), dtype=float) # first, just translation (to speed up)
                initial[0] = 0.0
                initial[1] = 0.0
                initial[2] = 0.0
                tomove_array = scipy.optimize.fmin_slsqp(calculate_rmsd,initial,args=(pdb_to_move_CA,pdb_orig_CA,SIMILAR), iprint=-1) # fmin_slsqp was faster than powell, fmin, fmin_cg, fmin_bfgs, and anneal in a test case
                #tomove_array = scipy.optimize.fmin(calculate_rmsd,initial,args=(pdb_to_move_CA,pdb_orig_CA,SIMILAR)) #, iprint=-1) # fmin_slsqp was faster than powell, fmin, fmin_cg, fmin_bfgs, and anneal in a test case
         
                initial = numpy.ndarray(shape=(6), dtype=float) # now translation and rotation
                initial[0] = tomove_array[0]
                initial[1] = tomove_array[1]
                initial[2] = tomove_array[2]
                initial[3] = 0.0
                initial[4] = 0.0
                initial[5] = 0.0
 
                tomove_array = scipy.optimize.fmin_slsqp(calculate_rmsd,initial,args=(pdb_to_move_CA,pdb_orig_CA,SIMILAR),iprint=-1) # fmin_slsqp was faster than powell, fmin, fmin_cg, fmin_bfgs, and anneal in a test case
                #tomove_array = scipy.optimize.fmin_slsqp(calculate_rmsd,initial,args=(pdb_to_move_CA,pdb_orig_CA,SIMILAR)) #,iprint=-1) # fmin_slsqp was faster than powell, fmin, fmin_cg, fmin_bfgs, and anneal in a test case
 
                rmsd = calculate_rmsd(tomove_array,pdb_to_move_CA,pdb_orig_CA,SIMILAR)
 
                if rmsd < vars['filter_step_three_CA_rmsd_cutoff']: # eventually this will be user specified # So the alpha carbons align
 
                    pdb_to_move=PDB() # so now load in all the atoms
                    #f = open(filename + ".pickle", 'r')
                    f = open(filename, 'r')
                    pdb_to_move = cPickle.load(f)
                    f.close()
 
                    rmsd = calculate_rmsd(tomove_array,pdb_to_move,pdb_orig,SIMILAR) # this line serves to align the all-atom PDB according to the previous CA alignment
 
                    key_atom_names = {"ALA":"CB", "ARG":"CZ", "ASN":"CG", "ASP":"CG", "CYS":"SG", "GLU":"CD", "GLN":"CD", "HIS":"CG", "ILE":"CB", "LEU":"CG", "LYS":"NZ", "MET":"CE", "PHE":"CG", "SER":"OG", "THR":"CB", "TRP":"CG", "TYR":"CG", "VAL":"CB"}
 
                    # Now check the angles between key amino-acid atoms and their CA atoms to see if residues are generally pointed in right direction
                    # The first step is identify key atoms
                    #### THIS WHOLE SECTION CAN BE STREAMLINES FURTHER####
                    pdb_to_move_CA_atoms = {}
                    pdb_to_move_key_atoms = {}
                    for index in pdb_to_move.AllAtoms:
                    atom = pdb_to_move.AllAtoms[index]
                    key = str(atom.resid) + "_" + atom.resname.strip() + "_" + atom.chain
                    if atom.atomname.strip() == "CA": pdb_to_move_CA_atoms[key] = index
                    if atom.resname.strip() in key_atom_names and atom.atomname.strip() == key_atom_names[atom.resname.strip()]: pdb_to_move_key_atoms[key] = index
                     
                    pdb_orig_CA_atoms = {} # this could be pickled
                    pdb_orig_key_atoms = {}
                    for index in pdb_orig.AllAtoms:
                    atom = pdb_orig.AllAtoms[index]
                    key = str(atom.resid) + "_" + atom.resname.strip() + "_" + atom.chain
                    if atom.atomname.strip() == "CA": pdb_orig_CA_atoms[key] = index
                    if atom.resname.strip() in key_atom_names and atom.atomname.strip() == key_atom_names[atom.resname.strip()]: pdb_orig_key_atoms[key] = index
                     
                    # now match up the alpha carbons
                    matched_CA = []
                    for key1 in pdb_to_move_CA_atoms:
                    CA_index_1 = pdb_to_move_CA_atoms[key1]
                    CA_1 = pdb_to_move.AllAtoms[CA_index_1]
                     
                    # look for the CA that's closest in the static PDB
                    best_dist = 1000000000.0
                    best_key = ""
                     
                    for key2 in pdb_orig_CA_atoms:
                        CA_index_2 = pdb_orig_CA_atoms[key2]
                        CA_2 = pdb_orig.AllAtoms[CA_index_2]
                        dist = CA_2.coordinates.dist_to(CA_1.coordinates)
                        if dist < best_dist:
                        best_dist = dist
                        best_key = key2
                     
                    matched_CA.append((key1, best_key))
                     
                    #pdb_lines = []
 
                    # Now get the atom indecies that will be used to calculate the vectors
                    atoms_to_calculate_vectors = []
                    for matches in matched_CA:
                    #print pdb_to_move_key_atoms[matches[0]],"***(())"
                    if matches[0] in pdb_to_move_key_atoms and matches[0] in pdb_to_move_CA_atoms and matches[1] in pdb_orig_CA_atoms and matches[1] in pdb_orig_key_atoms:
                        atoms_to_calculate_vectors.append((pdb_to_move_key_atoms[matches[0]], pdb_to_move_CA_atoms[matches[0]], pdb_orig_CA_atoms[matches[1]], pdb_orig_key_atoms[matches[1]]))
                     
                    # now calculate the angles
                    max_angle = 0.0
                    for atoms in atoms_to_calculate_vectors:
                    coor_one = pdb_to_move.AllAtoms[atoms[0]].coordinates
                    coor_two_1 = pdb_to_move.AllAtoms[atoms[1]].coordinates
                    coor_two_2 = pdb_orig.AllAtoms[atoms[2]].coordinates
                    coor_three = pdb_orig.AllAtoms[atoms[3]].coordinates
                    coor_two = coor_two_1.average_with(coor_two_2)
                     
                    vec1 = coor_one.minus(coor_two)
                    vec2 = coor_three.minus(coor_two)
                     
                    angle = math.acos(vec1.dot_product_with(vec2)/(vec1.length() * vec2.length())) * 180 / math.pi
                     
                    if angle > max_angle: max_angle = angle
                     
                    if max_angle < vars['filter_step_four_side_chain_angle_cutoff']:
 
                    # Now do an RMSD alignment by all atoms
                    tomove_array = scipy.optimize.fmin_slsqp(calculate_rmsd,tomove_array,args=(pdb_to_move,pdb_orig,SIMILAR),iprint=-1) # fmin_slsqp was faster than powell, fmin, fmin_cg, fmin_bfgs, and anneal in a test case
                    rmsd = calculate_rmsd(tomove_array,pdb_to_move,pdb_orig,SIMILAR)
     
                    if rmsd < vars['filter_step_five_rmsd_cutoff']:
     
                        # Now make sure the docked ligand does not clash with the protein atoms
                        # Let's first get a pdb of just the docked ligand
                        docked_ligand = PDB()
                        count = 1
                        for index in pdb_to_move.AllAtoms:
                            atom_to_move = pdb_to_move.AllAtoms[index]
                            if atom_to_move.belongs_to_protein() == False:
                                count = count + 1
                                docked_ligand.AllAtoms[count] = atom_to_move.CopyOf()
     
                        # now compare the atoms of the ligand with the atoms of the protein
                        steric_clash = False
                        for lig_index in docked_ligand.AllAtoms:
                            lig_atom = docked_ligand.AllAtoms[lig_index]
                            for prot_index in pdb.AllAtoms:
                                prot_atom = pdb.AllAtoms[prot_index]
                                dist = lig_atom.coordinates.dist_to(prot_atom.coordinates)
                                if dist < vars['filter_step_six_steric_clash_cutoff']:
                                    steric_clash = True
                                    break
                            if steric_clash == True: break
     
                        if steric_clash == False: 
             
                            # There needs to be a processing thing here. Dont save PDB's that clash with original pdb
                            thefilename = os.path.basename(filename) + ".RMSD." + str(round(rmsd,1)) + "." + micro_and_filename[0][-1]
                            pdb_to_move.SavePDB(vars['output_directory'] + 'temp.'+ thefilename +'.pdb')
                            pdb_orig.SavePDB(vars['output_directory'] + 'temp.' + thefilename + ".orig.pdb")
                            docked_ligand.SavePDB(vars['output_directory'] + 'temp.' + thefilename + ".lig.pdb")
                            #print atoms_to_calculate_vectors, angels, "*************"
                            #print angels
                            #for pdb_line in pdb_lines: print pdb_line
                            print "          A match was found from the database (" + os.path.basename(filename) + ")"
                            #os.system('~/stop_multi')
                            #sdf
                        #else: print "Match with database (" + os.path.basename(filename) + ")...rejected for steric clash"
                    #else: print "skip4", rmsd, micro_and_filename[0][-1]
                    #else: print "skip3", rmsd, micro_and_filename[0][-1]
                #else: print "skip1", pdb_to_move_CA_fingerprint, pdb_orig_CA_fingerprint, tol, micro_and_filename[0][-1]
                #else: print "skip2", math.fabs(pdb_to_move_max_inter_atom_distance - pdb_orig_max_distance), tol, micro_and_filename[0][-1]
 
        mutex.acquire()
        running.value -= 1
        mutex.release()
 
# Allows for the management of multiple docking threads.
# Requires: chunk is a list containing active-site microenvironments and associated files from 
#   the database. pdb is a pdb object of the original protein target. simplified_geometry is 
#   a large dictionary containing information about the microenvironments from the database to 
#   allow quick comparison without the need for an RMSD alignment. SIMILAR is a dictionary 
#   containing information about which amino acids are similar to one another. vars is a 
#   dictionary containing the command-line user-specified variables.
def manage_threads(chunks, pdb, simplified_geometry, SIMILAR, vars):
 
    print "Aligning the microenvironments from the database to the microenvironments of the active site to confirm match..."
 
    num_processors = len(chunks)
 
    global total
     
    running = multiprocessing.Value('i', num_processors)
    mutex = multiprocessing.Lock()
 
    arrays = []
    threads = []
    for i in range(num_processors):
        threads.append(docking_thread())
        arrays.append(multiprocessing.Array('i',[0]))
 
    processes = []
    for i in range(num_processors):
        p = multiprocessing.Process(target=threads[i].value_func, args=(running, mutex, chunks[i], pdb, simplified_geometry, SIMILAR, vars, arrays[i]))
 
        p.start()
        processes.append(p)
 
    last_percent = ""
    while running.value > 0:
        count_lines = 0
        for index in range(len(processes)):
            process = processes[index]
            count_lines = count_lines + arrays[index][0]
        if count_lines % 100 == 0:
            new_percent = str(round(100*float(count_lines)/float(total),1))
            if new_percent != last_percent: print "     Step " + str(count_lines) + " of " + str(total) + "... " + new_percent + "%"
            last_percent = str(round(100*float(count_lines)/float(total),1))
             
    for process in processes:
        process.terminate()
    mutex.acquire()
    sys.stdout.flush()
    mutex.release()
 
def calculate_rmsd_no_docking(pdb1, lig1_resname, pdb2, lig2_resname):
     
    total_dist_squared = 0.0
     
    count = 0
    #print "pdb1.allatoms", len(pdb1.AllAtoms)
    #print "pdb2.allatoms", len(pdb2.AllAtoms)
    for index1 in pdb1.AllAtoms:
        atom1 = pdb1.AllAtoms[index1]
        if atom1.element != "H": # so ignoring hydrogens
        best_dist = 999999999.9
        for index2 in pdb2.AllAtoms:
            atom2 = pdb2.AllAtoms[index2]
            if atom2.element != "H":
                #print atom1.element, atom2.element
                #print atom1.resname, lig1_resname
                #print atom2.resname, lig2_resname
                if atom1.element.strip() == atom2.element.strip() and atom1.resname.strip() == lig1_resname.strip() and atom2.resname.strip() == lig2_resname.strip():
                dist = atom1.coordinates.dist_to(atom2.coordinates)
                if best_dist > dist:
                    best_dist = dist
 
        if best_dist != 999999999.9:
        count = count + 1
        total_dist_squared = total_dist_squared + math.pow(best_dist,2)
     
    if count == 0:
    return 9999999999
    #global micro_and_filename, filename
    #print micro_and_filename[0], filename
     
    rmsd = math.pow(total_dist_squared / count,0.5)
 
    return rmsd
 
# now try to rank the file names
def cmp(filename1, filename2):
    filename1 = os.path.basename(filename1)
    filename2 = os.path.basename(filename2)
     
    # prefer exact matches to ones involving similar amino acids
    if ".SIMILAR." in filename1 and ".EXACT." in filename2: return 1
    if ".EXACT." in filename1 and ".SIMILAR." in filename2: return -1
     
    # prefer ones containing more residues to ones containing only a few
    if ".num_residues.3." in filename1 and ".num_residues.4." in filename2: return 1
    if ".num_residues.3." in filename1 and ".num_residues.5." in filename2: return 1
    if ".num_residues.4." in filename1 and ".num_residues.5." in filename2: return 1
     
    if ".num_residues.4." in filename1 and ".num_residues.3." in filename2: return -1
    if ".num_residues.5." in filename1 and ".num_residues.3." in filename2: return -1
    if ".num_residues.5." in filename1 and ".num_residues.4." in filename2: return -1
     
    # now sort based on rmsd
    filename1 = filename1.split(".")
    filename2 = filename2.split(".")
    #print filename1
    rmsd1 = float(filename1[15]+"."+filename1[16])
    rmsd2 = float(filename2[15]+"."+filename2[16])
    if rmsd1 < rmsd2:
    return -1
    elif rmsd1 > rmsd2:
    return 1
    else:
    return 0
 
def format_output():
    global vars
     
    print "Organizing output..."
     
    # Load in a list of all the pdbs
    filenames = glob.glob(vars['output_directory'] + "*.SIMILAR.pdb")
    filenames2 = glob.glob(vars['output_directory'] + "*.EXACT.pdb")
    filenames.extend(filenames2)
     
    # Load in information about pdbs
    # first load in all the files.
    pdb_objects = {} # this is not a very memory-friendly way of doing this. :(
    for filename in filenames:
    pdb_objects[filename] = PDB()
    pdb_objects[filename].LoadPDB(filename)
     
    # now identify the resnames of the ligands from the filename
    resnames = {}
    for filename in pdb_objects.keys():
    fl = filename.replace("."," ").split(" ")
    lig_resname = fl[6]
    resnames[filename] = lig_resname
     
    # now determine the number of atoms in the ligands of these files
    heavy_atoms_count = {}
    for filename in pdb_objects.keys():
     
    # now count the number of heavy atoms in the ligand
    pdb_tmp = pdb_objects[filename]
    count = 0
    for index in pdb_tmp.AllAtoms:
        atom = pdb_tmp.AllAtoms[index]
        if atom.element != "H" and atom.resname.strip() == resnames[filename]: count = count + 1
    heavy_atoms_count[filename] = count
 
    # now go through and find pdbs with RMSD that are very low, with the same number of ligand atoms, and mark some for deletion
    to_remove = []
    for index1 in range(len(filenames)-1):
    filename1 = filenames[index1]
    for index2 in range(index1 + 1, len(filenames)):
        filename2 = filenames[index2]
        if heavy_atoms_count[filename1] == heavy_atoms_count[filename2]:
        # now calculate the rmsd between the two
        rmsd = calculate_rmsd_no_docking(pdb_objects[filename1], resnames[filename1], pdb_objects[filename2], resnames[filename2])
        #print "====="
        #print rmsd
        if rmsd < 0.5:
            #print rmsd
            to_remove.append(os.path.basename(filename2)[5:])
     
    # now move the files around
    os.makedirs(vars['output_directory'] + "1.orig_files")
    os.makedirs(vars['output_directory'] + "2.non_redundant_files")
     
    # copy the non-redundant files to the appropriate directory
    for filename in filenames:
    if not filename in to_remove: shutil.copy2(filename[:-3] + "lig.pdb", vars['output_directory'] + "2.non_redundant_files" + os.sep + os.path.basename(filename)[5:])
     
    # move all files to the 1.orig_files directory
    for filename in glob.glob(vars['output_directory'] + "*.pdb"): shutil.move(filename, vars['output_directory'] + "1.orig_files" + os.sep + os.path.basename(filename)[5:])
 
    print "Ranking identified molecular fragments..."
 
    filenames = glob.glob(vars['output_directory'] + "2.non_redundant_files" + os.sep + "*.pdb")
    filenames.sort(cmp)
    f = open(vars['output_directory'] + "3.ranked_compounds.txt",'w')
    f.write("Rank\tFilename\n")
    f.write("====\t========\n\n")
    count = 1
    for filename in filenames:
    f.write(str(count) + "\t" + '.' + os.sep + '2.non_redundant_files' + os.sep + os.path.basename(filename) + "\n")
    count = count + 1
    f.close()
 
def show_flag(text, flag, prefix = "-"):
    flag = prefix + flag
    size = 45
    while len(flag) < size: flag = flag + " "
    indent2=""
    while len(indent2) < size + 1: indent2 = indent2 + " "
    wrapper = textwrap.TextWrapper(120,flag,indent2)
    print wrapper.fill(text)
 
def print_help_file():
    wrapper = textwrap.TextWrapper(120)
    for item in sys.argv:
        if item.upper() == "-HELP":     
            print ""
            print "INTRODUCTION"
            print "============"
            print ""
             
            print wrapper.fill("CrystalDock is a computer algorithm that aids the computational identification of molecular fragments predicted to bind a receptor pocket of interest. CrystalDock makes direct use of crystallographic and NMR structures from the Protein Data Bank (PDB). As of June 2011, the PDB contained 73,503 molecular models, 52,253 of which included ligands. While long-range electrostatic interactions certainly can influence ligand binding, for many ligands the predominant interactions required for molecular recognition are often with receptor atoms that immediately line the active site. When these key residues are grouped by proximity, they form \"microenvironments\" that are only compatible with the binding of certain molecular fragments. The PDB provides ample experimental data from which these microenvironments can be identified and characterized.")
            print ""
            print wrapper.fill("CrystalDock identifies the microenvironments of an active site of interest and then performs a geometric comparison to identify similar microenvironments present in ligand-bound PDB structures. Germane fragments from the crystallographic or NMR ligands are subsequently placed within the novel active site. These positioned fragments can then be linked together to produce ligands that are likely to bind the pocket of interest; alternatively, they can be joined to an inhibitor with a known or suspected binding pose to potentially improve binding affinity.")
            print ""
            print "PREREQUISITES"
            print "============="
            print ""
            print wrapper.fill("CrystalDock has been tested on Ubuntu Linux 10.04.1 LTS, Mac OS X 10.6.6, and Windows XP using Python versions 2.6.5, 2.6.1, and 2.7.1, respectively. The program also requires SciPy (http://www.scipy.org/) and NumPy (http://numpy.scipy.org/).")
            print ""
            print "COMMANDLINE PARAMETERS"
            print "======================"
            print ""
            print "The following commandline parameters are available:"
            print ""
             
             
            show_flag("A pdb file of the receptor into which fragments will be docked.", 'receptor_pdb_file')
            show_flag("By default, CrystalDock determines the number of active-site-lining residues automatically. However, the user can specify these residues explicitly if desired. A residue is specified by entering the residue index, name, and chain, separated by underscores (i.e., 371_ARG_A).", 'user_specified_residue')
            show_flag("The directory where the docking results will be written. This directory must not exist prior to running CrystalDock.", 'output_directory')
            show_flag("The directory containing the microenvironment database. The default is ./microenvironment_database/", 'microenvironment_database_directory')
             
            show_flag("The x-coordinate of a point specifying the location of the active site or active-site region of interest.", 'pocket_center_x')
            show_flag("The y-coordinate of a point specifying the location of the active site or active-site region of interest.", 'pocket_center_y')
            show_flag("The z-coordinate of a point specifying the location of the active site or active-site region of interest.", 'pocket_center_z')
            show_flag("The radius of a sphere, centered on the location coordinate above, that defines the region of the receptor surface that will be analyzed.", 'pocket_radius')
             
            show_flag("Performing full RMSD alignments of all active-site and database microenvironments is too computationally intensive. Consequently, microenvironments go through a number of \"filters\" to try to eliminate ones that are geometrically dissimilar without having to perform the full RMSD alignment. This commandline parameter can be used to control the first two steps of this filter. See the source code for more details. 2.0 angstroms by default.", 'filter_steps_one_and_two_tolerance')
            show_flag("A preliminary, fast RMSD alignment is performed using only the alpha carbons of the active-site and database microenvironments to ensure that they are generally geometrically similar. This commandline variable specifies the maximum allowable RMS distance following alignment. 2.5 angstroms by default.", 'filter_step_three_CA_rmsd_cutoff')
            show_flag("Following the preliminary RMSD alignment, the program analyzes the angle between the side chains of aligned residues. If any of these side chains are not generally pointing in the same direction, the microenvironments are judged to be dissimilar. This commandline variable specifies the maximum allowable angle between aligned side chains. 100.0 degrees by default.", 'filter_step_four_side_chain_angle_cutoff')
            show_flag("A final, more rigorous RMSD alignment is performed using all the common heavy atoms of the active-site and database microenvironments to ensure that they are geometrically similar. This commandline variable specifies the maximum allowable RMS distance following alignment. 1.5 angstroms by default.", 'filter_step_five_rmsd_cutoff')
            show_flag("A docked fragment is eliminated if it comes too close to a protein-receptor atom. This commandline variable specifies the minimum allowable distance. 2.0 angstroms by default.", 'filter_step_six_steric_clash_cutoff')
             
            show_flag("By default, CrystalDock identifies receptor microenvironments containing three, four, and five residues. If this flag is set to \"FALSE\", microenvironments of three residues will not be considered.", 'use_microenvironments_of_3_residues')
            show_flag("If this flag is set to \"FALSE\", microenvironments of four residues will not be considered.", 'use_microenvironments_of_4_residues')
            show_flag("If this flag is set to \"FALSE\", microenvironments of five residues will not be considered.", 'use_microenvironments_of_5_residues')
             
            show_flag("The number of processors to use. By default, all processors available on the system are employed.", 'num_processors')
             
            print ""
            print "EXAMPLES"
            print "========"
            print ""
            print wrapper.fill("Find fragments predicted to bind to a protein called 1XDN.pdb. The region of the active site to be analyzed is located at (37.6, 23.2, 13.4). Only the region within 6 angstroms of the specified coordinate should be considered. The output will be written to a directory called ./my_output/:")
            print ""
            print wrapper.fill("python crystal_dock.py -receptor_pdb_file 1XDN.pdb -pocket_center_x 37.6 -pocket_center_y 23.2 -pocket_center_z 13.4 -pocket_radius 6 -output_directory ./my_output/")
            print ""
            print wrapper.fill("Same as above, but only microenvironments containing three residues should be considered:")
            print ""
            print wrapper.fill("python crystal_dock.py -receptor_pdb_file 1XDN.pdb -pocket_center_x 37.6 -pocket_center_y 23.2 -pocket_center_z 13.4 -pocket_radius 6 -output_directory ./my_output/ -use_microenvironments_of_3_residues true -use_microenvironments_of_4_residues false -use_microenvironments_of_5_residues false")
            print ""
            print wrapper.fill("Same as above, but rather than allowing CrystalDock to auto-detect active-site-lining residues, the user specifies those residues explicitly:")
            print ""
            print wrapper.fill("python crystal_dock.py -receptor_pdb_file 1XDN.pdb -pocket_center_x 37.6 -pocket_center_y 23.2 -pocket_center_z 13.4 -pocket_radius 6 -output_directory ./my_output/ -use_microenvironments_of_3_residues true -use_microenvironments_of_4_residues false -use_microenvironments_of_5_residues false -user_specified_residue 371_ARG_A -user_specified_residue 118_ARG_A -user_specified_residue 292_ARG_A -user_specified_residue 406_TYR_A -user_specified_residue 347_TYR_A")
            print ""
            print wrapper.fill("Same as above, but now with altered filter parameters:")
            print ""
            print wrapper.fill("python crystal_dock.py -receptor_pdb_file 1XDN.pdb -pocket_center_x 37.6 -pocket_center_y 23.2 -pocket_center_z 13.4 -pocket_radius 6 -output_directory ./my_output/ -use_microenvironments_of_3_residues true -use_microenvironments_of_4_residues false -use_microenvironments_of_5_residues false -user_specified_residue 371_ARG_A -user_specified_residue 118_ARG_A -user_specified_residue 292_ARG_A -user_specified_residue 406_TYR_A -user_specified_residue 347_TYR_A -filter_steps_one_and_two_tolerance 4.0 -filter_step_three_CA_rmsd_cutoff 4.0 -filter_step_four_side_chain_angle_cutoff 180.0 -filter_step_five_rmsd_cutoff 4.0 -filter_step_six_steric_clash_cutoff 4.0")
            print ""
            print wrapper.fill("Same as above, but explicitly instruct the program to run on 2 processors:")
            print ""
            print wrapper.fill("python crystal_dock.py -receptor_pdb_file 1XDN.pdb -pocket_center_x 37.6 -pocket_center_y 23.2 -pocket_center_z 13.4 -pocket_radius 6 -output_directory ./my_output/ -use_microenvironments_of_3_residues true -use_microenvironments_of_4_residues false -use_microenvironments_of_5_residues false -user_specified_residue 371_ARG_A -user_specified_residue 118_ARG_A -user_specified_residue 292_ARG_A -user_specified_residue 406_TYR_A -user_specified_residue 347_TYR_A -filter_steps_one_and_two_tolerance 4.0 -filter_step_three_CA_rmsd_cutoff 4.0 -filter_step_four_side_chain_angle_cutoff 180.0 -filter_step_five_rmsd_cutoff 4.0 -filter_step_six_steric_clash_cutoff 4.0 -num_processors 2")
            print ""
            print "OUTPUT"
            print "======"
            print ""
            print "Three items are placed in the output directory:"
            print ""
             
             
            show_flag("A directory containing all the identified fragments, in PDB format.", '1.orig_files (subdirectory)', '')
            show_flag("A directory containing all the identified fragments with redundant fragments (RMSD < 0.5) removed.", '2.non_redundant_files (subdirectory)', '')
            show_flag("A text file listing all the non-redundant fragments. Fragments with microenvironments whose amino-acid matches are exact always rank better than those whose matches are merely similar. If fragments cannot be distinguished based on this criteria, fragments with microenvironments containing greater numbers of amino acids are given precedence over those with fewer amino acids. Finally, all other things being equal, the fragments are ranked by the RMSD between their associated microenvironments and the identified microenvironments of the novel binding pocket.", '3.ranked_compounds.txt (file)', '')
            print ""
            sys.exit(0)
 
# Print out header information
print ""
reference("")
print ""
 
# check to see if "-help" is in the command line
print_help_file()
 
print "For a comprehensive help file, use the \"-help\" commandline parameter."
print ""
 
# Get the command-line parameters
vars = get_commandline_parameters()
 
# Loading in PDB file
print "Loading the PDB file " + vars['receptor_pdb_file'] + "..."
pdb = PDB()
pdb.LoadPDB(vars['receptor_pdb_file'])
 
# Identify active-site residues
active_site_residues = id_active_site_residues(vars)
 
# Identify all possible combinations of microenvironments
# database of similar amino acids. Aaron did this.
SIMILAR = {' CYS':[' CYS',' SER',' THR'], ' SER':[' CYS',' SER',' THR'], ' THR':[' CYS',' SER',' THR'],' PRO':[' PRO'], ' ALA':[' ALA',' VAL'], ' GLY':[' GLY'], ' ASN':[' ASN',' GLN'], ' ASP':[' ASP',' GLU'], ' GLU':[' ASP',' GLU'], ' GLN':[' ASN',' GLN'], ' HIS':[' HIS', ' LYS'], ' ARG':[' ARG', ' LYS'], ' LYS':[' ARG', ' LYS', ' HIS'], ' MET':[' MET', ' ILE', ' LEU', ' VAL'], ' ILE':[' MET', ' ILE', ' LEU', ' VAL'], ' LEU':[' MET', ' ILE', ' LEU', ' VAL'], ' VAL':[' ALA', ' MET', ' ILE', ' LEU', ' VAL'], ' PHE':[' PHE', ' TYR', ' TRP'], ' TYR':[' PHE', ' TYR', ' TRP'], ' TRP':[' PHE', ' TYR', ' TRP']}
microenvironments = combinations_of_micro_environments(active_site_residues)
 
# Identify potential matching microenvironments from the database
micros_and_filenames = id_matching_microenvironments_from_database(microenvironments)
 
# Get the total number of "dockings." Needed so we can tell user about progress.
total = 0
for micro_and_filename in micros_and_filenames: total = total + len(micro_and_filename[1])
 
# Load pickle file with all simplified geometric information for the microfragments
print "Loading simplified geometric information about the microenvironments..."
f = open(vars['microenvironment_database_directory'] + os.sep + 'distances.pickle','r')
simplified_geometry = cPickle.load(f)
f.close()
 
if "WINDOWS" in platform.system().upper(): # so you're running on windows
    print "WARNING: Multithreading is not supported in Microsoft Windows. Using only one processor."
 
    chunks = divide_micros_and_filenames_into_separate_lists(1)
    a = multiprocessing.Array('i',[0])
    running = multiprocessing.Value('i', 1)
    mutex = multiprocessing.Lock()
     
    dock = docking_thread()
    dock.value_func(running, mutex, chunks[0], pdb, simplified_geometry, SIMILAR, vars, a, True)
 
else:
 
    # divide micros_and_filenames into separate lists for running on separate threads
    chunks = divide_micros_and_filenames_into_separate_lists(vars['num_processors'])
 
    # align the microenvironments from the database using multithreading
    # With RMSD, consider incorporating CA-CB vector into RMSD instead of all atoms 
    manage_threads(chunks, pdb, simplified_geometry, SIMILAR, vars)
 
# move files around in the output directory to make it more readable, rank compounds as well
format_output()
 
# Tell the user how long it took to execute the script
print "Execution time:", time.time() - starttime, "Seconds"
