---
layout: post_toc
title: Amber力场相关参数文件
date: 2015-11-13 22:22:55
categories: CompCB
tags: CompBiol MD
---

基于Amber14

# 文件列表

## 参数文件位置

- Amber/dat/leap/cmd/ : source加载的一系列力场等文件所在
- Amber/dat/leap/cmd/oldff : source加载的一系列力场等**旧版**文件所在, 如source oldff/leaprc.ff99SB
- Amber/dat/antechamber/ : antechamber处理小分子时的参数, 包括原子类型, parmchk等.

## dat/leap/cmd:

- leaprc.constph
- leaprc.ff03.r1
- leaprc.ff03ua
- leaprc.ff12SB
- leaprc.ff14ipq
- leaprc.ff14SB
- leaprc.ff14SBonlysc
- leaprc.ff14SB.redq
- leaprc.ffAM1 
- leaprc.ffPM3
- leaprc.gaff
- leaprc.GLYCAM_06EPb
- leaprc.GLYCAM_06j-1
- leaprc.lipid11
- leaprc.lipid14
- leaprc.modrna08
- leaprc.parmbsc0\_chiOL4_ezOL1
- leaprc.phosaa10
- leaprc.spce
- leaprc.tip3p
- leaprc.tip4pew
- oldff: 
	- leaprc.ff02
	- leaprc.ff02polEP.r0
	- leaprc.ff02polEP.r1
	- leaprc.ff02pol.r0
	- leaprc.ff02pol.r1
	- leaprc.ff03
	- leaprc.ff10
	- leaprc.ff84  
	- leaprc.ff86   
	- leaprc.ff94
	- leaprc.ff94.nmr
	- leaprc.ff96
	- leaprc.ff98
	- leaprc.ff99
	- leaprc.ff99bsc0
	- leaprc.ff99SB
	- leaprc.ff99SBildn
	- leaprc.ff99SBnmr
	- leaprc.GLYCAM_04  
	- leaprc.GLYCAM_06  
	- leaprc.GLYCAM_06EP
	- leaprc.GLYCAM_06h
	- leaprc.GLYCAM_06h-1
	- leaprc.GLYCAM_06h-12SB
	- leaprc.GLYCAM\_06j_10
	- leaprc.parmCHI_YIL.bsc
	- leaprc.rna.ff02
	- leaprc.rna.ff02EP
	- leaprc.rna.ff84
	- leaprc.rna.ff94  
	- leaprc.rna.ff98  
	- leaprc.rna.ff99
	- leaprc.toyrna

## dat/leap/parm

- all_modrna08.frcmod
- frcmod.chcl3
- frcmod.chiOL4
- frcmod.constph
- frcmod.dc4
- frcmod.ff02pol.r1
- frcmod.ff03
- frcmod.ff03ua
- frcmod.ff12SB
- frcmod.ff14SB
- frcmod.ff99SB
- frcmod.ff99SB14
- frcmod.ff99SBildn
- frcmod.ff99SBnmr
- frcmod.ff99SP
- frcmod.ions1lsm\_1264_spce
- frcmod.ions1lsm\_1264_tip3p
- frcmod.ions1lsm\_1264_tip4pew
- frcmod.ions1lsm\_hfe_spce
- frcmod.ions1lsm\_hfe_tip3p
- frcmod.ions1lsm\_hfe_tip4pew
- frcmod.ions1lsm_iod
- frcmod.ions34lsm\_1264_spce
- frcmod.ions34lsm\_1264_tip3p
- frcmod.ions34lsm\_1264_tip4pew
- frcmod.ions34lsm\_hfe_spce
- frcmod.ions34lsm\_hfe_tip3p
- frcmod.ions34lsm\_hfe_tip4pew
- frcmod.ions34lsm\_iod_spce
- frcmod.ions34lsm\_iod_tip3p
- frcmod.ions34lsm\_iod_tip4pew
- frcmod.ionsff99_tip3p
- frcmod.ionsjc_spce
- frcmod.ionsjc_tip3p
- frcmod.ionsjc_tip4pew
- frcmod.ionslm\_1264_spce
- frcmod.ionslm\_1264_tip3p
- frcmod.ionslm\_1264_tip4pew
- frcmod.ionslrcm\_cm_spce
- frcmod.ionslrcm\_cm_tip3p
- frcmod.ionslrcm\_cm_tip4pew
- frcmod.ionslrcm\_hfe_spce
- frcmod.ionslrcm\_hfe_tip3p
- frcmod.ionslrcm\_hfe_tip4pew
- frcmod.ionslrcm_iod
- frcmod.meoh
- frcmod.nma
- frcmod.opc
- frcmod.parmbsc0
- frcmod.parmbsc0_ezOL1
- frcmod.parmCHI_YIL
- frcmod.phosaa10
- frcmod.pol3
- frcmod.protonated_nucleic
- frcmod.qspcfw
- frcmod.spce
- frcmod.spcfw
- frcmod.tip3pf
- frcmod.tip4p
- frcmod.tip4pew
- frcmod.tip5p
- frcmod.urea
- gaff.dat
- GLYCAM_06EPb.dat
- GLYCAM_06h.dat
- GLYCAM_06j.dat
- lipid11.dat
- lipid14.dat
- lj\_1264_pol.dat
- nucgen.dat
- opls.info
- opls_parm.dat
- parm10.dat
- parm14ipq.dat
- parm91.dat
- parm91X.dat
- parm91X.ua.dat
- parm94.dat
- parm96.dat
- parm98.dat
- parm99.dat
- parm99EP.dat
- parmAM1.dat
- parmPM3.dat
- toyrna.dat

