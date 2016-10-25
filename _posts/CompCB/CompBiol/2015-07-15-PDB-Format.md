---
layout: post
title: PDB格式-原子部分
date: 2015-07-15 00:21:39
categories: CompCB
tags: CompBiol
---

-  1 -  6        Record name     "ATOM  "/"HETATM"/"TER   "                                          
-  7 - 11        Integer         Atom serial number.                   
- 13 - 16        Atom            Atom name.                            
- 17             Character       Alternate location indicator.         
- 18 - 20        Residue name    Residue name.                         
- 22             Character       Chain identifier.                     
- 23 - 26        Integer         Residue sequence number.              
- 27             AChar           Code for insertion of residues.       
- 31 - 38        Real(8.3)       Orthogonal coordinates for X in Angstroms.                       
- 39 - 46        Real(8.3)       Orthogonal coordinates for Y in Angstroms.                            
- 47 - 54        Real(8.3)       Orthogonal coordinates for Z in Angstroms.                            
- 55 - 60        Real(6.2)       Occupancy.                            
- 61 - 66        Real(6.2)       Temperature factor (Default = 0.0).                   
- 73 - 76        LString(4)      Segment identifier, left-justified.   
- 77 - 78        LString(2)      Element symbol, right-justified.      
- 79 - 80        LπString(2)      Charge on the atom. 

PQR file use 55 - 62 column for charges and 63 - 69 column for radii.
But the PQR generated from Amber may 55 - 62 column for charges and 63 - 70 column for radii.
mpdb in amber may 55 - 64 column for charges and 65 - 72 column for radii, 79-80 for atom type.

Example

~~~
         1         2         3         4         5         6         7         8
12345678901234567890123456789012345678901234567890123456789012345678901234567890
ATOM    145  N   VAL A  25      32.433  16.336  57.540  1.00 11.92      A1   N
ATOM    146  CA  VAL A  25      31.132  16.439  58.160  1.00 11.85      A1   C
ATOM    147  C   VAL A  25      30.447  15.105  58.363  1.00 12.34      A1   C
ATOM    148  O   VAL A  25      29.520  15.059  59.174  1.00 15.65      A1   O
ATOM    149  CB AVAL A  25      30.385  17.437  57.230  0.28 13.88      A1   C
ATOM    150  CB BVAL A  25      30.166  17.399  57.373  0.72 15.41      A1   C
ATOM    151  CG1AVAL A  25      28.870  17.401  57.336  0.28 12.64      A1   C
ATOM    152  CG1BVAL A  25      30.805  18.788  57.449  0.72 15.11      A1   C
ATOM    153  CG2AVAL A  25      30.835  18.826  57.661  0.28 13.58      A1   C
ATOM    154  CG2BVAL A  25      29.909  16.996  55.922  0.72 13.25      A1   C
~~~

## Reference
1. [RCSB-PDB](http://deposit.rcsb.org/adit/docs/pdb_atom_format.html)

------
