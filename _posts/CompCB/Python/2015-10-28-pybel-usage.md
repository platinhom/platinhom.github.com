---
layout: post
title: pybel使用
date: 2015-10-28 12:05:13
categories: CompCB
tags: Python CompChem
---

Pybel提供了一些简单的Openbabel的功能和对象.Pybel1.8(对应OB-2.3.2)提供的功能很有限, 主要有两个类继承自OB: OBAtom和OBMol.  
Molecule是其主要功能实现的对象,提供以下功能:  
    - 读取写出分子
    - 加氢去氢
    - 产生3维结构并优化
    - 计算分子指纹和分子描述符
    - SMART匹配
    - 生成2D坐标并出图

## pybel主要内容

- Global variables:  
informats, outformats, descs, fps, forcefields, operations, ob(openbabel)
- Functions:  
readfile(), readstring()
- Classes:  
Atom, Molecule, Outputfile, Fingerprint, Smarts, MoleculeData

## 全局变量

- informats: 支持的输入格式:  
'CONFIG': 'DL-POLY CONFIG', 'CONTCAR': 'VASP format', 'HISTORY': 'DL-POLY HISTORY', 'POSCAR': 'VASP format', 'VASP': 'VASP format', 'abinit': 'ABINIT Output Format', 'acesout': 'ACES output format', 'acr': 'ACR format', 'adfout': 'ADF output format', 'alc': 'Alchemy format', 'arc': 'Accelrys/MSI Biosym/Insight II CAR format', 'axsf': 'XCrySDen Structure Format', 'bgf': 'MSI BGF format', 'box': 'Dock 3.5 Box format', 'bs': 'Ball and Stick format', 'c09out': 'Crystal 09 output format', 'c3d1': 'Chem3D Cartesian 1 format', 'c3d2': 'Chem3D Cartesian 2 format', 'caccrt': 'Cacao Cartesian format', 'can': 'Canonical SMILES format', 'car': 'Accelrys/MSI Biosym/Insight II CAR format', 'castep': 'CASTEP format', 'ccc': 'CCC format', 'cdx': 'ChemDraw binary format', 'cdxml': 'ChemDraw CDXML format', 'cif': 'Crystallographic Information File', 'ck': 'ChemKin format', 'cml': 'Chemical Markup Language', 'cmlr': 'CML Reaction format', 'crk2d': 'Chemical Resource Kit diagram(2D)', 'crk3d': 'Chemical Resource Kit 3D format', 'ct': 'ChemDraw Connection Table format', 'cub': 'Gaussian cube format', 'cube': 'Gaussian cube format', 'dat': 'Generic Output file format', 'dmol': 'DMol3 coordinates format', 'dx': 'OpenDX cube format for APBS', 'ent': 'Protein Data Bank format', 'fa': 'FASTA format', 'fasta': 'FASTA format', 'fch': 'Gaussian formatted checkpoint file format', 'fchk': 'Gaussian formatted checkpoint file format', 'fck': 'Gaussian formatted checkpoint file format', 'feat': 'Feature format', 'fhiaims': 'FHIaims XYZ format', 'fract': 'Free Form Fractional format', 'fs': 'Fastsearch format', 'fsa': 'FASTA format', 'g03': 'Gaussian Output', 'g09': 'Gaussian Output', 'g92': 'Gaussian Output', 'g94': 'Gaussian Output', 'g98': 'Gaussian Output', 'gal': 'Gaussian Output', 'gam': 'GAMESS Output', 'gamess': 'GAMESS Output', 'gamin': 'GAMESS Input', 'gamout': 'GAMESS Output', 'got': 'GULP format', 'gpr': 'Ghemical format', 'gro': 'GRO format', 'gukin': 'GAMESS-UK Input', 'gukout': 'GAMESS-UK Output', 'gzmat': 'Gaussian Z-Matrix Input', 'hin': 'HyperChem HIN format', 'inchi': 'InChI format', 'inp': 'GAMESS Input', 'ins': 'ShelX format', 'jout': 'Jaguar output format', 'log': 'Generic Output file format', 'mcdl': 'MCDL format', 'mcif': 'Macromolecular Crystallographic Info', 'mdl': 'MDL MOL format', 'ml2': 'Sybyl Mol2 format', 'mmcif': 'Macromolecular Crystallographic Info', 'mmd': 'MacroModel format', 'mmod': 'MacroModel format', 'mol': 'MDL MOL format', 'mol2': 'Sybyl Mol2 format', 'mold': 'Molden format', 'molden': 'Molden format', 'molf': 'Molden format', 'moo': 'MOPAC Output format', 'mop': 'MOPAC Cartesian format', 'mopcrt': 'MOPAC Cartesian format', 'mopin': 'MOPAC Internal', 'mopout': 'MOPAC Output format', 'mpc': 'MOPAC Cartesian format', 'mpo': 'Molpro output format', 'mpqc': 'MPQC output format', 'mrv': 'Chemical Markup Language', 'msi': 'Accelrys/MSI Cerius II MSI format', 'nwo': 'NWChem output format', 'out': 'Generic Output file format', 'outmol': 'DMol3 coordinates format', 'output': 'Generic Output file format', 'pc': 'PubChem format', 'pcm': 'PCModel Format', 'pdb': 'Protein Data Bank format', 'pdbqt': 'AutoDock PDQBT format', 'png': 'PNG 2D depiction', 'pos': 'POS cartesian coordinates format', 'pqr': 'PQR format', 'pqs': 'Parallel Quantum Solutions format', 'prep': 'Amber Prep format', 'pwscf': 'PWscf format', 'qcout': 'Q-Chem output format', 'res': 'ShelX format', 'rsmi': 'Reaction SMILES format', 'rxn': 'MDL RXN format', 'sd': 'MDL MOL format', 'sdf': 'MDL MOL format', 'smi': 'SMILES format', 'smiles': 'SMILES format', 'sy2': 'Sybyl Mol2 format', 't41': 'ADF TAPE41 format', 'tdd': 'Thermo format', 'text': 'Read and write raw text', 'therm': 'Thermo format', 'tmol': 'TurboMole Coordinate format', 'txt': 'Title format', 'txyz': 'Tinker XYZ format', 'unixyz': 'UniChem XYZ format', 'vmol': 'ViewMol format', 'xml': 'General XML format', 'xsf': 'XCrySDen Structure Format', 'xtc': 'XTC format', 'xyz': 'XYZ cartesian coordinates format', 'yob': 'YASARA.org YOB format'
- outformats: 支持的输出格式:  
'CONFIG': 'DL-POLY CONFIG', 'CONTCAR': 'VASP format', 'POSCAR': 'VASP format', 'VASP': 'VASP format', 'acesin': 'ACES input format', 'adf': 'ADF cartesian input format', 'alc': 'Alchemy format', 'ascii': 'ASCII format', 'bgf': 'MSI BGF format', 'box': 'Dock 3.5 Box format', 'bs': 'Ball and Stick format', 'c3d1': 'Chem3D Cartesian 1 format', 'c3d2': 'Chem3D Cartesian 2 format', 'cac': 'CAChe MolStruct format', 'caccrt': 'Cacao Cartesian format', 'cache': 'CAChe MolStruct format', 'cacint': 'Cacao Internal format', 'can': 'Canonical SMILES format', 'cdxml': 'ChemDraw CDXML format', 'cht': 'Chemtool format', 'cif': 'Crystallographic Information File', 'ck': 'ChemKin format', 'cml': 'Chemical Markup Language', 'cmlr': 'CML Reaction format', 'com': 'Gaussian 98/03 Input', 'copy': 'Copy raw text', 'crk2d': 'Chemical Resource Kit diagram(2D)', 'crk3d': 'Chemical Resource Kit 3D format', 'csr': 'Accelrys/MSI Quanta CSR format', 'cssr': 'CSD CSSR format', 'ct': 'ChemDraw Connection Table format', 'cub': 'Gaussian cube format', 'cube': 'Gaussian cube format', 'dmol': 'DMol3 coordinates format', 'dx': 'OpenDX cube format for APBS', 'ent': 'Protein Data Bank format', 'fa': 'FASTA format', 'fasta': 'FASTA format', 'feat': 'Feature format', 'fh': 'Fenske-Hall Z-Matrix format', 'fhiaims': 'FHIaims XYZ format', 'fix': 'SMILES FIX format', 'fps': 'FPS text fingerprint format (Dalke)', 'fpt': 'Fingerprint format', 'fract': 'Free Form Fractional format', 'fs': 'Fastsearch format', 'fsa': 'FASTA format', 'gamin': 'GAMESS Input', 'gau': 'Gaussian 98/03 Input', 'gjc': 'Gaussian 98/03 Input', 'gjf': 'Gaussian 98/03 Input', 'gpr': 'Ghemical format', 'gr96': 'GROMOS96 format', 'gro': 'GRO format', 'gukin': 'GAMESS-UK Input', 'gukout': 'GAMESS-UK Output', 'gzmat': 'Gaussian Z-Matrix Input', 'hin': 'HyperChem HIN format', 'inchi': 'InChI format', 'inchikey': 'InChIKey', 'inp': 'GAMESS Input', 'jin': 'Jaguar input format', 'k': 'Compare molecules using InChI', 'lmpdat': 'The LAMMPS data format', 'mcdl': 'MCDL format', 'mcif': 'Macromolecular Crystallographic Info', 'mdl': 'MDL MOL format', 'ml2': 'Sybyl Mol2 format', 'mmcif': 'Macromolecular Crystallographic Info', 'mmd': 'MacroModel format', 'mmod': 'MacroModel format', 'mna': 'Multilevel Neighborhoods of Atoms (MNA)', 'mol': 'MDL MOL format', 'mol2': 'Sybyl Mol2 format', 'mold': 'Molden format', 'molden': 'Molden format', 'molf': 'Molden format', 'molreport': 'Open Babel molecule report', 'mop': 'MOPAC Cartesian format', 'mopcrt': 'MOPAC Cartesian format', 'mopin': 'MOPAC Internal', 'mp': 'Molpro input format', 'mpc': 'MOPAC Cartesian format', 'mpd': 'MolPrint2D format', 'mpqcin': 'MPQC simplified input format', 'mrv': 'Chemical Markup Language', 'msms': "M.F. Sanner's MSMS input format", 'nul': 'Outputs nothing', 'nw': 'NWChem input format', 'outmol': 'DMol3 coordinates format', 'pcm': 'PCModel Format', 'pdb': 'Protein Data Bank format', 'pdbqt': 'AutoDock PDQBT format', 'png': 'PNG 2D depiction', 'pov': 'POV-Ray input format', 'pqr': 'PQR format', 'pqs': 'Parallel Quantum Solutions format', 'qcin': 'Q-Chem input format', 'report': 'Open Babel report format', 'rsmi': 'Reaction SMILES format', 'rxn': 'MDL RXN format', 'sd': 'MDL MOL format', 'sdf': 'MDL MOL format', 'smi': 'SMILES format', 'smiles': 'SMILES format', 'svg': 'SVG 2D depiction', 'sy2': 'Sybyl Mol2 format', 'tdd': 'Thermo format', 'text': 'Read and write raw text', 'therm': 'Thermo format', 'tmol': 'TurboMole Coordinate format', 'txt': 'Title format', 'txyz': 'Tinker XYZ format', 'unixyz': 'UniChem XYZ format', 'vmol': 'ViewMol format', 'xed': 'XED format', 'xyz': 'XYZ cartesian coordinates format', 'yob': 'YASARA.org YOB format', 'zin': 'ZINDO input format'
- descs: 支持的描述符: 'abonds', 'atoms', 'bonds', 'cansmi', 'cansmiNS', 'dbonds', 'formula', 'HBA1', 'HBA2', 'HBD', 'InChI', 'InChIKey', 'L5', 'logP', 'MP', 'MR', 'MW', 'nF', 's', 'sbonds', 'smarts', 'tbonds', 'title', 'TPSA'
- fps: 支持的指纹类型: 'fp2', 'fp3', 'fp4', 'maccs'
- forcefields: 支持的力场: 'gaff', 'ghemical', 'mmff94', 'mmff94s', 'uff'
- operations: 支持的操作: 0xout, addfilename, AddInIndex, AddPolarH, align, canonical, conformer, energy, fillUC, gen2D, gen3D, genalias, highlight, largest, minimize, partialcharge, readconformer, s, smallest, sort, unique, v
- ob(openbabel): 就是openbabel模块,另外还加载了sys, math, os.path, tempfile, PIL, Tk, piltk