## dat/leap/prep

- all_amino03.in
- all_aminoct03.in
- all_aminont03.in
- amino10.in
- amino12.in
- aminoct10.in
- aminoct12.in
- aminont10.in
- aminont12.in
- chcl3.in
- dna\_nuc94-bsc0_chiOl4-ezOL1.in
- GLYCAM_06EPb.prep
- GLYCAM_06j-1.prep
- GLYCAM\_lipids_06h.prep
- meoh.in
- nma.in
- nucleic10.in
- protonated_nucleic
- toyrna.in
- uni_amino03.in
- uni_aminoct03.in
- uni_aminont03.in
- oldff
	- all_amino02EP.in
	- all_amino02.in
	- all_amino02.r1.in
	- all_amino94.in
	- all_aminoct02EP.in
	- all_aminoct02.in
	- all_aminoct94.in
	- all_aminont02EP.in
	- all_aminont02.in
	- all_aminont94.in
	- allct.in
	- all.in
	- allnt.in
	- all_nuc02EP.in
	- all_nuc02.in
	- all_nuc94.in
	- GLYCAM_06h.prep
	- GLYCAM_06j.prep
	- na.amberua.in
	- opls_nacl.in
	- opls_unict.in
	- opls_uni.in
	- opls_unint.in
	- protein.amberua.C.in
	- protein.amberua.in
	- protein.amberua.N.in
	- unict.in
	- uni.in
	- unint.in

## dat/leap/lib

