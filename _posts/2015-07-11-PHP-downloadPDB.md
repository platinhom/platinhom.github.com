---
layout: post
title: 用PHP下载PDB并指定链ID
date: 2015-07-10 17:18:42
categories: CompCB
tags: PHP CompBiol
---

提供给服务器使用的在线下载PDB并可以选择指定链的函数.也可以处理本地PDB文件提取指定链.
支持 A-D 去下载ABCD链, 也支持-D, H-来下载一大段. 也支持使用*,all,-或者不输入(或空格)来提取所有链.

###  file\_get\_contents
该函数能够获取远程文件(网页)或本地文件的所有内容, 返回字符串.

### strstr(str,匹配串)
查找字符串,并返回找到第一个位置(包括该匹配部分)开始到最后的字串.比起strpos可能返回0而判断为假(找不到),该函数作为判断是否找到更为好用.

### ord和chr
将整形和ascii型互变.大写字母65-90, 小写字母97-122. 大写变小写是+32. 这里用来判断范围,例如A-F可以转为65-70然后$i++.

### PDB标识
提取原子使用前六字符 `ATOM  `或`HETATM`,如果之前找到对应的链,下一行找到`TER   `,那么也把该行输出.

~~~php
<?php
// File: GetPDBChain.php
// Author: Platinhom, 2015.7.10
// This function can download PDB with 4-digit ID and even only the given chains.
// It can also use to extract the given chains on local PDB file.
// Use as: 
// require_once('GetPDBChain.php');
// getchainsbyID('A-DE','http://www.rcsb.org/pdb/files/2QW7.pdb','2QW7.pdb');
// 1st argument is chain ID expression, support *,all,- or blank to download intact file
// 2nd argument is the file to be deal with. Need the intact address
// 3rd argument is the output file

function getchainsbyID($chainstr,$s,$sout){
  if(!$s) return false;
  if(!$sout) return false;
  $chainstr=strtoupper(trim($chainstr));
  //$s=strtoupper(trim($s));//This will upper address, don't use.
  $writeall=false;
  if ($chainstr=="*" or $chainstr=="ALL" or $chainstr=="" or $chainstr=="-"){
    $writeall=true;
  }
  elseif(strstr($chainstr, "-")){
    $newstr="";
    $lenc=strlen($chainstr);
    for ($i=0;$i<$lenc;$i++){
      $l=$chainstr[$i];
      if ($l!='-'){
        $newstr.=$l;
      }
      else{
        //"-?"
        if ($i==0){
          $lp=$chainstr[$i+1];
          $olp=ord($lp);
          if ($olp>=65 && $olp<=90){
            for($j=65;$j<=$olp;$j++){
              $newstr.=chr($j);
            }
          }
        }
        //"...-"
        elseif ($i== ($lenc-1)) {
          $lp=$chainstr[$i-1];
          $olp=ord($lp);
          if ($olp>=65 && $olp<=90){
            for($j=$olp;$j<=90;$j++){
              $newstr.=chr($j);
            }
          }
        }
        else{
          $olp=ord($chainstr[$i+1]);$olm=ord($chainstr[$i-1]);
          if ($olp>$olm && $olp<=90 && $olm>=65){
            for($j=$olm;$j<=$olp;$j++){
              $newstr.=chr($j);
            }
          }
        }
      }
    }
    $chainstr=$newstr;
  }

  if(!strstr($s, "\n")) {
    $pdb = file_get_contents("$s");
  }
  if($pdb){
    $fh=fopen($sout,'w');
    if ($writeall){
      fwrite($fh,$pdb);
    }
    else{
      if(!is_array($pdb))
        $pdb = explode("\n", $pdb);
      $findpos=false;
      foreach($pdb as $line) {
        $line = trim($line);
        $start06=substr($line, 0, 6);
        if( $start06 == 'ATOM  ' || $start06=='HETATM') {
            $chain = substr($line, 21, 1);
            $findpos=stristr($chainstr,$chain);
            if ($findpos){
              fwrite($fh, $line."\n");
            }
        }
        //chain ter;
        elseif ($findpos && $start06=="TER   ") {
             fwrite($fh, $line."\n");
             $findpos=false;
        }
      }
    }
    fclose($fh);
    return true;
  }
  return false;
}
//Test on local file or online file
//getchainsbyID("A-DE",'pdb2qw7.pdb','2qw72.pdb');
//getchainsbyID("*",'http://www.rcsb.org/pdb/files/2QW7.pdb','2qw72.pdb');
?>
~~~

------