附:   

### descriptors

- abonds    Number of aromatic bonds
- atoms    Number of atoms
- bonds    Number of bonds
- cansmi    Canonical SMILES
- cansmiNS    Canonical SMILES without isotopes or stereo
- dbonds    Number of double bonds
- formula    Chemical formula
- HBA1    Number of Hydrogen Bond Acceptors 1 (JoelLib)
- HBA2    Number of Hydrogen Bond Acceptors 2 (JoelLib)
- HBD    Number of Hydrogen Bond Donors (JoelLib)
- InChI    IUPAC InChI identifier
- InChIKey    InChIKey
- L5    Lipinski Rule of Five
- logP    octanol/water partition coefficient
- MP    Melting point
- MR    molar refractivity
- MW    Molecular Weight filter
- nF    Number of Fluorine Atoms
- s    SMARTS filter
- sbonds    Number of single bonds
- smarts    SMARTS filter
- tbonds    Number of triple bonds
- title    For comparing a molecule's title

## 函数

- readfile(format, filename, opt=None): 格式参考以上的informats, 文件就是读取的文件罗,opt是格式选项的指定专用的字典. 注意, 返回的是**迭代器**!! 用next()来读取!
- readstring(format,string,opt=None): 同上,只是把原有的文件变换成字符串形式. 一般用于smile式(smi). 返回的是**一个分子**.

