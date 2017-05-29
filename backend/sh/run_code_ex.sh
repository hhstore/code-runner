#!/usr/bin/env bash
prog=$1

###########error log info : ################
SEP="@@--@@--codebox--@@--@@"

ERROR_1="you must provide a file!"
ERROR_2="file does not exist!"
ERROR_3="invalid language!"

ERROR_LOG_1="INFO: ${ERROR_1} ${SEP} STATUS_CODE: 1 ${SEP} TIME_COST: 0"
ERROR_LOG_2="INFO: ${ERROR_2} ${SEP} STATUS_CODE: 1 ${SEP} TIME_COST: 0"
ERROR_LOG_3="INFO: ${ERROR_3} ${SEP} STATUS_CODE: 1 ${SEP} TIME_COST: 0"

##########error judge : ####################
if [ -z $1 ];then
    echo ${ERROR_LOG_1}
    exit 1
fi

if [ ! -f $1 ];then
    echo ${ERROR_LOG_2}
    exit 1
fi

#########run code : #######################

echo "INFO: "
TIME_START=`date +%s%N`; #time_countion

extension="${prog##*.}"
case "$extension" in    # 多版本支持
    "c99")
    gcc -o $prog.out -g $prog &&./$prog.out
    ;;
    "c11")
    gcc -o $prog.out -g $prog &&./$prog.out   # 待修改C11编译选项
    ;;
    "cpp99")
    g++ -o $prog.out -g $prog &&./$prog.out
    ;;
    "cpp11")
    g++ -o $prog.out -g $prog &&./$prog.out   # 待修改C++11编译选项
    ;;
    "java")
    javac $prog && java ${prog%.*}   # 待修改
    ;;
    "py2")
    python $prog     # 待修改
    ;;
    "py3")
    python $prog     # 待修改
    ;;
    "rb")
    ruby $prog
    ;;
    "go")
    go run $prog
    ;;
    "pl")
    perl $prog
    ;;
    *)
    echo ${ERROR_LOG_3}
    ;;
esac

###########################################

echo "${SEP} STATUS_CODE: $?"
TIME_END=`date +%s%N`;
time=$((TIME_END-TIME_START))
time=`expr $time / 1000000`

echo "${SEP} TIME_COST: ${time}"

###########################################
