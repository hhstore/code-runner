#!/usr/bin/env bash
kill_time=$1
running_script=$2
code_file=$3

SEP="@@--@@--codebox--@@--@@"
###################################################

# run
timeout -s 9 ${kill_time} ${running_script} ${code_file}


# kill judge.
if [ $? != 0 ]
then
    echo "${SEP} KILL_CODE: ${?} INFO: timeout! killed!"
fi



# clean
#rm -rf ${code_file} ${code_file}.*
