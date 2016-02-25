#!/bin/bash

#Francis Paran
#file_tree

function argv() {
    if [ $1 -gt 0 ]; then
	    return 0
    else
	    return 1
    fi
}

show_hidden="0"
recurse="0"
line_by_line="0"

while getopts :hlr OPTION ; do
	case $OPTION in
		h) # -h show hidden files
		    show_hidden="1" ;;
		l) # -l line by line
		    line_by_line="1" ;;
		r) # -r recursive
		    recurse="1" ;;
	       \?)
		    echo "Options: [-h (show hidden)], [-l (line by line)], [-r (recursive)] [<directory>||.]" 
		    exit 2 ;;
    	esac
done

shift $(($OPTIND-1))

if argv $#; then
	directory=${1}
else
	directory=`pwd`
fi	

python `which file_tree`.py "$directory" $show_hidden $recurse $line_by_line