应用例子:

~~~python
mol = readfile("smi", "myfile.smi").next() # Python 2
mol = next(readfile("smi", "myfile.smi"))  # Python 3

# You can make a list of the molecules in a file using:
mols = list(readfile("smi", "myfile.smi"))

#You can iterate over the molecules in a file as shown in the following code snippet:
atomtotal = 0
for mol in readfile("sdf", "head.sdf"):
	atomtotal += len(mol.atoms)

#Generate mol from smile string
mymol = readstring("smi", "C1=CC=CS1")
~~~

## 类

- **Outputfile**(format, filename, overwrite=False, opt=None)  
用于写出多个分子, 单个分子可以用分子对象的write(). 格式就是outformats支持的格式,第二参数是文件名咯.第三个是否覆盖已有文件,opt就是格式专有选项.
	- close():关闭该文件不能再写入.
	- write(molecule):将分子写入文件.
- **Fingerprint**(fingerprint)  
参数是OBFingerprint.FindFingerprint()计算出的vector. 属性bits是相应的指纹列表, `|`支持或操作例如 *tanimoto = a | b*
- **Smarts**(smartspattern)  
SMART式匹配器. 输入参数是SMART式字符串.  
	- findall(molecule): 在分子中搜索SMART式,返回匹配的所有元组的list.每个元组包含相应匹配的原子序号(1开始).元组数就是匹配子结构数量.
