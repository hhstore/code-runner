#!/usr/bin/env bash
kill_time=$1
sh_file=$2
code_file=$3

###################################################
# msg:
SEP="=1=2=3=4=5=== I Am A Dividing Line ! ===5=4=3=2=1="
ERROR_LOG="RESULT: timeout! killed! ${SEP} STATUS_CODE: -1 ${SEP} TIME_COST: 0"

###################################################

# run
timeout -s 9 ${kill_time} ${sh_file} ${code_file}

###################################################

# kill judge.
if [ $? != 0 ]
then
    echo "${ERROR_LOG}"
fi



# clean
#rm -rf ${code_file} ${code_file}.*
