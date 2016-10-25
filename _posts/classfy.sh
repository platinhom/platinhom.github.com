#! /bin/bash
## To classfy blog based on category


mv */*/*.md .

##mv */*.md .
##mv */*/*/*.md .
##mv */*/*/*/*.md .

for d in `ls -d */*/`
do
rmdir $d
done

sleep 5

for f in *.md
do
	cata=`head -n 7 $f | grep categories | awk '{print $2}'`
	tag=`head -n 7 $f | grep tags | awk '{print $2}'`

	if [ $cata == Summary ]; then
		[ -d $cata ] || mkdir -p $cata
		mv $f $cata		
	else
		[ -d $cata/$tag ] || mkdir -p $cata/$tag
		mv $f $cata/$tag
	fi

done
