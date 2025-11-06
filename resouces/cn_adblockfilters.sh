#!/bin/bash
##adblockfilters
#   adblockclashlite.list 更新至 ACL:BanAD
#   https://github.com/217heidai/adblockfilters
#

CURRENT_DIR=$(cd $(dirname $0); pwd)

target_dir=$1
if [ -z "$target_dir" ]; then
    target_dir=$CURRENT_DIR
fi

if [ ! -d "$target_dir" ]; then
    echo "${target_dir} unkown directory"
    exit 1
fi

work_dir=$(realpath "$target_dir")
target_dir="${work_dir}/chinese"
sing_exe="${work_dir}/sing-box"

LOG_FILE="merge.log"
# cat /dev/null > $LOG_FILE

# ———————————————————————————————————————————————————————————————————————————————————————————————


function download_adblockfilters() {
    mkdir -p $target_dir/adblockfilters
    cd $target_dir/adblockfilters/
    aclssr_dir=$(dirname $work_dir)/ACL4SSR

    # PASS "AdGuard_Base_filter.txt" "AdGuard_Chinese_filter.txt" "AdGuard_DNS_filter.txt" "AdGuard_Mobile_Ads_filter.txt"
    file_array=("adblockclashlite.list" "adblockclash.list")
    for file in "${file_array[@]}"; do
        wget --no-check-certificate -q --show-progress -T10 -t3 -O $file "https://github.com/217heidai/adblockfilters/raw/refs/heads/main/rules/${file}"

        if [[ "$file" == *.list ]]; then
            basename=${file%.list}
            echo "source << ${basename}"

            # ad keys
            if [[ "$file" == "adblockclashlite.list" ]]; then
                # 合并文件
                cat "${aclssr_dir}/Clash/BanAD.list" > temp_file && cat "$file" >> temp_file
                # 合并碎片
                sed -i '/17173.com/d' temp_file
                cat $CURRENT_DIR/fragment/BanAD.list >> temp_file

                # 去重
                sort -u temp_file > "$file"
            fi

            #convert to json
            python $CURRENT_DIR/convert_json.py --single  $target_dir/adblockfilters/$file $basename.json

            #convert to srs
            srs_file=${basename}.srs
            $sing_exe rule-set compile $basename.json -o $srs_file
            echo -e "output >> ${srs_file}\n"
        fi
    done

    # BanAD
    acl_dir=$work_dir/ACL4SSR
    echo "copy adblockclashlite:BanAD to ${acl_dir}"
    cp ./adblockclashlite.json $acl_dir/BanAD.json
    cp ./adblockclashlite.srs $acl_dir/BanAD.srs

    # AdGuard
    adguard_dir=$work_dir/AdGuard
    if [ -d "$adguard_dir" ]; then
        echo "move AdGuard files to ${adguard_dir}"
        mv ./AdGuard* $adguard_dir/
    fi

}

function merge_hiddify_geo(){
    src_dir=$(dirname $work_dir)/hiddify-geo/country
    LOG_FILE="${work_dir}/geo/${LOG_FILE}"
    echo "merge dir >> ${src_dir}"

    # 遍历country目录下所有以geoip或geosite开头的.srs文件
    for file1 in $(ls $src_dir/geo*-*.srs); do
        filename1=${file1##*/}
        # 修正2：移除多余的$$符号
        caty=${filename1%%-*}    # 截取第一个"-"前的部分
        country=${filename1#*-}   # 截取第一个"-"后的部分
        # echo "类型: $caty, 国家代码: $country"

        # Check if file exists in folder b with the same name
        file2="$work_dir/geo/$caty/$country"

        # If file not found, print filename
        if [ ! -f $file2 ]; then
            cp $file1 $file2
            echo "hiddify-geo/country/${filename1}" >> $LOG_FILE
        fi

    done
}

# 替换碎片
function replace_fragment(){
    aclssr_dir=$(dirname $target_dir)/ACL4SSR
    geosite_dir=$(dirname $target_dir)/geo/geosite

    # banad 在 func download_adblockfilters 中已经合并

    # ProxyGFWlist.json
    cd $aclssr_dir
    basename="ProxyGFWlist"
    sed -i 's/"ip138.com",//g' $basename.json
    echo "replace ==>  $aclssr_dir/$basename.json"
    $sing_exe rule-set compile $basename.json -o $aclssr_dir.srs

    # geosite cn
    cd $geosite_dir
    sed -i '/browserleaks.com/d' "${geosite_dir}/cn.json"
    echo "replace ==> ${geosite_dir}/cn.json"
    $sing_exe rule-set compile cn.json -o cn.srs

}


# ———————————————————————————————————————————————————————————————————————————————————————————————
chmod +x $sing_exe
# rm -rf $target_dir
mkdir $target_dir ; cd $target_dir
echo "start<= ${target_dir}"

download_adblockfilters
merge_hiddify_geo
replace_fragment

echo "end<= ${target_dir}"
#END FILE











