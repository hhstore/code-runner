#!/usr/bin/env bash
code_file=$1

###########error log info : ################
SEP="=1=2=3=4=5=== I Am A Dividing Line ! ===5=4=3=2=1="

ERROR_1="you must provide a file!"
ERROR_2="file does not exist!"
ERROR_3="invalid language!"

ERROR_LOG_1="${SEP} RESULT: ${ERROR_1} ${SEP} STATUS_CODE: -2 ${SEP} TIME_COST: 0"
ERROR_LOG_2="${SEP} RESULT: ${ERROR_2} ${SEP} STATUS_CODE: -3 ${SEP} TIME_COST: 0"
ERROR_LOG_3="${ERROR_3} ${SEP} STATUS_CODE: -4 ${SEP} TIME_COST: 0"
OK_LOG="${SEP} STATUS_CODE: 1 ${SEP} TIME_COST: 0"


########## error judge : ####################
if [ -z $1 ];then
    echo ${ERROR_LOG_1}
    exit 1
fi

if [ ! -f $1 ];then
    echo ${ERROR_LOG_2}
    exit 1
fi

###########################################

# create code_folder

file="${code_file##*/}"
folder="${file%%.*}"
extension="${file##*.}"


mkdir ${folder}
chmod 777 ${folder}
mv ${code_file} ${folder}
code_path="./${folder}/${folder}.${extension}"


###########################################
# test log:

#echo "Server Log:"
#echo "mkdir Folder name: ${folder}"
#rm -rf "/iDockerShare"
#echo "Current Folder: $(pwd)"
##echo "Current Folder Content: $(ls -a)"
#echo "Current Folder Content: $(ls)"
#echo "Code Path: ${code_path}"

######### run code : #######################

echo "${SEP} RESULT: "

TIME_START=`date +%s%N`; #time_countion

case "$extension" in
    "c")
    gcc -o ${code_path}.out -g ${code_path} &&./${code_path}.out
    ;;
    "cpp")
    g++ -o ${code_path}.out -g ${code_path} &&./${code_path}.out
    ;;
    "java")
    java_class=${code_path##*_}
    java_path="${folder}/${java_class}"
    mv ${code_path} ${java_path}
    cd ${folder}
    javac ${java_class} && java ${java_class%.*}
    cd ..
    ;;
    "go")
    go run ${code_path}
    ;;
    "pl")
    perl ${code_path}
    ;;
    "py")
    python ${code_path}
    ;;
    "rb")
    ruby ${code_path}
    ;;
    *)
    echo ${ERROR_LOG_3}
    ;;
esac

###########################################

echo "${SEP} STATUS_CODE: $?"

TIME_END=`date +%s%N`;
time=$((TIME_END-TIME_START))
time=`expr ${time} / 1000000`

echo "${SEP} TIME_COST: ${time}"

###########################################
