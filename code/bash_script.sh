#!/bin/bash
var1="$1"
if [ $var1 = daynumber ]
then
	out=$( date +%j )
	echo 'Today is day '$out
	if [ $out -eq 069 ]
	then
		echo 'nice'
	fi
fi
if [ $var1 = weekday ]
then
	out=$( date +%A )
	echo 'Today is '$out
fi
if [ $var1 = christmas ]
then
	today=$( date +%j )
	if [ ${today:0:-2} = 0 ] #removes 0 digit for days <100 which causes the subtraction result to be off by 10.
	then
		today=${today:1}
	fi
	let "out = 360 - $today"
	echo 'There are' $out 'days until Christmas.'
fi

case $var1 in
	daynumber)
		;;
	weekday)
		;;
	christmas)
		;;
	*)
		echo 'invaliad argument'
		echo 'Valid arguements: daynumber, weekday, christmas'
		;;
esac