- 8Mureabox.off
- 8Murea.readme
- all_amino03.lib
- all_amino94ildn.lib
- all_amino94.lib
- all_amino94.nmr.lib
- all_aminoAM1.lib
- all_aminoct03.lib
- all_aminoct94ildn.lib
- all_aminoct94.lib
- all_aminont03.lib
- all_aminont94ildn.lib
- all_aminont94.lib
- all_aminoPM3.lib
- all_modrna08.lib
- all_nucleic94.lib
- all_nucleic94.nmr.lib
- all\_prot_nucleic10.cmd
- all\_prot_nucleic10.lib
- all\_prot_nucleic10.log
- amino10.lib
- amino12.lib
- amino12.redq.lib
- amino14ipq.lib
- aminoct10.lib
- aminoct12.lib
- aminoct12.redq.lib
- aminoct14ip1_vac.lib
- aminoct14ipq.lib
- aminont10.lib
- aminont12.lib
- aminont12.redq.lib
- aminont14ipq.lib
- atomic_ions.cmd
- atomic_ions.lib
- atomic_ions.log
- chcl3box.off
- constph.lib
- cph\_nucleic_caps.lib
- DNA_CI.lib
- ff03.cmd
- ff03.log
- ff03ua.cmd
- ff03ua.log
- ff10.cmd
- ff10.log
- ff12SB.cmd
- ff12SB.log
- ff94.cmd
- ff94.log
- GLYCAM\_amino\_06j_12SB.lib
- GLYCAM\_aminoct\_06j_12SB.lib
- GLYCAM\_aminont\_06j_12SB.lib
- ions94.cmd
- ions94.lib
- ions94.log
- lipid11.lib
- lipid14.lib
- lipid14_supp.lib
- Makefile
- meohbox.off
- nab10.cmd
- nab10.lib
- nab10.log
- nmabox.off
- nucleic10.lib
- nucleic12.lib
- nucleic12.redq.lib
- opcbox.off
- pol3box.off
- PTR.lib
- qspcfwbox.off
- residues.RNA.parmCHI_YIL.bsc.lib
- RNA_CI.lib
- S1P.lib
- SEP.lib
- solvents.cmd
- solvents.lib
- solvents.log
- spcebox.off
- spcfwbox.off
- T1P.lib
- tip3pbox.off
- tip3pfbox.off
- tip4pbox.off
- tip4pewbox.off
- tip5pbox.off
- TPO.lib
- uni_amino03.lib
- uni_aminoct03.lib
- uni_aminont03.lib
- Y1P.lib
- oldff
	- all_amino02EP.lib
	- all_amino02.lib
	- all_amino02.r1.lib
	- all_amino2011pol.lib
	- all_amino91.lib
	- all_aminoct02EP.lib
	- all_aminoct02.lib
	- all_aminoct2011pol.lib
	- all_aminoct91.lib
	- all_aminont02EP.lib
	- all_aminont02.lib
	- all_aminont2011pol.lib
	- all_aminont91.lib
	- all_nucleic02EP.lib
	- all_nucleic02.lib
	- all_nucleic91.lib
	- dna.amberua.lib
	- ff02.cmd
	- ff02EP.cmd
	- ff02EP.log
	- ff02.log
	- ff91.cmd
	- ff91.log
	- GLYCAM\_amino\_06j_10.lib
	- GLYCAM\_aminoct\_06j_10.lib
	- GLYCAM\_aminont\_06j_10.lib
	- ions91.cmd
	- ions91.lib
	- pro-dna91.nmr.off
	- protein.amberua.lib
	- rna.amberua.lib

## dat/antechamber

- APS.DAT
- ATCOR.DAT
- ATOM_EQU.TYPE
- ATOMTYPE_AMBER.DEF
- ATOMTYPE_BCC.DEF
- ATOMTYPE_CHECK.TAB
- ATOMTYPE_GAS.DEF
- ATOMTYPE_GFF.DEF
- ATOMTYPE_SYBYL.DEF
- BCCPARM.DAT
- BONDTYPE_CHECK.TAB
- CONNECT.TPL
- CORR\_NAME_TYPE.DAT
- database_sample.def
- ESPPARM.DAT
- GASPARM.DAT
- mainchain_sample.dat
- PARMCHK.DAT
- RADIUS.DAT
- residuegen_sample.dat
- respgen\_addfile_sample.dat

# 文件内容

## leaprc.ff14SB

一般新版本都加载这个ff14SB力场.  

> leaprc.ff14SB概要

~~~bash
#   load atom type hybridizations
addAtomTypes {...}
#   Load the main parameter set.
parm10 = loadamberparams parm10.dat
frcmod14SB = loadamberparams frcmod.ff14SB
#   Load main chain and terminating amino acid libraries, nucleic acids
loadOff amino12.lib
loadOff aminoct12.lib
loadOff aminont12.lib
loadOff nucleic12.lib
#   Load water and ions
loadOff atomic_ions.lib
loadOff solvents.lib
HOH = TP3
WAT = TP3
#   Define the PDB name map for the amino acids and nucleic acids
addPdbResMap {...}
#  try to be good about reading in really old atom names as well:
addPdbAtomMap {...}
# assume that most often proteins use HIE
NHIS = NHIE
HIS = HIE
CHIS = CHIE
~~~

> leaprc.ff14SB详细内容: 

