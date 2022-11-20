# 功能：将被git追踪到的文件按原目录拷贝


files=`git ls-tree -r main --name-only`
target_path="/d/f"

if [ ! -d `dirname ${target_path}` ]
then
    mkdir ${target_path}
else
    rm -rf ${target_path}/
    mkdir ${target_path}
fi


for i in ${files}
do
    if [ ! -d ${target_path}/`dirname ${i}` ]
    then
        mkdir ${target_path}/`dirname ${i}`
        echo -en "创建目录${target_path}/`dirname ${i}`\n"
    fi
    cp -r `pwd`/${i}  ${target_path}/`dirname ${i}`/
    echo -en "\t${target_path}/${i}\n"
done