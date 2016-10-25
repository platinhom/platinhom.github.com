---
layout: post
title: ubuntu16 安装matlab问题
date: 2016-08-20 19:23:25
categories: MathStat
tags: Matlab Ubuntu
---

今天好不容易下载好MATLAB2016a安装完后启动报错：

![](http://www.linuxdiyf.com/linux/uploads/allimg/160707/2-160FG00G0U0.png)

~~~
------------------------------------------------------------------------
       Segmentation violation detected at Sun Aug 21 02:11:29 2016
------------------------------------------------------------------------

Configuration:
  Crash Decoding      : Disabled
  Crash Mode          : continue (default)
  Current Graphics Driver: Unknown hardware
  Current Visual      : 0x21 (class 4, depth 24)
  Default Encoding    : UTF-8
  GNU C Library       : 2.23 stable
  Host Name           : hom-home
  MATLAB Architecture : glnxa64
  MATLAB Root         : /home/hom/Softwares/MATLAB/R2016a
  MATLAB Version      : 9.0.0.341360 (R2016a)
  OpenGL              : hardware
  Operating System    : Linux 4.4.0-21-generic #37-Ubuntu SMP Mon Apr 18 18:33:37 UTC 2016 x86_64
  Processor ID        : x86 Family 6 Model 58 Stepping 9, GenuineIntel
  Virtual Machine     : Java 1.7.0_60-b19 with Oracle Corporation Java HotSpot(TM) 64-Bit Server VM mixed mode
  Window System       : The X.Org Foundation (11803000), display :0

Fault Count: 1


Abnormal termination:
Segmentation violation

Register State (from fault):
  RAX = 0000000000000000  RBX = 00007f5e16b950e8
  RCX = 00007f5e6c2214e0  RDX = 0000000000000006
  RSP = 00007f5efcc57de0  RBP = 00007f5efcc57f00
  RSI = 0000000000000000  RDI = 00007f5e16b6b8a8

   R8 = 0000000000000030   R9 = 0000000000000004
  R10 = 00007f5e16eebef0  R11 = 00007f5e16b68000
  R12 = 00007f5e74525ba0  R13 = 0000006900000006
  R14 = 0000000000000006  R15 = 00007f5e16b6c280

  RIP = 00007f5f176f756c  EFL = 0000000000010206

   CS = 0033   FS = 0000   GS = 0000

Stack Trace (from fault):
[  0] 0x00007f5f176f756c                        /lib64/ld-linux-x86-64.so.2+00050540
[  1] 0x00007f5f17700681                        /lib64/ld-linux-x86-64.so.2+00087681
[  2] 0x00007f5f176fb394                        /lib64/ld-linux-x86-64.so.2+00066452
[  3] 0x00007f5f176ffbd9                        /lib64/ld-linux-x86-64.so.2+00084953
[  4] 0x00007f5f14e4af09                   /lib/x86_64-linux-gnu/libdl.so.2+00003849
[  5] 0x00007f5f176fb394                        /lib64/ld-linux-x86-64.so.2+00066452
[  6] 0x00007f5f14e4b571                   /lib/x86_64-linux-gnu/libdl.so.2+00005489
[  7] 0x00007f5f14e4afa1                   /lib/x86_64-linux-gnu/libdl.so.2+00004001 dlopen+00000049
[  8] 0x00007f5f116960b6 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libut.so+00315574
[  9] 0x00007f5f11696c76 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libut.so+00318582 _Z11utGetModuleRKSbIDsSt11char_traitsIDsESaIDsEEPi+00000022
[ 10] 0x00007f5f11696d6b /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libut.so+00318827 utGetModule+00000171
[ 11] 0x00007f5f06fbbd45 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_dispatcher.so+00482629
[ 12] 0x00007f5f06faeeaf /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_dispatcher.so+00429743 _ZN13Mlm_MATLAB_fn8try_loadEv+00000031
[ 13] 0x00007f5f06fa5e95 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_dispatcher.so+00392853 _ZN13Mlm_MATLAB_fn4loadEv+00000037
[ 14] 0x00007f5f06fa35e9 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_dispatcher.so+00382441 _ZN13Mfh_MATLAB_fn11dispatch_fhEiPP11mxArray_tagiS2_+00000057
[ 15] 0x00007f5f03fe81c9 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+09232841
[ 16] 0x00007f5f04114dbf /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+10464703
[ 17] 0x00007f5f0410aa5a /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+10422874
[ 18] 0x00007f5f040d3911 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+10197265
[ 19] 0x00007f5f03ba1b2a /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+04750122
[ 20] 0x00007f5f03ba2a4c /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+04753996
[ 21] 0x00007f5f03ba0ebc /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+04746940
[ 22] 0x00007f5f03b9e9ea /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+04737514
[ 23] 0x00007f5f03b9edb1 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+04738481
[ 24] 0x00007f5f03ba0a63 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+04745827
[ 25] 0x00007f5f03ba0be9 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+04746217
[ 26] 0x00007f5f03c5116f /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+05468527
[ 27] 0x00007f5f03c5422a /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+05481002
[ 28] 0x00007f5f03ef6543 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+08242499
[ 29] 0x00007f5f03fd8e5c /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+09170524
[ 30] 0x00007f5f06ffc27e /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_dispatcher.so+00746110 _ZN8Mfh_file16dispatch_fh_implEMS_FviPP11mxArray_tagiS2_EiS2_iS2_+00000862
[ 31] 0x00007f5f06ffc9a0 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_dispatcher.so+00747936 _ZN8Mfh_file11dispatch_fhEiPP11mxArray_tagiS2_+00000032
[ 32] 0x00007f5f03fe81c9 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+09232841
[ 33] 0x00007f5f04114dbf /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+10464703
[ 34] 0x00007f5f0410aa5a /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+10422874
[ 35] 0x00007f5f040d3911 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+10197265
[ 36] 0x00007f5f03ba1b2a /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+04750122
[ 37] 0x00007f5f03ba2a4c /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+04753996
[ 38] 0x00007f5f03ba0ebc /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+04746940
[ 39] 0x00007f5f03b9e9ea /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+04737514
[ 40] 0x00007f5f03b9edb1 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+04738481
[ 41] 0x00007f5f03ba0a63 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+04745827
[ 42] 0x00007f5f03ba0be9 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+04746217
[ 43] 0x00007f5f03c5116f /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+05468527
[ 44] 0x00007f5f03c5422a /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+05481002
[ 45] 0x00007f5f03ef6543 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+08242499
[ 46] 0x00007f5f03ebf07e /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+08015998
[ 47] 0x00007f5f03ec3058 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+08032344
[ 48] 0x00007f5f03ec3107 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+08032519
[ 49] 0x00007f5f03f392c5 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+08516293
[ 50] 0x00007f5f03f39792 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwm_lxe.so+08517522
[ 51] 0x00007f5f072fc769 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwmcr.so+00788329
[ 52] 0x00007f5f0731c474 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwmcr.so+00918644 _Z32mnRunPathDependentInitializationv+00000036
[ 53] 0x00007f5f072fe5a3 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwmcr.so+00796067 _ZN11mcrInstance26init_on_interpreter_threadEP11MfileReaderP13MexFileReader+00000483
[ 54] 0x00007f5f10a6ed6c /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwmlutil.so+04328812 _ZNK5boost9function0IbEclEv+00000028
[ 55] 0x00007f5f073078e5 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwmcr.so+00833765
[ 56] 0x00007f5f0730dd09 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwmcr.so+00859401 _ZN5boost6detail17task_shared_stateINS_3_bi6bind_tIbPFbRKNS_8functionIFbvEEEENS2_5list1INS2_5valueIS6_EEEEEEbE6do_runEv+00000025
[ 57] 0x00007f5f0730e43b /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwmcr.so+00861243 _ZN5boost6detail22task_base_shared_stateIbE3runEv+00000059                                                                                                                                  
[ 58] 0x00007f5f0730e497 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwmcr.so+00861335
[ 59] 0x00007f5f072e575a /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwmcr.so+00694106
[ 60] 0x00007f5f07658c06 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwiqm.so+00969734
[ 61] 0x00007f5f07646b4c /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwiqm.so+00895820 _ZN5boost6detail8function21function_obj_invoker0ISt8functionIFNS_3anyEvEES4_E6invokeERNS1_15function_bufferE+00000028
[ 62] 0x00007f5f0764721f /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwiqm.so+00897567 _ZNK5boost9function0INS_3anyEEclEv+00000031
[ 63] 0x00007f5f07646993 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwiqm.so+00895379 _ZN3iqm18PackagedTaskPlugin7executeEP15inWorkSpace_tagRN5boost10shared_ptrIN14cmddistributor17IIPCompletedEventEEE+00000163
[ 64] 0x00007f5f072fa71d /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwmcr.so+00780061
[ 65] 0x00007f5f07628f98 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwiqm.so+00774040
[ 66] 0x00007f5f076135af /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwiqm.so+00685487
[ 67] 0x00007f5f076107e3 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwiqm.so+00673763
[ 68] 0x00007f5f16a4aa3a /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwservices.so+03443258
[ 69] 0x00007f5f16a498a7 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwservices.so+03438759
[ 70] 0x00007f5f16a4a10c /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwservices.so+03440908 _Z25svWS_ProcessPendingEventsiib+00000092
[ 71] 0x00007f5f072e5ed2 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwmcr.so+00696018
[ 72] 0x00007f5f072e6211 /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwmcr.so+00696849
[ 73] 0x00007f5f072d2cfd /home/hom/Softwares/MATLAB/R2016a/bin/glnxa64/libmwmcr.so+00617725
[ 74] 0x00007f5f156206fa              /lib/x86_64-linux-gnu/libpthread.so.0+00030458
[ 75] 0x00007f5f15356b5d                    /lib/x86_64-linux-gnu/libc.so.6+01076061 clone+00000109
[ 76] 0x0000000000000000                                   <unknown-module>+00000000


If this problem is reproducible, please submit a Service Request via:
    http://www.mathworks.com/support/contact_us/

A technical support engineer might contact you with further information.

Thank you for your help.                                                
~~~

注意到最后一句是libc.so出的问题，经查有这么个帖子解决：[matlab2015b在ubuntu16.04中启动崩溃的问题](http://www.linuxdiyf.com/linux/22140.html),可以参看[官方方法](https://www.mathworks.com/support/bugreports/1297894), 简而言之就是MATLAB自带libc版本和ubuntu的冲突,在ubuntu15以后就会有这个问题.解决方法就是在`$MATLABINSTALLDIR/sys/os/glnxa64/libstdc++.so.6`重命名为`libstdc++.so.6.old`,使其采用自带系统的libc库.

上述执行以后,终于能弹出matlab界面, 但很快又死了,在用户目录下出现matlab的crash文件内容:

~~~
------------------------------------------------------------------------
       Segmentation violation detected at Sun Aug 21 02:16:51 2016
------------------------------------------------------------------------

Configuration:
  Crash Decoding      : Disabled
  Crash Mode          : continue (default)
  Current Graphics Driver: Unknown hardware
  Current Visual      : 0x21 (class 4, depth 24)
  Default Encoding    : UTF-8
  GNU C Library       : 2.23 stable
  Host Name           : hom-home
  MATLAB Architecture : glnxa64
  MATLAB Root         : /home/hom/Softwares/MATLAB/R2016a
  MATLAB Version      : 9.0.0.341360 (R2016a)
  OpenGL              : hardware
  Operating System    : Linux 4.4.0-21-generic #37-Ubuntu SMP Mon Apr 18 18:33:37 UTC 2016 x86_64
  Processor ID        : x86 Family 6 Model 58 Stepping 9, GenuineIntel
  Virtual Machine     : Java 1.7.0_60-b19 with Oracle Corporation Java HotSpot(TM) 64-Bit Server VM mixed mode
  Window System       : The X.Org Foundation (11803000), display :0

Fault Count: 1


Abnormal termination:
Segmentation violation

Register State (from fault):
  RAX = 00007fcab6b0fe40  RBX = 0000000000000000
  RCX = 0000000000000001  RDX = 00007fcab6b0fec0
  RSP = 00007fcab6b0fe10  RBP = 00007fca540a5910
  RSI = 0000000000000000  RDI = 00007fcab6b0fe40

   R8 = 0000000000000000   R9 = 0000000000000001
  R10 = 00007fca54128d10  R11 = 0000000000000000
  R12 = 00007fca5437cb00  R13 = 00007fca540a5910
  R14 = 00007fca5443c150  R15 = 00007fca543787b0

  RIP = 00007fc9b93a624d  EFL = 0000000000010246

   CS = 0033   FS = 0000   GS = 0000

Stack Trace (from fault):
[  0] 0x00007fc9b93a624d             /usr/lib/nvidia-361/libGLX_nvidia.so.0+00344653


If this problem is reproducible, please submit a Service Request via:
    http://www.mathworks.com/support/contact_us/

A technical support engineer might contact you with further information.

Thank you for your help.                                                
~~~

这个问题是NVIDIA显卡和新版MATLAB冲突所导致的....据说NVIDIA的[367.18-1驱动](http://www.nvidia.com/download/driverResults.aspx/102879/en-us)解决了这个问题, 但Ubuntu安装法的NVIDIA显卡是361版..我又懒得折腾显卡了...

参见这个官方论坛解答[Matlab crash graphics driver issue](https://cn.mathworks.com/matlabcentral/answers/286306-matlab-crash-graphics-driver-issue), 就是可以启动时使用`matlab -softwareopengl` 来强制使用软件opengl加速(会影响表现). 另外也可以在打开matlab后使用`opengl('save','software')`来保存打开软件加速方法(逆转就是`opengl('save','hardware')`)

这个帖子有教使用367的驱动来解决问题: [How to Run Matlab 2016a with Nvidia Drivers of GTX-960 in Ubuntu 16.04?](http://askubuntu.com/questions/765455/how-to-run-matlab-2016a-with-nvidia-drivers-of-gtx-960-in-ubuntu-16-04/767231)

~~~bash
sudo apt purge nvidia*
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update
sudo apt install nvidia-367
~~~

### 附录:安装需要的

~~~bash
sudo mount -o loop matlab.iso /mnt/matlab
cd /mnt/matlab
./INSTALL
### Installation will need a FIK (install key), copy files to $MATLAB_INSTALL_DIR/bin/glnxa64/ ,after run it, will need a license.
# Install matlab to software center and control user to use and also solve the libc problem
sudo apt-get install matlab-support 
## change access of ~/.matlab to your user!
sudo chown username -R ~/.matlab
# may need no graphic interface, add following to .bashrc
alias matlabno="matlab -nodesktop -nosplash"
# May need update to nvidia-367 as before
~~~

## Reference

1. [Ubuntu official documentation: MATLAB](https://help.ubuntu.com/community/MATLAB)

------