~~~bash
logFile leap.log
#
# ----- leaprc for loading the ff14SB force field
# ----- NOTE: this is designed for PDB format 3!
#    Uses frcmod.ff14SB for proteins; ff99bsc0 for DNA; ff99bsc0_chiOL3 for RNA
#
#   load atom type hybridizations
#
addAtomTypes {
    { "H"   "H" "sp3" }
    { "HO"  "H" "sp3" }
    { "HS"  "H" "sp3" }
    { "H1"  "H" "sp3" }
    { "H2"  "H" "sp3" }
    { "H3"  "H" "sp3" }
    { "H4"  "H" "sp3" }
    { "H5"  "H" "sp3" }
    { "HW"  "H" "sp3" }
    { "HC"  "H" "sp3" }
    { "HA"  "H" "sp3" }
    { "HP"  "H" "sp3" }
    { "HZ"  "H" "sp3" }
    { "OH"  "O" "sp3" }
    { "OS"  "O" "sp3" }
    { "O"   "O" "sp2" }
    { "O2"  "O" "sp2" }
    { "OP"  "O" "sp2" }
    { "OW"  "O" "sp3" }
    { "CT"  "C" "sp3" }
    { "CX"  "C" "sp3" }
    { "C8"  "C" "sp3" }
    { "2C"  "C" "sp3" }
    { "3C"  "C" "sp3" }
    { "CH"  "C" "sp3" }
    { "CS"  "C" "sp2" }
    { "C"   "C" "sp2" }
    { "CO"   "C" "sp2" }
    { "C*"  "C" "sp2" }
    { "CA"  "C" "sp2" }
    { "CB"  "C" "sp2" }
    { "CC"  "C" "sp2" }
    { "CN"  "C" "sp2" }
    { "CM"  "C" "sp2" }
    { "CK"  "C" "sp2" }
    { "CQ"  "C" "sp2" }
    { "CD"  "C" "sp2" }
    { "C5"  "C" "sp2" }
    { "C4"  "C" "sp2" }
    { "CP"  "C" "sp2" }
    { "CI"  "C" "sp3" }
    { "CJ"  "C" "sp2" }
    { "CW"  "C" "sp2" }
    { "CV"  "C" "sp2" }
    { "CR"  "C" "sp2" }
    { "CA"  "C" "sp2" }
    { "CY"  "C" "sp2" }
    { "C0"  "Ca" "sp3" }
    { "MG"  "Mg" "sp3" }
    { "N"   "N" "sp2" }
    { "NA"  "N" "sp2" }
    { "N2"  "N" "sp2" }
    { "N*"  "N" "sp2" }
    { "NP"  "N" "sp2" }
    { "NQ"  "N" "sp2" }
    { "NB"  "N" "sp2" }
    { "NC"  "N" "sp2" }
    { "NT"  "N" "sp3" }
    { "NY"  "N" "sp2" }
    { "N3"  "N" "sp3" }
    { "S"   "S" "sp3" }
    { "SH"  "S" "sp3" }
    { "P"   "P" "sp3" }
    { "LP"  ""  "sp3" }
    { "EP"  ""  "sp3" }
    { "F"   "F" "sp3" }
    { "Cl"  "Cl" "sp3" }
    { "Br"  "Br" "sp3" }
    { "I"   "I"  "sp3" }
    { "F-"   "F" "sp3" }
    { "Cl-"  "Cl" "sp3" }
    { "Br-"  "Br" "sp3" }
    { "I-"   "I"  "sp3" }
    { "Li+"  "Li"  "sp3" }
    { "Na+"  "Na"  "sp3" }
    { "K+"  "K"  "sp3" }
    { "Rb+"  "Rb"  "sp3" }
    { "Cs+"  "Cs"  "sp3" }
    { "Mg+"  "Mg"  "sp3" }
# glycam
    { "OG"  "O" "sp3" }
    { "OL"  "O" "sp3" }
    { "AC"  "C" "sp3" }
    { "EC"  "C" "sp3" }
}
#
#   Load the main parameter set.
#
parm10 = loadamberparams parm10.dat
frcmod14SB = loadamberparams frcmod.ff14SB
#
#   Load main chain and terminating amino acid libraries, nucleic acids
#
loadOff amino12.lib
loadOff aminoct12.lib
loadOff aminont12.lib
loadOff nucleic12.lib
#
#       Load water and ions
# 
loadOff atomic_ions.lib
loadOff solvents.lib
HOH = TP3
WAT = TP3
 
