#! /bin/bash
# file: gitsubmit.sh

comment=$1
if [ -z $commend ];then
comment=regular
fi

cd ..
git add -A
git commit -am "$comment"
if [ ! -z $2 ];then
	#git remote add gitcafe git@gitcafe.com:platinhom/platinhom.git 
	git push gitcafe master:gitcafe-pages
fi
# may be change to your branch here
git push origin master
cd -
