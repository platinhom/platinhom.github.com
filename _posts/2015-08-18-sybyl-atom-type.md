---
layout: post
title: Sybyl原子类型
date: 2015-08-18 12:13:50
categories: CompCB
tags: CompBiol
---

## Sybyl atom type

| Code	| Definition	| Code	| Definition
| C.3	| carbon sp3| H| hydrogen
| C.2| carbon sp2| H.spc| hydrogen in Single Point Charge (SPC) water model
| C.1| carbon sp| H.t3p| hydrogen in Transferable intermolecular Potential (TIP3P) water model
| C.ar| carbon aromatic| LP| lone pair
| C.cat| carbocation (C+) used only in a guadinium group| Du| dummy atom
| N.3| nitrogen sp3 | Du.C| dummy carbon
| N.2| nitrogen sp2 | Any| any atom
| N.1| nitrogen sp | Hal| halogen
| N.ar| nitrogen aromatic | Het| heteroatom = N, O, S, P
| N.am| nitrogen amide | Hev| heavy atom (non hydrogen)
| N.pl3| nitrogen trigonal planar | Li| lithium
| N.4| nitrogen sp3 positively charged | Na| sodium
| O.3| oxygen sp3 | Mg| magnesium
| O.2| oxygen sp2 | Al| aluminum
| O.co2| oxygen in carboxylate and phosphate groups| Si| silicon
| O.spc| oxygen in Single Point Charge (SPC) water model| K| potassium
| O.t3p| oxygen in Transferable Intermolecular Potential (TIP3P) water model| Ca| calcium
| S.3| sulfur sp3| Cr.th| chromium (tetrahedral)
| S.2| sulfur sp2| Cr.oh| chromium (octahedral)
| S.O| sulfoxide sulfur| Mn| manganese
| S.O2| sulfone sulfur| Fe| iron
| P.3| phosphorous sp3| Co.oh| cobalt (octahedral)
| F| fluorine| Cu| copper
| Cl| chlorine| Zn| zinc
| Br| bromine| Se| selenium
| I| iodine| Mo| molybdenum
| �| �| Sn| tin

O.co2 只有在COO- 这种质子化状态才出现(否则就是O.2+O.3). 同理N.4也是(否则N.3).

## Reference

1. [Tripos mol2 atom types](http://www.tripos.com/mol2/atom_types.html)

------