#
#   Define the PDB name map for the amino acids and nucleic acids
#
addPdbResMap {
  { 0 "HYP" "NHYP" } { 1 "HYP" "CHYP" }
  { 0 "ALA" "NALA" } { 1 "ALA" "CALA" }
  { 0 "ARG" "NARG" } { 1 "ARG" "CARG" }
  { 0 "ASN" "NASN" } { 1 "ASN" "CASN" }
  { 0 "ASP" "NASP" } { 1 "ASP" "CASP" }
  { 0 "CYS" "NCYS" } { 1 "CYS" "CCYS" }
  { 0 "CYX" "NCYX" } { 1 "CYX" "CCYX" }
  { 0 "GLN" "NGLN" } { 1 "GLN" "CGLN" }
  { 0 "GLU" "NGLU" } { 1 "GLU" "CGLU" }
  { 0 "GLY" "NGLY" } { 1 "GLY" "CGLY" }
  { 0 "HID" "NHID" } { 1 "HID" "CHID" }
  { 0 "HIE" "NHIE" } { 1 "HIE" "CHIE" }
  { 0 "HIP" "NHIP" } { 1 "HIP" "CHIP" }
  { 0 "ILE" "NILE" } { 1 "ILE" "CILE" }
  { 0 "LEU" "NLEU" } { 1 "LEU" "CLEU" }
  { 0 "LYS" "NLYS" } { 1 "LYS" "CLYS" }
  { 0 "MET" "NMET" } { 1 "MET" "CMET" }
  { 0 "PHE" "NPHE" } { 1 "PHE" "CPHE" }
  { 0 "PRO" "NPRO" } { 1 "PRO" "CPRO" }
  { 0 "SER" "NSER" } { 1 "SER" "CSER" }
  { 0 "THR" "NTHR" } { 1 "THR" "CTHR" }
  { 0 "TRP" "NTRP" } { 1 "TRP" "CTRP" }
  { 0 "TYR" "NTYR" } { 1 "TYR" "CTYR" }
  { 0 "VAL" "NVAL" } { 1 "VAL" "CVAL" }
  { 0 "HIS" "NHIS" } { 1 "HIS" "CHIS" }
  { 0 "G" "G5"  } { 1 "G" "G3"  }
  { 0 "A" "A5"  } { 1 "A" "A3"  }
  { 0 "C" "C5"  } { 1 "C" "C3"  }
  { 0 "U" "U5"  } { 1 "U" "U3"  }
  { 0 "DG" "DG5"  } { 1 "DG" "DG3"  }
  { 0 "DA" "DA5"  } { 1 "DA" "DA3"  }
  { 0 "DC" "DC5"  } { 1 "DC" "DC3"  }
  { 0 "DT" "DT5"  } { 1 "DT" "DT3"  }
#  some old Amber residue names for RNA:
  { 0  "RA5" "A5" } { 1 "RA3" "A3"} {"RA" "A" }
  { 0  "RC5" "C5" } { 1 "RC3" "C3"} {"RC" "C" }
  { 0  "RG5" "G5" } { 1 "RG3" "G3"} {"RG" "G" }
  { 0  "RU5" "U5" } { 1 "RU3" "U3"} {"RU" "U" }
#  some really old Amber residue names, assuming DNA:
  { 0 "GUA" "DG5"  } { 1 "GUA" "DG3"  } { "GUA" "DG" }
  { 0 "ADE" "DA5"  } { 1 "ADE" "DA3"  } { "ADE" "DA" }
  { 0 "CYT" "DC5"  } { 1 "CYT" "DC3"  } { "CYT" "DC" }
  { 0 "THY" "DT5"  } { 1 "THY" "DT3"  } { "THY" "DT" }
#  uncomment out the following if you have this old style RNA files:
# { 0 "GUA" "G5"  } { 1 "GUA" "G3"  } { "GUA" "G" }
# { 0 "ADE" "A5"  } { 1 "ADE" "A3"  } { "ADE" "A" }
# { 0 "CYT" "C5"  } { 1 "CYT" "C3"  } { "CYT" "C" }
# { 0 "URA" "R5"  } { 1 "URA" "R3"  } { "URA" "R" }
 
}
 
#  try to be good about reading in really old atom names as well:
addPdbAtomMap {
  { "O5*" "O5'" }
  { "C5*" "C5'" }
  { "C4*" "C4'" }
  { "O4*" "O4'" }
  { "C3*" "C3'" }
  { "O3*" "O3'" }
  { "C2*" "C2'" }
  { "O2*" "O2'" }
  { "C1*" "C1'" }
  { "C5M" "C7"  }
  { "H1*" "H1'" }
  { "H2*1" "H2'" }
  { "H2*2" "H2''" }
  { "H2'1" "H2'" }
  { "H2'2" "H2''" }
  { "H3*" "H3'" }
  { "H4*" "H4'" }
  { "H5*1" "H5'" }
  { "H5*2" "H5''" }
  { "H5'1" "H5'" }
  { "H5'2" "H5''" }
  { "HO'2" "HO2'" }
  { "H5T"  "HO5'" }
  { "H3T"  "HO3'" }
  { "O1'" "O4'" }
  { "OA"  "OP1" }
  { "OB"  "OP2" }
  { "O1P" "OP1" }
  { "O2P" "OP2" }
}
 
