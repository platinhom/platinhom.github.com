---
layout: post_mathjax
title: Usage of Delphi-APBS-AmberPB
date: 2015-06-18 17:38:54
categories: CompCB
tags: CompBiol Python Bash Software
---

### [APBS](http://www.poissonboltzmann.org/)
[APBS-PDB2PQR](http://www.poissonboltzmann.org/docs/downloads/); [APBS-download](http://sourceforge.net/projects/apbs/); [PDB2PQR-download](http://sourceforge.net/projects/pdb2pqr/); [APBS-PDB2PQR github](https://github.com/Electrostatics/apbs-pdb2pqr);  
[egg Lysozyme pKa example](http://www.poissonboltzmann.org/examples/Lysozyme_pKa_example/)

- Run APBS as: `apbs file.in 2>&1 | tee file.out`
- APBS parameters input example:

~~~ python
read
    mol pqr 2LZT-noASH66.pqr # This is the compound for which we will calculate
                         # solvation energies
    mol pqr 2LZT-ASP66.pqr      # This is a compound used as a reference for grid
                         # centering
end

elec name inhom          
    mg-auto              # Focusing calculations
    dime 258 258 258     # This is a good grid spacing for this system
    cglen 52.0 66.0 79.0 # These are reasonable coarse grid settings for
                         # this system (PDB2PQR-recommended)
    fglen 51.0 59.0 67.0 # These are reasonable fine grid settings for this
                         # system (PDB2PQR-recommended)
    cgcent mol 2         # Center the grid on the reference molecule
    fgcent mol 2         # Center the grid on the reference molecule
    mol 1
    lpbe
    bcfl sdh
    pdie 20.00
    sdie 78.54
    srfm smol
    sdens 40.0
    chgm spl2
    srad 1.40
    swin 0.30
    temp 298.15
    calcenergy total
    calcforce no
end

# Print the final energy 
print energy inhom end

quit
~~~

- A bash script to run for all pqr files. You can modify to add your parameters in apbs input file.

~~~ bash
#!/bin/bash
# Author: Hom, 2015.6.18
# Run all the pqr files by apbs. 
# Run as : ./Run-apbs.sh

for i in *.pqr; do
	echo "Running ${i}..."
	prefix=${i%.pqr}
	
	# Generate the input parameters file. You can modify parameters here.
	echo "read                                                                         " > ${prefix}.in
	echo "    mol pqr ${prefix}.pqr # This is the compound for which we will calculate " >> ${prefix}.in
	echo "                         # solvation energies                                " >> ${prefix}.in
	echo "    mol pqr ref.pqr      # This is a compound used as a reference for grid   " >> ${prefix}.in
	echo "                         # centering                                         " >> ${prefix}.in
	echo "end                                                                          " >> ${prefix}.in
	echo "                                                                             " >> ${prefix}.in
	echo "elec name inhom                                                              " >> ${prefix}.in
	echo "    mg-auto              # Focusing calculations                             " >> ${prefix}.in
	echo "    dime 129 129 129     # This is a good grid spacing for this system       " >> ${prefix}.in
	echo "    cglen 52.0 66.0 79.0 # These are reasonable coarse grid settings for     " >> ${prefix}.in
	echo "                         # this system (PDB2PQR-recommended)                 " >> ${prefix}.in
	echo "    fglen 51.0 59.0 67.0 # These are reasonable fine grid settings for this  " >> ${prefix}.in
	echo "                         # system (PDB2PQR-recommended)                      " >> ${prefix}.in
	echo "    cgcent mol 2         # Center the grid on the reference molecule         " >> ${prefix}.in
	echo "    fgcent mol 2         # Center the grid on the reference molecule         " >> ${prefix}.in
	echo "    mol 1                                                                    " >> ${prefix}.in
	echo "    lpbe                                                                     " >> ${prefix}.in
	echo "    bcfl sdh                                                                 " >> ${prefix}.in
	echo "    pdie 20.00                                                               " >> ${prefix}.in
	echo "    sdie 80.00                                                               " >> ${prefix}.in
	echo "    sdens 40.0                                                               " >> ${prefix}.in
	echo "    srfm smol                                                                " >> ${prefix}.in
	echo "    chgm spl2                                                                " >> ${prefix}.in
	echo "    srad 1.40                                                                " >> ${prefix}.in
	echo "    swin 0.30                                                                " >> ${prefix}.in
	echo "    temp 298.15                                                              " >> ${prefix}.in
	echo "    calcenergy total                                                         " >> ${prefix}.in
	echo "    calcforce no                                                             " >> ${prefix}.in
	echo "end                                                                          " >> ${prefix}.in
	echo "                                                                             " >> ${prefix}.in
	echo "# Print the final energy                                                     " >> ${prefix}.in
	echo "print energy inhom end                                                       " >> ${prefix}.in
	echo "                                                                             " >> ${prefix}.in
	echo "quit                                                                         " >> ${prefix}.in
	
# Print the final energy 
print energy inhom end

quit
	
	(apbs.exe ${prefix}.in 2>&1) | tee ${prefix}.apbs
done
~~~ 

### [DelPhi](http://wiki.c2b2.columbia.edu/honiglab_public/index.php/Software:DelPhi)     
How to use: [Delphi workshop](http://cinjweb.umdnj.edu/~kerrigje/pdf_files/Delphi_Workshop.pdf),[Manual](https://honiglab.c2b2.columbia.edu/software/DelPhi/doc/delphi_manual.pdf), [ref](/pdf/reference/pKa-pI/delphi-2012.pdf).  

- Run delphi as `./delphicpp input.prm 2>&1 | tee output.out`  
NOTE: Delphi reports energy in units of kT. (1 kT = 0.592 kcal/mol for T = 298 K and k= 0.001986577 kcal/mol•K)  

- input parameters file example(`input.prm`) for delphi.  
NOTE: You can also use `Run-delphi.sh` below to run multi-jobs via automatic generating input parameter file.

~~~ fortran
!gsize=165					   ! GRID SIZE: must be an odd number. A larger grid size will give more accurate potentials;
                               ! however, will require more cpu time. (NOTE: min = 5; max = 571) 
scale=2.0                      ! Reciprocal of one grid spacing (grids/angstrom). 
in(pdb,file="test.pqr")        ! reads in ala.pdb
in(crg,file="test.crg")        ! reads in charge file ala.crg
in(siz,file="test.siz")        ! reads in size file ala.siz
indi=2                         ! interior dielectric default= 2
exdi=80                        ! exterior dielectric constant, default 80 for water
prbrad=1.40                    ! Probe radius. Used for the solvent accessible surface calculation. (prbrad = 1.4 for water.)
salt=0                         ! The concentration of the first kind of salt (in mol/L). 
energy(s,c,g)                  ! outputs reaction field (solvation), coulombic and grid energies. 
                               ! ION:Use for the direct ionic contribution
perfil=80                      ! sets percent box fill to 80%,default=80.
bndcon=2                       ! An integer flag used to specify the type of boundary condition. 
                               ! 1 – potential is zero 
                               ! 2 – dipolar, boundary potentials are approximated by the Debye-Hückel potential. 
                               ! 3 – focusing, (requires a potential map from a prior calculation)
                               ! 4 – Coulombic, Approximate from the sum of the Debye-Hückel potentials of all charges qi
maxc=0.0001                    ! The convergence threshold value based on maximum change of potentia
linit= 800                     ! An integer number (> 3) of iterations with linear equation,default automatic.
conint=100                     ! A flag that determines at what iteration interval convergence is checked, by default itequals 10.
!nonit=0                       ! An integer number(>0) used to designate the number of iterations with the nonlinear PB equation.
!in(phi,unit=18)               ! reads in a previously created potential map for focussing calcs - not enabled
!in(frc,file="self")           ! uses pdb file entries to output potential
!out(modpdb)                   ! outputs pdb file with radii and charges
!out(frc,file="ala.frc")       ! and field values in ala.frc
!out(phi,unit=14)              ! outputs a potential map in default file
!out(phi,file="ala.phi")       ! outputs potential map in ala.phi
!acenter(28.114,40.477,9.909)  ! Takes 3 coordinates (in ?) and uses those coordinates for positioning of the molecule center. 
!salt2 					       ! Used to handle multiple valence salts 
!ionrad = The ion exclusion layer around the molecule (in A). Default ionrad = 2.0 for sodium chloride.
 
~~~

- A python script to extract the information from a pqr file to siz/crg file for delphi.

###### FILE: pqr2sizcrg.py

~~~ python
#! /usr/bin/env python
# -*- coding: utf8 -*-

# Author: Hom, Date: 2015.6.17
# To extract the information from pqr file to siz and crg files for delphi.
# Usage: python pqr2sizcrg.py input.pqr

import os,sys

if (__name__ == '__main__'):
	if (len(sys.argv)!=2):
		print "Please assign the pqr file."
		input()
		exit()
	fname=sys.argv[1]
	fnamelist=os.path.splitext(fname)
	fcrg=fnamelist[0]+".crg"
	fsiz=fnamelist[0]+".siz"
	fr=open(fname)
	fs=open(fsiz,'w')
	fc=open(fcrg,'w')
	fs.write("!Extract info. from pqr to siz file. By Hom.\n")
	fc.write("!Extract info. from pqr to crg file. By Hom.\n")
	fs.write("atom__resnumbc_radius_\n")
	fc.write("atom__resnumbc_charge_\n")
	for line in fr:
		items=line.split()
		if (items[0]=="ATOM" or items[0]=="HETATM"):
			outline="%-5.5s %-3.3s %-4.4s "%(items[2],items[3],items[4])
			outs=outline+"%-6.6s \n"%items[9]
			outc=outline+"%-6.6s \n"%items[8]
			fs.write(outs)
			fc.write(outc)

#end main
~~~

- A bash script to run for all the pqr files. You can modify to add your parameters in delphi input file. 
- You will need the `pqr2sizcrg.py` script above. 

~~~ bash
#!/bin/bash
# Author: Hom, 2015.6.18
# Run all the pqr files by delphi. 
# Run as : ./Run-delphi.sh

if [ ! -f ./pqr2sizcrg.py ];then
	echo "Please make sure you have pqr2sizcrg.py script "
	echo "to extract the charges and radius from pqr file!"
	exit
fi

for i in *.pqr; do
	echo "Running ${i}..."
	prefix=${i%.pqr}
	
	# Generate parameter file. You can revise the parameters you need.
	echo "! Delphi parameter file, created by pbrun.pl.               " > ${prefix}.prm
	echo "in(pdb,file=\"${prefix}.pqr\")    ! reads in PQR file       " >> ${prefix}.prm
	echo "in(crg,file=\"${prefix}.crg\")    ! reads in charge file    " >> ${prefix}.prm
	echo "in(siz,file=\"${prefix}.siz\")    ! reads in size file      " >> ${prefix}.prm
	echo "scale=2.0    ! grid size (resolution, in grid/Angstrom)     " >> ${prefix}.prm
	echo "indi=1.0      ! interior dielectric                         " >> ${prefix}.prm
	echo "exdi=80.0     ! external dielectric	                      " >> ${prefix}.prm
	echo "perfil=80                                                   " >> ${prefix}.prm
	echo "prbrad=1.4                                                  " >> ${prefix}.prm
	echo "bndcon=2                                                    " >> ${prefix}.prm
	echo "rionst=0.1                                                  " >> ${prefix}.prm
	echo "maxc=0.0001                                                 " >> ${prefix}.prm
	echo "linit=800                                                   " >> ${prefix}.prm
	echo "conint=100                                                  " >> ${prefix}.prm
	echo "energy(s,c,g)                                               " >> ${prefix}.prm
	
	# Need pqr2sizcrg.py files.
	./pqr2sizcrg.py ${prefix}.pqr
	(delphicpp.exe ${prefix}.prm 2>&1) | tee ${prefix}.delphi
done
~~~

### AmberPB

---
