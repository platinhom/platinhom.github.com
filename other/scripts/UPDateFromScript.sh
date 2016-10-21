#! /bin/bash
# file: UPDateFromScript.sh
# Author: Platinhom, 2015.6.25

# A script to update the code block in the blog files.
# The code block should be between ~~~ ..... ~~~ 
# and has a line before the block: ###### FILE: sourcecode_file  

# Example:
# ###### FILE: UPDateFromScript.sh
# 
# ~~~ bash
# codes
# ~~~
# Also support the filename as link in markdown:
# ###### FILE: [UPDateFromScript.sh](link)

# You may change the two directories, saving the source code files and blog files.
sd="/Users/Hom/MyGit/Homepage/platinhom.github.com/other/scripts"
pd="/Users/Hom/MyGit/Homepage/platinhom.github.com/_posts"

# Check the existence of UPDateFromScript.py
if [ ! -f "${sd}/UPDateFromScript.py" ];then
	echo "UPDateFromScript.py is not in the scripts directory!";
	exit 1;
fi

# Check the existence of two directories
if [ ! \( \( -d "${sd}" \) -a \( -d "${pd}" \) \) ];then
	echo "Please assign the scripts and _post directory!";
	exit 1;
fi

# Start the script in the script directory.
cd $sd

### linkfile save the relation between source code file and blog files.
: > linkfile #clear the file
### Update the working time
date >> UPDateFromScript.log

### File the relationship between source code files and blog files.
### Only process the file with extension start at [bspcfrjv] here.
### bat/sh/csh/f90/py/pl/rb/vbs/js
for fii in *.[spcfrj]*
do
	###  !!!!!! sourcecode_file
	echo "!!!!!! $fii">>linkfile
	### Blog with md/html extension.
	grep "^###### FILE:" ${pd}/*.[mh]*[dl] | grep "$fii" | awk -F \: '{print $1}' >>linkfile
done

# IFS is seperate symbol.
# Avoid the blank to seperate file name, 
# Here we change it temply.
OLDIFS=$IFS
IFS=$'\n'

sourcefile=""
blogfile=""
for line in `cat linkfile`
do
	if [ ${line:0:6} = "!!!!!!" ];then
		sourcefile=${line:7};
	else
		blogfile=$line;
		# Run the program by UPDateFromScript.py !
		newfile=`python UPDateFromScript.py "$sourcefile" "$blogfile" | grep "!!! New file"`;

		if [ -z "${newfile}" ];then
			echo "$sourcefile and $blogfile with the same codes"!
		else
			# Notice the string return...
			sysOS=`uname -s`
			if [ $sysOS == "Darwin" -o $sysOS == "Linux" ];then
				newfile=${newfile:17};
			else
			# file string is different when python return in Window.
				newfile="${blogfile}-tmp.md"
			fi
			
			# Log the result difference
			echo $newfile $blogfile | tee -a UPDateFromScript.log;
			diff $newfile $blogfile | tee -a UPDateFromScript.log;
			# Replace the old file
			echo "Compare done! Stop 5s. If you need, Ctrl+C to cancel replacement!"
			sleep 5
			mv $newfile $blogfile
		fi
	fi
done

# Correct the IFS
IFS=$OLDIFS

# Come back to the last directory.
cd - > /dev/null