#
# assume that most often proteins use HIE
#
NHIS = NHIE
HIS = HIE
CHIS = CHIE
~~~

## leaprc.ff99SB

> leaprc.ff99SB 概要

~~~bash
#   load atom type hybridizations
addAtomTypes {...}
#   Load the main parameter set.
parm99 = loadamberparams parm99.dat
frcmod99SB = loadamberparams frcmod.ff99SB
#   Load DNA/RNA libraries
loadOff all_nucleic94.lib
#   Load main chain and terminating 
#   amino acid libraries (i.e. ff94 libs)
loadOff all_amino94.lib
loadOff all_aminoct94.lib
loadOff all_aminont94.lib
#   Load water and ions
loadOff ions94.lib
loadOff solvents.lib
HOH = TP3
WAT = TP3
#   Define the PDB name map for the amino acids and nucleic acids
addPdbResMap {...}
#  try to be good about reading in really old atom names as well:
addPdbAtomMap {...}
# assume that most often proteins use HIE
NHIS = NHIE
HIS = HIE
CHIS = CHIE
~~~

> leaprc.ff99SB 详细内容

~~~bash
logFile leap.log
#
# ----- leaprc for loading the ff99SB (Hornak & Simmerling) force field
# -----  this file is updated for PDB format 3
#
#   load atom type hybridizations
#
addAtomTypes {
    { "H"   "H" "sp3" }
    { "HO"  "H" "sp3" }
    { "HS"  "H" "sp3" }
    { "H1"  "H" "sp3" }
    { "H2"  "H" "sp3" }
    { "H3"  "H" "sp3" }
    { "H4"  "H" "sp3" }
    { "H5"  "H" "sp3" }
    { "HW"  "H" "sp3" }
    { "HC"  "H" "sp3" }
    { "HA"  "H" "sp3" }
    { "HP"  "H" "sp3" }
    { "OH"  "O" "sp3" }
    { "OS"  "O" "sp3" }
    { "O"   "O" "sp2" }
    { "O2"  "O" "sp2" }
    { "OW"  "O" "sp3" }
    { "CT"  "C" "sp3" }
    { "CH"  "C" "sp3" }
    { "C2"  "C" "sp3" }
    { "C3"  "C" "sp3" }
    { "C"   "C" "sp2" }
    { "C*"  "C" "sp2" }
    { "CA"  "C" "sp2" }
    { "CB"  "C" "sp2" }
    { "CC"  "C" "sp2" }
    { "CN"  "C" "sp2" }
    { "CM"  "C" "sp2" }
    { "CK"  "C" "sp2" }
    { "CQ"  "C" "sp2" }
    { "CD"  "C" "sp2" }
    { "CE"  "C" "sp2" }
    { "CF"  "C" "sp2" }
    { "CP"  "C" "sp2" }
    { "CI"  "C" "sp2" }
    { "CJ"  "C" "sp2" }
    { "CW"  "C" "sp2" }
    { "CV"  "C" "sp2" }
    { "CR"  "C" "sp2" }
    { "CA"  "C" "sp2" }
    { "CY"  "C" "sp2" }
    { "C0"  "Ca" "sp2" }
    { "MG"  "Mg" "sp3" }
    { "N"   "N" "sp2" }
    { "NA"  "N" "sp2" }
    { "N2"  "N" "sp2" }
    { "N*"  "N" "sp2" }
    { "NP"  "N" "sp2" }
    { "NQ"  "N" "sp2" }
    { "NB"  "N" "sp2" }
    { "NC"  "N" "sp2" }
    { "NT"  "N" "sp3" }
    { "N3"  "N" "sp3" }
    { "S"   "S" "sp3" }
    { "SH"  "S" "sp3" }
    { "P"   "P" "sp3" }
    { "LP"  ""  "sp3" }
    { "F"   "F" "sp3" }
    { "CL"  "Cl" "sp3" }
    { "BR"  "Br" "sp3" }
    { "I"   "I"  "sp3" }
    { "FE"  "Fe" "sp3" }
    { "EP"  ""  "sp3" }
# glycam
    { "OG"  "O" "sp3" }
    { "OL"  "O" "sp3" }
    { "AC"  "C" "sp3" }
    { "EC"  "C" "sp3" }
}
#
#   Load the main parameter set.
#
parm99 = loadamberparams parm99.dat
frcmod99SB = loadamberparams frcmod.ff99SB
#
#   Load DNA/RNA libraries
#
loadOff all_nucleic94.lib
#
#   Load main chain and terminating 
#   amino acid libraries (i.e. ff94 libs)
#
loadOff all_amino94.lib
loadOff all_aminoct94.lib
loadOff all_aminont94.lib
#
#       Load water and ions
# 
loadOff ions94.lib
loadOff solvents.lib
HOH = TP3
WAT = TP3
 
