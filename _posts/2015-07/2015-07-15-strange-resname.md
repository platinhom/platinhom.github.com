---
layout: post
title: 20种氨基酸以外常见残基名字
date: 2015-07-15 04:17:23
categories: CompCB
tags: CompBiol
---

资料主要源于Jocobson网站(Ref1),作了修改添加.  
The main source from Jocobson's lab. I added some more informations here.


## Standard amino acids:
 
All standard amino acids are referred to using their 3 letter codes.
 
Note that specific protonation states for residues with titratable side chains can be specified, and are referred to with the following codes:
 
- ASH:  neutral ASP
- GLH:  neutral GLU
- LYN:  neutral LYS
- ARN:  neutral ARG
- HID:  neutral HIS, protonated at delta position
- HIE:  neutral HIS, protonated at epsilon position
- HIP:  positively charge HIS (protonated at both positions)
- TYM:  negatively charged TYR
- CYM:  negatively charged CYS
- CYX:	SS-bonded CYS
- NALA or ALAB: N-terminal residue
- CALA or ALAE: C-terminal residue
- DA5: 5-terminal DA
- DA3: 3-terminal DA

 
By default, the terminal residues are charged (positively charged amino group on N-terminus; negatively charged carboxylate on C-terminus).  These residues have an appended letter to distinguish them, "B" for the N-terminus ("beginning"), and "E" for C-terminus ("ending"), e.g., ALAB and ALAE for terminal alanines.
 
 
## Nonstandard amino acids
 
- SEP:  phosphorylated serine
- TPO:  phosphorylated threonine
- PTR:  phosphorylated tyrosine
- ASQ:  phosphorylated Asp
- NLE:  norleucine (frequently used non-natural)
- AIB:  aminobutyric acid
- MSE:  seleno-methionine
- HYP:  hydroxyproline
- MMO:  N-methyl Arg
 
## D amino acids
 
- DAL:  D-Ala
- DVA:  D-Val
- DLE:  D-Leu
- DLY:  D-Lys
- DTY:  D-Tyr
- DTR:  D-Trp
 
## Monoatomic ions
 
- NA:  sodium (1+)
- K:  potassium (1+)
- CA:  calcium (2+)
- MG:  magnesium (2+)
- FE:  iron (3+)
- ZN:  zinc (2+)
- CO:  cobalt (2+)
- CL:  chloride (1-)
 
 
## Capping groups:
 
There are a variety of options for terminating the chain. 

- ACE:  acetyl (N-terminus)
- NMA:  N-methyl amide (C-terminus)
- PCA:  pyroglutamic acid (N-terminus)
- NH2:  amide cap (N-terminus; like NMA, except without the methyl)
- ASA:  aspartic aldehyde (C-terminus; ASP, but with aldehyde terminus)

Note that the common capping groups ACE, NH2, and NMA create an additional peptide bond.  PCA is somewhat more exotic, and results from a GLU side chain forming a cyclic amide with the N-terminus.   All of the listed caps create a neutral terminus.
 
 
## Common ligands:
 
Many ligands are now supported, in fact most ligands found in the PDB have been atomtyped.  Some common ones include HEM (heme) and COA (acetyl CoA).  There are about 3000 others.  Naming conventions are intended to match those approved by the PDB, i.e., 3-letter codes, which can be found in databases such as HIC-UP. H2O/WAT for water.

## Reference:

1. [Jocobson lab](http://www.jacobsonlab.org/plop_manual/plop_residues.htm)

------
