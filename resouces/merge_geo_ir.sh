#!/bin/bash

CURRENT_DIR=$(cd $(dirname $0); pwd)
SPECIAL_CODES=(ir)
LOG_FILE="merge.log"

target_dir=$1
if [ -z "$target_dir" ]; then
    target_dir=$CURRENT_DIR
fi

target_dir=$(readlink -f $target_dir)
if [ ! -d "$target_dir" ]; then
    echo "${target_dir} unkown directory"
    exit 1
fi

merge_src_dir=$2
if [ -z "$merge_src_dir" ]; then
    echo "ERR: empty merge source!"
    exit 1
fi
merge_src_dir=$(readlink -f $merge_src_dir)


## Begin

LOG_FILE="${target_dir}/${LOG_FILE}"
cat /dev/null > $LOG_FILE

cd $merge_src_dir
echo -e "\n\ttarget>> ${target_dir}\n\tmerging<= ${merge_src_dir}\n\n"

# Loop through files in folder a
for file1 in $(ls *.srs); do
  # Get the filename without path
    filename1=${file1##*/}

    fsub=${filename1%%-*}
    filename2=${filename1#*-}

    # Country code
    ccode=$(echo "$filename1" |rev | awk -F'[-|.|!]' '{print $2}' | rev | awk -F'@' '{print $1}' )

    # Check if file exists in folder b with the same name
    file2="$target_dir/$fsub/$filename2"

    # If file not found, print filename
    if [ ! -f $file2 ]; then
        cp $file1 $file2
        echo "${fsub}/${filename2}" >> $LOG_FILE

    elif [[ " ${SPECIAL_CODES[@]} " =~ " $ccode " ]]; then
        cp $file1 $file2
        echo "${fsub}/${filename2}" >> $LOG_FILE
        # echo -e "\n\t$ccode $file1"
    fi
done
cat $LOG_FILE


#END FILE