#
#   Define the PDB name map for the amino acids and DNA.
#
addPdbResMap {
  { 0 "ALA" "NALA" } { 1 "ALA" "CALA" }
  { 0 "ARG" "NARG" } { 1 "ARG" "CARG" }
  { 0 "ASN" "NASN" } { 1 "ASN" "CASN" }
  { 0 "ASP" "NASP" } { 1 "ASP" "CASP" }
  { 0 "CYS" "NCYS" } { 1 "CYS" "CCYS" }
  { 0 "CYX" "NCYX" } { 1 "CYX" "CCYX" }
  { 0 "GLN" "NGLN" } { 1 "GLN" "CGLN" }
  { 0 "GLU" "NGLU" } { 1 "GLU" "CGLU" }
  { 0 "GLY" "NGLY" } { 1 "GLY" "CGLY" }
  { 0 "HID" "NHID" } { 1 "HID" "CHID" }
  { 0 "HIE" "NHIE" } { 1 "HIE" "CHIE" }
  { 0 "HIP" "NHIP" } { 1 "HIP" "CHIP" }
  { 0 "ILE" "NILE" } { 1 "ILE" "CILE" }
  { 0 "LEU" "NLEU" } { 1 "LEU" "CLEU" }
  { 0 "LYS" "NLYS" } { 1 "LYS" "CLYS" }
  { 0 "MET" "NMET" } { 1 "MET" "CMET" }
  { 0 "PHE" "NPHE" } { 1 "PHE" "CPHE" }
  { 0 "PRO" "NPRO" } { 1 "PRO" "CPRO" }
  { 0 "SER" "NSER" } { 1 "SER" "CSER" }
  { 0 "THR" "NTHR" } { 1 "THR" "CTHR" }
  { 0 "TRP" "NTRP" } { 1 "TRP" "CTRP" }
  { 0 "TYR" "NTYR" } { 1 "TYR" "CTYR" }
  { 0 "VAL" "NVAL" } { 1 "VAL" "CVAL" }
  { 0 "HIS" "NHIS" } { 1 "HIS" "CHIS" }
  { 0 "GUA" "DG5"  } { 1 "GUA" "DG3"  } { "GUA" "DG" }
  { 0 "ADE" "DA5"  } { 1 "ADE" "DA3"  } { "ADE" "DA" }
  { 0 "CYT" "DC5"  } { 1 "CYT" "DC3"  } { "CYT" "DC" }
  { 0 "THY" "DT5"  } { 1 "THY" "DT3"  } { "THY" "DT" }
  { 0 "G" "RG5"  } { 1 "G" "RG3"  } { "G" "RG" } { "GN" "RGN" }
  { 0 "A" "RA5"  } { 1 "A" "RA3"  } { "A" "RA" } { "AN" "RAN" }
  { 0 "C" "RC5"  } { 1 "C" "RC3"  } { "C" "RC" } { "CN" "RCN" }
  { 0 "U" "RU5"  } { 1 "U" "RU3"  } { "U" "RU" } { "UN" "RUN" }
  { 0 "DG" "DG5"  } { 1 "DG" "DG3"  }
  { 0 "DA" "DA5"  } { 1 "DA" "DA3"  }
  { 0 "DC" "DC5"  } { 1 "DC" "DC3"  }
  { 0 "DT" "DT5"  } { 1 "DT" "DT3"  }
 
}
 
