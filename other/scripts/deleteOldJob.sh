#! /bin/bash
# Author: Zhixiong Zhao, 2015.7.10
#
# Monitor the job number and generated old directories.
# Use as : nohup ./deleteOldJob.sh &
 
cd /home/labsite/MIBPBweb/MIBPBRun
 
while true
do
 
#jobnum=`ps -ef | grep "sh -c ./mibpb" |wc -l;`
 
nowtime=`date +%s`
dirnum=`ls mibpb* | wc -l`
 
if [ $dirnum -gt 0 ];then
for dir in mibpb*
do
filetime=`stat -c %Y $dir`
delta=`expr $nowtime - $filetime`
#7day=604800second
echo $filetime $delta
if [ $delta -gt 604800 ];then
rm -rf $dir
#mv $dir ..
echo "$dir :time $delta seconds." 
fi
done
fi
 
sleep 3600
done #while
 
cd -
