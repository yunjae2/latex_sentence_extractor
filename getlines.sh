#!/bin/bash

if [ "$#" -ne 3 ]
then
	echo "usage: $0 <text file> <start line> <end line>"
	exit
fi

textfile=$1
startline=$2
endline=$3

cat $textfile | head -n $endline | tail -n +$startline > .temp.txt

CALLEE_DIR=`dirname $0`
$CALLEE_DIR/extract.py < .temp.txt

rm .temp.txt