addPdbAtomMap {
  { "O5*" "O5'" }
  { "C5*" "C5'" }
  { "C4*" "C4'" }
  { "O4*" "O4'" }
  { "C3*" "C3'" }
  { "O3*" "O3'" }
  { "C2*" "C2'" }
  { "C1*" "C1'" }
  { "C5M" "C7"  }
  { "O2*" "O2'" }
  { "H1*" "H1'" }
  { "H2*1" "H2'1" }
  { "H2*2" "H2'2" }
  { "H2'"  "H2'1" }
  { "H2''" "H2'2" }
  { "H3*" "H3'" }
  { "H4*" "H4'" }
  { "H5*1" "H5'1" }
  { "H5*2" "H5'2" }
  { "H5'"  "H5'1" }
  { "H5''" "H5'2" }
  { "HO2'" "HO'2" }
  { "HO5'" "H5T" }
  { "HO3'" "H3T" }
  { "O1'" "O4'" }
  { "OA"  "O1P" }
  { "OB"  "O2P" }
  { "OP1" "O1P" }
  { "OP2" "O2P" }
}
 
 
#
# assumed that most often proteins use HIE
#
NHIS = NHIE
HIS = HIE
CHIS = CHIE
~~~

## leaprc.gaff

> leaprc.gaff 详细内容

~~~bash
logFile leap.log
#
# ----- leaprc for loading the general Amber Force field.
#       This file is mostly for use with Antechamber
#
#   load atom type hybridizations
#
addAtomTypes {
    { "h1"  "H" "sp3" }
    { "h2"  "H" "sp3" }
    { "h3"  "H" "sp3" }
    { "h4"  "H" "sp3" }
    { "h5"  "H" "sp3" }
    { "ha"  "H" "sp3" }
    { "hc"  "H" "sp3" }
    { "hn"  "H" "sp3" }
    { "ho"  "H" "sp3" }
    { "hp"  "H" "sp3" }
    { "hs"  "H" "sp3" }
    { "hw"  "H" "sp3" }
    { "hx"  "H" "sp3" }
    { "o"  "O" "sp2" }
    { "o2"  "O" "sp2" }
    { "oh"  "O" "sp3" }
    { "os"  "O" "sp3" }
    { "ow"  "O" "sp3" }
    { "c"  "C" "sp2" }
    { "c1"  "C" "sp2" }
    { "c2"  "C" "sp2" }
    { "c3"  "C" "sp3" }
    { "ca"  "C" "sp2" }
    { "cc"  "C" "sp2" }
    { "cd"  "C" "sp2" }
    { "ce"  "C" "sp2" }
    { "cf"  "C" "sp2" }
    { "cg"  "C" "sp2" }
    { "ch"  "C" "sp2" }
    { "cp"  "C" "sp2" }
    { "cq"  "C" "sp2" }
    { "cu"  "C" "sp2" }
    { "cv"  "C" "sp2" }
    { "cx"  "C" "sp2" }
    { "cy"  "C" "sp2" }
    { "cz"  "C" "sp2" }
    { "n"   "N" "sp2" }
    { "n1"  "N" "sp2" }
    { "n2"  "N" "sp2" }
    { "n3"  "N" "sp3" }
    { "n4"  "N" "sp3" }
    { "na"  "N" "sp2" }
    { "nb"  "N" "sp2" }
    { "nc"  "N" "sp2" }
    { "nd"  "N" "sp2" }
    { "ne"  "N" "sp2" }
    { "nf"  "N" "sp2" }
    { "nh"  "N" "sp2" }
    { "no"  "N" "sp2" }
    { "s"   "S" "sp2" }
    { "s2"   "S" "sp2" }
    { "s3"   "S" "sp3" }
    { "s4"   "S" "sp3" }
    { "s6"   "S" "sp3" }
    { "sh"   "S" "sp3" }
    { "ss"   "S" "sp3" }
    { "sx"   "S" "sp3" }
    { "sy"   "S" "sp3" }
    { "p2"   "P" "sp2" }
    { "p3"   "P" "sp3" }
    { "p4"   "P" "sp3" }
    { "p5"   "P" "sp3" }
    { "pb"   "P" "sp3" }
    { "pc"   "P" "sp3" }
    { "pd"   "P" "sp3" }
    { "pe"   "P" "sp3" }
    { "pf"   "P" "sp3" }
    { "px"   "P" "sp3" }
    { "py"   "P" "sp3" }
    { "f"   "F" "sp3" }
    { "cl"  "Cl" "sp3" }
    { "br"  "Br" "sp3" }
    { "i"   "I"  "sp3" }
}
#
#   Load the general force field parameter set.
#
gaff = loadamberparams gaff.dat
~~~

------