- **Molecule**(OBMol):
分子,需要参数OBMol(openbabel的分子对象).也可以用 *readfile*/*readstring* 函数产生. 该对象也是pybel主要使用对象.  
    - OBMol: 就是OB的分子,内含相应的C++方法
	- atoms: 原子对象的列表
	- charge: 分子电荷
	- conformers: 构象?返回的是c++ vector.
	- data: 返回分子一些属性信息的字典,用于构造MoleculeData.
	- dim: 返回Long型?! 的整数,0/2/3维
	- energy: 返回分子的能量
	- exactmass: 精确分子量
	- formula: 分子式
	- molwt: 分子量
	- spin: 自旋度
	- sssr: 最小环的集合(C++)
	- title: 分子名
	- unitcell: 晶胞信息,有的话.
	- addh(): 加氢
	- removeh(): 去氢
	- calcfp(fptype='FP2'): 计算指纹返回指纹对象Fingerprint.指纹类型参考全局变量
	- calcdesc(descnames=[]): 计算相应描述符, 如果不指名就会全部计算.描述符参考全局变量.
	- draw(show=True, filename=None, update=False, usecoords=False): 产生2维分子描述.show是否在屏幕显示, filename可以指定写到图像文件,后两者是否更新以及使用现有坐标.
	- localopt(forcefield='mmff94', steps=500): 局部优化,力场和优化步数.如果没有坐标会优先使用make3D().需要分子有H.
	- make3D(forcefield='mmff94', steps=50): 先产生3维坐标再调用局部优化,参数是局部优化参数.
	- write(format='smi', filename=None, overwrite=False): 将文件写到文件,格式,文件名以及是否覆盖已有文件. 如果不指名文件名, 返回文件内容的字符串.
- **MoleculeData**(obmol)  
使用ob的分子产生相应附加数据的对象, 一个类似于字典的对象. 其实用途不大,更常用mol.data.
- **Atom**(OBAtom)  
使用OB的原子对象来构造, 或者读入分子后储存在Molecule.atoms里的对象.  
    - OBAtom: 就是OB的原子.可以调用相关方法属性.
    - atomicmass: 原子量
    - exactmass: 精确原子量
    - atomicnum: 元素号
    - type: 原子类型
    - spin: 自旋态
    - hyb: 杂化态(1,2,3)
    - idx: 索引号(1起)
    - coordidx: 配位索引号?
    - cidx: Cidx??
    - isotope: 同位素,要是非同位素就为0
    - coords: 3维坐标, 元组.
    - formalcharge: formal电荷
    - partialcharge: 部分电荷
    - valence: 连接数
    - implicitvalence: 可能的最大连接数
    - heavyvalence: 相连重原子价数
    - heterovalence: 相连杂原子价数
    - vector: 坐标的c++vector

注意, 新版本的可能略有不同,如mac上还有Residue对象等.

## pybel源代码(1.8)

~~~python
#-*. coding: utf-8 -*-
## Copyright (c) 2008-2012, Noel O'Boyle; 2012, Adrià Cereto-Massagué
## All rights reserved.
##
##  This file is part of Cinfony.
##  The contents are covered by the terms of the GPL v2 license
##  which is included in the file LICENSE_GPLv2.txt.

"""
pybel - A Cinfony module for accessing Open Babel

Global variables:
  ob - the underlying SWIG bindings for Open Babel
  informats - a dictionary of supported input formats
  outformats - a dictionary of supported output formats
  descs - a list of supported descriptors
  fps - a list of supported fingerprint types
  forcefields - a list of supported forcefields
"""

import sys
import math
import os.path
import tempfile

if sys.platform[:4] == "java":
    import org.openbabel as ob
    import java.lang.System
    java.lang.System.loadLibrary("openbabel_java")
    _obfuncs = ob.openbabel_java
    _obconsts = ob.openbabel_javaConstants
    import javax
elif sys.platform[:3] == "cli":
    import System
    import clr
    clr.AddReference('System.Windows.Forms')
    clr.AddReference('System.Drawing')
     
    from System.Windows.Forms import (
        Application, DockStyle, Form, PictureBox, PictureBoxSizeMode
        )
    from System.Drawing import Image, Size

    _obdotnet = os.environ["OBDOTNET"]
    if _obdotnet[0] == '"': # Remove trailing quotes
        _obdotnet = _obdotnet[1:-1]
    clr.AddReferenceToFileAndPath(os.path.join(_obdotnet, "OBDotNet.dll"))
    import OpenBabel as ob
    _obfuncs = ob.openbabel_csharp
    _obconsts = ob.openbabel_csharp
else:
    import openbabel as ob
    _obfuncs = _obconsts = ob
    try:
        import Tkinter as tk
        from PIL import Image as PIL
        from PIL import ImageTk as piltk
    except ImportError: #pragma: no cover
        tk = None

def _formatstodict(list):
    if sys.platform[:4] == "java":
        list = [list.get(i) for i in range(list.size())]
    broken = [x.replace("[Read-only]", "").replace("[Write-only]","").split(" -- ") for x in list]
    broken = [(x,y.strip()) for x,y in broken]
    return dict(broken)
_obconv = ob.OBConversion()
_builder = ob.OBBuilder()
informats = _formatstodict(_obconv.GetSupportedInputFormat())
"""A dictionary of supported input formats"""
outformats = _formatstodict(_obconv.GetSupportedOutputFormat())
"""A dictionary of supported output formats"""

def _getplugins(findplugin, names):
    plugins = dict([(x, findplugin(x)) for x in names if findplugin(x)])
    return plugins
def _getpluginnames(ptype):
    if sys.platform[:4] == "cli":
        plugins = ob.VectorString()
    else:
        plugins = ob.vectorString()
    ob.OBPlugin.ListAsVector(ptype, None, plugins)
    if sys.platform[:4] == "java":
        plugins = [plugins.get(i) for i in range(plugins.size())]
    return [x.split()[0] for x in plugins]

descs = _getpluginnames("descriptors")
"""A list of supported descriptors"""
_descdict = _getplugins(ob.OBDescriptor.FindType, descs)
fps = [_x.lower() for _x in _getpluginnames("fingerprints")]
"""A list of supported fingerprint types"""
_fingerprinters = _getplugins(ob.OBFingerprint.FindFingerprint, fps)
forcefields = [_x.lower() for _x in _getpluginnames("forcefields")]
"""A list of supported forcefields"""
_forcefields = _getplugins(ob.OBForceField.FindType, forcefields)
operations = _getpluginnames("ops")
"""A list of supported operations"""
_operations = _getplugins(ob.OBOp.FindType, operations)

def readfile(format, filename, opt=None):
    """Iterate over the molecules in a file.

    Required parameters:
       format - see the informats variable for a list of available
                input formats
       filename

    Optional parameters:
       opt    - a dictionary of format-specific options
                For format options with no parameters, specify the
                value as None.

    You can access the first molecule in a file using the next() method
    of the iterator (or the next() keyword in Python 3):
        mol = readfile("smi", "myfile.smi").next() # Python 2
        mol = next(readfile("smi", "myfile.smi"))  # Python 3

    You can make a list of the molecules in a file using:
        mols = list(readfile("smi", "myfile.smi"))

    You can iterate over the molecules in a file as shown in the
    following code snippet:
    >>> atomtotal = 0
    >>> for mol in readfile("sdf", "head.sdf"):
    ...     atomtotal += len(mol.atoms)
    ...
    >>> print atomtotal
    43
    """
    if opt == None:
        opt = {}
    obconversion = ob.OBConversion()
    formatok = obconversion.SetInFormat(format)
    for k, v in opt.items():
        if v == None:
            obconversion.AddOption(k, obconversion.INOPTIONS)
        else:
            obconversion.AddOption(k, obconversion.INOPTIONS, str(v))
    if not formatok:
        raise ValueError("%s is not a recognised Open Babel format" % format)
    if not os.path.isfile(filename):
        raise IOError("No such file: '%s'" % filename)
    def filereader():
        obmol = ob.OBMol()
        notatend = obconversion.ReadFile(obmol,filename)
        while notatend:
            yield Molecule(obmol)
            obmol = ob.OBMol()
            notatend = obconversion.Read(obmol)
    return filereader()

def readstring(format, string, opt=None):
    """Read in a molecule from a string.

    Required parameters:
       format - see the informats variable for a list of available
                input formats
       string

    Optional parameters:
       opt    - a dictionary of format-specific options
                For format options with no parameters, specify the
                value as None.

    Example:
    >>> input = "C1=CC=CS1"
    >>> mymol = readstring("smi", input)
    >>> len(mymol.atoms)
    5
    """
    if opt == None:
        opt = {}

    obmol = ob.OBMol()
    obconversion = ob.OBConversion()

    formatok = obconversion.SetInFormat(format)
    if not formatok:
        raise ValueError("%s is not a recognised Open Babel format" % format)
    for k, v in opt.items():
        if v == None:
            obconversion.AddOption(k, obconversion.INOPTIONS)
        else:
            obconversion.AddOption(k, obconversion.INOPTIONS, str(v))

    success = obconversion.ReadString(obmol, string)
    if not success:
        raise IOError("Failed to convert '%s' to format '%s'" % (
            string, format))
    return Molecule(obmol)

class Outputfile(object):
    """Represent a file to which *output* is to be sent.

    Although it's possible to write a single molecule to a file by
    calling the write() method of a molecule, if multiple molecules
    are to be written to the same file you should use the Outputfile
    class.

    Required parameters:
       format - see the outformats variable for a list of available
                output formats
       filename

    Optional parameters:
       overwrite -- if the output file already exists, should it
                   be overwritten? (default is False)
       opt -- a dictionary of format-specific options
              For format options with no parameters, specify the
              value as None.

    Methods:
       write(molecule)
       close()
    """
    def __init__(self, format, filename, overwrite=False, opt=None):
        if opt == None:
            opt = {}
        self.format = format
        self.filename = filename
        if not overwrite and os.path.isfile(self.filename):
            raise IOError("%s already exists. Use 'overwrite=True' to overwrite it." % self.filename)

        self.obConversion = ob.OBConversion()
        formatok = self.obConversion.SetOutFormat(self.format)
        if not formatok:
            raise ValueError("%s is not a recognised Open Babel format" % format)

        for k, v in opt.items():
            if v == None:
                self.obConversion.AddOption(k, self.obConversion.OUTOPTIONS)
            else:
                self.obConversion.AddOption(k, self.obConversion.OUTOPTIONS, str(v))
        self.total = 0 # The total number of molecules written to the file

    def write(self, molecule):
        """Write a molecule to the output file.

        Required parameters:
           molecule
        """
        if not self.filename:
            raise IOError("Outputfile instance is closed.")

        if self.total==0:
            self.obConversion.WriteFile(molecule.OBMol, self.filename)
        else:
            self.obConversion.Write(molecule.OBMol)
        self.total += 1

    def close(self):
        """Close the Outputfile to further writing."""
        self.obConversion.CloseOutFile()
        self.filename = None

class Molecule(object):
    """Represent a Pybel Molecule.

    Required parameter:
       OBMol -- an Open Babel OBMol or any type of cinfony Molecule

    Attributes:
       atoms, charge, conformers, data, dim, energy, exactmass, formula,
       molwt, spin, sssr, title, unitcell.
    (refer to the Open Babel library documentation for more info).

    Methods:
       addh(), calcfp(), calcdesc(), draw(), localopt(), make3D(), removeh(),
       write()

    The underlying Open Babel molecule can be accessed using the attribute:
       OBMol
    """
    _cinfony = True

    def __init__(self, OBMol):

        if hasattr(OBMol, "_cinfony"):
            a, b = OBMol._exchange
            if a == 0:
                mol = readstring("smi", b)
            else:
                mol = readstring("mol", b)
            OBMol = mol.OBMol

        self.OBMol = OBMol

    @property
    def atoms(self):
        return [ Atom(self.OBMol.GetAtom(i+1)) for i in range(self.OBMol.NumAtoms()) ]
    @property
    def charge(self): return self.OBMol.GetTotalCharge()
    @property
    def conformers(self): return self.OBMol.GetConformers()
    @property
    def data(self): return MoleculeData(self.OBMol)
    @property
    def dim(self): return self.OBMol.GetDimension()
    @property
    def energy(self): return self.OBMol.GetEnergy()
    @property
    def exactmass(self): return self.OBMol.GetExactMass()
    @property
    def formula(self): return self.OBMol.GetFormula()
    @property
    def molwt(self): return self.OBMol.GetMolWt()
    @property
    def spin(self): return self.OBMol.GetTotalSpinMultiplicity()
    @property
    def sssr(self): return self.OBMol.GetSSSR()
    def _gettitle(self): return self.OBMol.GetTitle()
    def _settitle(self, val): self.OBMol.SetTitle(val)
    title = property(_gettitle, _settitle)
    @property
    def unitcell(self):
        unitcell_index = _obconsts.UnitCell
        if sys.platform[:3] == "cli":
            unitcell_index = System.UInt32(unitcell_index)
        unitcell = self.OBMol.GetData(unitcell_index)
        if unitcell:
            if sys.platform[:3] != "cli":
                return _obfuncs.toUnitCell(unitcell)
            else:
                return unitcell.Downcast[ob.OBUnitCell]()
        else:
            raise AttributeError("Molecule has no attribute 'unitcell'")
    @property
    def _exchange(self):
        if self.OBMol.HasNonZeroCoords():
            return (1, self.write("mol"))
        else:
            return (0, self.write("can").split()[0])

    def __iter__(self):
        """Iterate over the Atoms of the Molecule.

        This allows constructions such as the following:
           for atom in mymol:
               print atom
        """
        return iter(self.atoms)

    def calcdesc(self, descnames=[]):
        """Calculate descriptor values.

        Optional parameter:
           descnames -- a list of names of descriptors

        If descnames is not specified, all available descriptors are
        calculated. See the descs variable for a list of available
        descriptors.
        """
        if not descnames:
            descnames = descs
        ans = {}
        for descname in descnames:
            try:
                desc = _descdict[descname]
            except KeyError:
                raise ValueError("%s is not a recognised Open Babel descriptor type" % descname)
            ans[descname] = desc.Predict(self.OBMol)
        return ans

    def calcfp(self, fptype="FP2"):
        """Calculate a molecular fingerprint.

        Optional parameters:
           fptype -- the fingerprint type (default is "FP2"). See the
                     fps variable for a list of of available fingerprint
                     types.
        """
        if sys.platform[:3] == "cli":
            fp = ob.VectorUInt()
        else:
            fp = ob.vectorUnsignedInt()
        fptype = fptype.lower()
        try:
            fingerprinter = _fingerprinters[fptype]
        except KeyError:
            raise ValueError("%s is not a recognised Open Babel Fingerprint type" % fptype)
        fingerprinter.GetFingerprint(self.OBMol, fp)
        return Fingerprint(fp)

    def write(self, format="smi", filename=None, overwrite=False, opt=None):
        """Write the molecule to a file or return a string.

        Optional parameters:
           format -- see the informats variable for a list of available
                     output formats (default is "smi")
           filename -- default is None
           overwite -- if the output file already exists, should it
                       be overwritten? (default is False)
           opt -- a dictionary of format specific options
                  For format options with no parameters, specify the
                  value as None.

        If a filename is specified, the result is written to a file.
        Otherwise, a string is returned containing the result.

        To write multiple molecules to the same file you should use
        the Outputfile class.
        """
        if opt == None:
            opt = {}
        obconversion = ob.OBConversion()
        formatok = obconversion.SetOutFormat(format)
        if not formatok:
            raise ValueError("%s is not a recognised Open Babel format" % format)
        for k, v in opt.items():
            if v == None:
                obconversion.AddOption(k, obconversion.OUTOPTIONS)
            else:
                obconversion.AddOption(k, obconversion.OUTOPTIONS, str(v))

        if filename:
            if not overwrite and os.path.isfile(filename):
                raise IOError("%s already exists. Use 'overwrite=True' to overwrite it." % filename)
            obconversion.WriteFile(self.OBMol,filename)
            obconversion.CloseOutFile()
        else:
            return obconversion.WriteString(self.OBMol)

    def localopt(self, forcefield="mmff94", steps=500):
        """Locally optimize the coordinates.

        Optional parameters:
           forcefield -- default is "mmff94". See the forcefields variable
                         for a list of available forcefields.
           steps -- default is 500

        If the molecule does not have any coordinates, make3D() is
        called before the optimization. Note that the molecule needs
        to have explicit hydrogens. If not, call addh().
        """
        forcefield = forcefield.lower()
        if self.dim != 3:
            self.make3D(forcefield)
        ff = _forcefields[forcefield]
        success = ff.Setup(self.OBMol)
        if not success:
            return
        ff.SteepestDescent(steps)
        ff.GetCoordinates(self.OBMol)

##    def globalopt(self, forcefield="MMFF94", steps=1000):
##        if not (self.OBMol.Has2D() or self.OBMol.Has3D()):
##            self.make3D()
##        self.localopt(forcefield, 250)
##        ff = _forcefields[forcefield]
##        numrots = self.OBMol.NumRotors()
##        if numrots > 0:
##            ff.WeightedRotorSearch(numrots, int(math.log(numrots + 1) * steps))
##        ff.GetCoordinates(self.OBMol)

    def make3D(self, forcefield = "mmff94", steps = 50):
        """Generate 3D coordinates.

        Optional parameters:
           forcefield -- default is "mmff94". See the forcefields variable
                         for a list of available forcefields.
           steps -- default is 50

        Once coordinates are generated, hydrogens are added and a quick
        local optimization is carried out with 50 steps and the
        MMFF94 forcefield. Call localopt() if you want
        to improve the coordinates further.
        """
        forcefield = forcefield.lower()
        _builder.Build(self.OBMol)
        self.addh()
        self.localopt(forcefield, steps)

    def addh(self):
        """Add hydrogens."""
        self.OBMol.AddHydrogens()

    def removeh(self):
        """Remove hydrogens."""
        self.OBMol.DeleteHydrogens()

    def __str__(self):
        return self.write()

    def draw(self, show=True, filename=None, update=False, usecoords=False):
        """Create a 2D depiction of the molecule.

        Optional parameters:
          show -- display on screen (default is True)
          filename -- write to file (default is None)
          update -- update the coordinates of the atoms to those
                    determined by the structure diagram generator
                    (default is False)
          usecoords -- don't calculate 2D coordinates, just use
                       the current coordinates (default is False)

        Tkinter and Python Imaging Library are required for image display.
        """
        obconversion = ob.OBConversion()
        formatok = obconversion.SetOutFormat("_png2")
        if not formatok:
            errormessage = ("PNG depiction support not found. You should compile "
                            "Open Babel with support for Cairo. See installation "
                            "instructions for more information.")
            raise ImportError(errormessage)

        # Need to copy to avoid removing hydrogens from self
        workingmol = Molecule(ob.OBMol(self.OBMol))
        workingmol.removeh()

        if not usecoords:
            _operations['gen2D'].Do(workingmol.OBMol)
        if update == True:
            if workingmol.OBMol.NumAtoms() != self.OBMol.NumAtoms():
                errormessage = ("It is not possible to update the original molecule "
                                "with the calculated coordinates, as the original "
                                "molecule contains explicit hydrogens for which no "
                                "coordinates have been calculated.")
                raise RuntimeError(errormessage)
            else:
                for i in range(workingmol.OBMol.NumAtoms()):
                    self.OBMol.GetAtom(i + 1).SetVector(workingmol.OBMol.GetAtom(i + 1).GetVector())

        if filename:
            filedes = None
        else:
            if sys.platform[:3] == "cli" and show:
                errormessage = ("It is only possible to show the molecule if you "
                                "provide a filename. The reason for this is that I kept "
                                "having problems when using temporary files.")
                raise RuntimeError(errormessage)
            
            filedes, filename = tempfile.mkstemp()

        workingmol.write("_png2", filename=filename, overwrite=True)

        if show:
            if sys.platform[:4] == "java":
                image = javax.imageio.ImageIO.read(java.io.File(filename))
                frame = javax.swing.JFrame(visible=1)
                frame.getContentPane().add(javax.swing.JLabel(javax.swing.ImageIcon(image)))
                frame.setSize(300,300)
                frame.setDefaultCloseOperation(javax.swing.WindowConstants.DISPOSE_ON_CLOSE)
                frame.show()
            elif sys.platform[:3] == "cli":
                form = _MyForm()
                form.setup(filename, self.title)
                Application.Run(form)                
            else:
                if not tk:
                    errormessage = ("Tkinter or Python Imaging "
                                    "Library not found, but is required for image "
                                    "display. See installation instructions for "
                                    "more information.")
                    raise ImportError(errormessage)
                root = tk.Tk()
                root.title((hasattr(self, "title") and self.title)
                           or self.__str__().rstrip())
                frame = tk.Frame(root, colormap="new", visual='truecolor').pack()
                image = PIL.open(filename)
                imagedata = piltk.PhotoImage(image)
                label = tk.Label(frame, image=imagedata).pack()
                quitbutton = tk.Button(root, text="Close", command=root.destroy).pack(fill=tk.X)
                root.mainloop()
        if filedes:
            os.close(filedes)
            os.remove(filename)

class Atom(object):
    """Represent a Pybel atom.

    Required parameter:
       OBAtom -- an Open Babel OBAtom

    Attributes:
       atomicmass, atomicnum, cidx, coords, coordidx, exactmass,
       formalcharge, heavyvalence, heterovalence, hyb, idx,
       implicitvalence, isotope, partialcharge, spin, type,
       valence, vector.

    (refer to the Open Babel library documentation for more info).

    The original Open Babel atom can be accessed using the attribute:
       OBAtom
    """

    def __init__(self, OBAtom):
        self.OBAtom = OBAtom

    @property
    def coords(self):
        return (self.OBAtom.GetX(), self.OBAtom.GetY(), self.OBAtom.GetZ())
    @property
    def atomicmass(self): return self.OBAtom.GetAtomicMass()
    @property
    def atomicnum(self): return self.OBAtom.GetAtomicNum()
    @property
    def cidx(self): return self.OBAtom.GetCIdx()
    @property
    def coordidx(self): return self.OBAtom.GetCoordinateIdx()
    @property
    def exactmass(self): return self.OBAtom.GetExactMass()
    @property
    def formalcharge(self): return self.OBAtom.GetFormalCharge()
    @property
    def heavyvalence(self): return self.OBAtom.GetHvyValence()
    @property
    def heterovalence(self): return self.OBAtom.GetHeteroValence()
    @property
    def hyb(self): return self.OBAtom.GetHyb()
    @property
    def idx(self): return self.OBAtom.GetIdx()
    @property
    def implicitvalence(self): return self.OBAtom.GetImplicitValence()
    @property
    def isotope(self): return self.OBAtom.GetIsotope()
    @property
    def partialcharge(self): return self.OBAtom.GetPartialCharge()
    @property
    def spin(self): return self.OBAtom.GetSpinMultiplicity()
    @property
    def type(self): return self.OBAtom.GetType()
    @property
    def valence(self): return self.OBAtom.GetValence()
    @property
    def vector(self): return self.OBAtom.GetVector()

    def __str__(self):
        c = self.coords
        return "Atom: %d (%.2f %.2f %.2f)" % (self.atomicnum, c[0], c[1], c[2])

def _findbits(fp, bitsperint):
    """Find which bits are set in a list/vector.

    This function is used by the Fingerprint class.

    >>> _findbits([13, 71], 8)
    [1, 3, 4, 9, 10, 11, 15]
    """
    ans = []
    start = 1
    if sys.platform[:4] == "java":
        fp = [fp.get(i) for i in range(fp.size())]
    for x in fp:
        i = start
        while x > 0:
            if x % 2:
                ans.append(i)
            x >>= 1
            i += 1
        start += bitsperint
    return ans

class Fingerprint(object):
    """A Molecular Fingerprint.

    Required parameters:
       fingerprint -- a vector calculated by OBFingerprint.FindFingerprint()

    Attributes:
       fp -- the underlying fingerprint object
       bits -- a list of bits set in the Fingerprint

    Methods:
       The "|" operator can be used to calculate the Tanimoto coeff. For example,
       given two Fingerprints 'a', and 'b', the Tanimoto coefficient is given by:
          tanimoto = a | b
    """
    def __init__(self, fingerprint):
        self.fp = fingerprint
    def __or__(self, other):
        return ob.OBFingerprint.Tanimoto(self.fp, other.fp)
    @property
    def bits(self):
        return _findbits(self.fp, ob.OBFingerprint.Getbitsperint())
    def __str__(self):
        fp = self.fp
        if sys.platform[:4] == "java":
            fp = [self.fp.get(i) for i in range(self.fp.size())]
        return ", ".join([str(x) for x in fp])

class Smarts(object):
    """A Smarts Pattern Matcher

    Required parameters:
       smartspattern

    Methods:
       findall(molecule)

    Example:
    >>> mol = readstring("smi","CCN(CC)CC") # triethylamine
    >>> smarts = Smarts("[#6][#6]") # Matches an ethyl group
    >>> print smarts.findall(mol)
    [(1, 2), (4, 5), (6, 7)]

    The numbers returned are the indices (starting from 1) of the atoms
    that match the SMARTS pattern. In this case, there are three matches
    for each of the three ethyl groups in the molecule.
    """
    def __init__(self,smartspattern):
        """Initialise with a SMARTS pattern."""
        self.obsmarts = ob.OBSmartsPattern()
        success = self.obsmarts.Init(smartspattern)
        if not success:
            raise IOError("Invalid SMARTS pattern")
    def findall(self,molecule):
        """Find all matches of the SMARTS pattern to a particular molecule.

        Required parameters:
           molecule
        """
        self.obsmarts.Match(molecule.OBMol)
        vector = self.obsmarts.GetUMapList()
        if sys.platform[:4] == "java":
            vector = [vector.get(i) for i in range(vector.size())]
        return list(vector)

class MoleculeData(object):
    """Store molecule data in a dictionary-type object

    Required parameters:
      obmol -- an Open Babel OBMol

    Methods and accessor methods are like those of a dictionary except
    that the data is retrieved on-the-fly from the underlying OBMol.

    Example:
    >>> mol = readfile("sdf", 'head.sdf').next() # Python 2
    >>> # mol = next(readfile("sdf", 'head.sdf')) # Python 3
    >>> data = mol.data
    >>> print data
    {'Comment': 'CORINA 2.61 0041  25.10.2001', 'NSC': '1'}
    >>> print len(data), data.keys(), data.has_key("NSC")
    2 ['Comment', 'NSC'] True
    >>> print data['Comment']
    CORINA 2.61 0041  25.10.2001
    >>> data['Comment'] = 'This is a new comment'
    >>> for k,v in data.items():
    ...    print k, "-->", v
    Comment --> This is a new comment
    NSC --> 1
    >>> del data['NSC']
    >>> print len(data), data.keys(), data.has_key("NSC")
    1 ['Comment'] False
    """
    def __init__(self, obmol):
        self._mol = obmol
    def _data(self):
        data = self._mol.GetData()
        if sys.platform[:4] == "java":
            data = [data.get(i) for i in range(data.size())]
        answer = [x for x in data if
                   x.GetDataType()==_obconsts.PairData or
                   x.GetDataType()==_obconsts.CommentData]
        if sys.platform[:3] != "cli":
            answer = [_obfuncs.toPairData(x) for x in answer]
        return answer
    def _testforkey(self, key):
        if not key in self:
            raise KeyError("'%s'" % key)
    def keys(self):
        return [x.GetAttribute() for x in self._data()]
    def values(self):
        return [x.GetValue() for x in self._data()]
    def items(self):
        return iter(zip(self.keys(), self.values()))
    def __iter__(self):
        return iter(self.keys())
    def iteritems(self): # Can remove for Python 3
        return self.items()
    def __len__(self):
        return len(self._data())
    def __contains__(self, key):
        return self._mol.HasData(key)
    def __delitem__(self, key):
        self._testforkey(key)
        self._mol.DeleteData(self._mol.GetData(key))
    def clear(self):
        for key in self:
            del self[key]
    def has_key(self, key):
        return key in self
    def update(self, dictionary):
        for k, v in dictionary.items():
            self[k] = v
    def __getitem__(self, key):
        self._testforkey(key)
        answer = self._mol.GetData(key)
        if sys.platform[:3] != "cli":
            answer = _obfuncs.toPairData(answer)
        return answer.GetValue()
    def __setitem__(self, key, value):
        if key in self:
            if sys.platform[:3] != "cli":
                pairdata = _obfuncs.toPairData(self._mol.GetData(key))
            else:
                pairdata = self._mol.GetData(key).Downcast[ob.OBPairData]()
            pairdata.SetValue(str(value))
        else:
            pairdata = ob.OBPairData()
            pairdata.SetAttribute(key)
            pairdata.SetValue(str(value))
            self._mol.CloneData(pairdata)
    def __repr__(self):
        return dict(self.items()).__repr__()

if sys.platform[:3] == "cli":
    class _MyForm(Form):
        def __init__(self):
            Form.__init__(self)

        def setup(self, filename, title):
            # adjust the form's client area size to the picture
            self.ClientSize = Size(300, 300)
            self.Text = title
             
            self.filename = filename
            self.image = Image.FromFile(self.filename)
            pictureBox = PictureBox()
            # this will fit the image to the form
            pictureBox.SizeMode = PictureBoxSizeMode.StretchImage
            pictureBox.Image = self.image
            # fit the picture box to the frame
            pictureBox.Dock = DockStyle.Fill
             
            self.Controls.Add(pictureBox)
            self.Show()

if __name__=="__main__": #pragma: no cover
    import doctest
    doctest.testmod(verbose=True)
~~~

## Reference

1. [Pybel API](http://open-babel.readthedocs.org/en/latest/UseTheLibrary/Python_PybelAPI.html)
2. [Pybel](http://open-babel.readthedocs.org/en/latest/UseTheLibrary/Python_Pybel.html)
3. [Pybel: a Python wrapper for the OpenBabel cheminformatics toolkit](http://journal.chemistrycentral.com/content/2/1/5)
4. [OpenBabel Documentation](http://open-babel.readthedocs.org/en/latest/index.html)
5. [OpenBabel-Python](http://open-babel.readthedocs.org/en/latest/UseTheLibrary/Python.html)

------
