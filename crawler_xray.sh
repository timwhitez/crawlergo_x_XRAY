#! /bin/bash
## File Name: crawler_xray.sh 
# Author: Mr.Frame
# Blog: https://askding.github.io/
# Date: Thu Mar 25 10:32:35 CST 2021
# Description:
#             联动crawlergo和xray
# 用法：
#    ./crawler_xray.sh   <path/to/target.txt>
#
# 提示:
# 需要修改chrome路径

thread=50                                 # 定义进程数
[ -e /tmp/$$.fifo ] || mkfifo /tmp/$$.fifo # 创建命名管道文件
exec 3<> /tmp/$$fifo                      # 创建FD 3，以可读（<）可写（>）的方式关联管道文件，FD 3具有命名管道的特性
rm -rf /tmp/$$fifo                        # 删除命名管道文件，通过FD 3


echo "./xray_darwin_amd64 webscan --listen 127.0.0.1:7777 --html-output xray-report.html" && sleep 1.5
./xray_darwin_amd64 webscan --listen 127.0.0.1:7777 --html-output xray-report.html &

for i in $(seq $thread); do
    echo >&3                              # 循环$thread次向FD 3写入\n , 类比一个令牌 
done

echo "./crawlergo -c ~/.BurpSuite/burpbrowser/88.0.4324.192/Chromium.app/Contents/MacOS/Chromium  -t 10  -f smart --fuzz-path --push-pool-max 10 --output-mode json --push-to-proxy http://127.0.0.1:7777 Target" && sleep 1.5
while read url; do
	read -u 3
	(
		./crawlergo -c ~/.BurpSuite/burpbrowser/88.0.4324.192/Chromium.app/Contents/MacOS/Chromium  -t 5  -f smart --fuzz-path --push-pool-max 10 --output-mode json --push-to-proxy http://127.0.0.1:7777 $url
	)&
	# 最后需要归还令牌
	echo >&3                          # 再次向FD 3写入\n , 类似归还令牌
done < $1
wait                                      # 等待并发进程执行完毕，执行后续命令 
if [ $? -eq 0 ]; then
	echo "Scan succeed. "
else
	echo "scan failed "
fi

exec 3<&-                                 # 关闭FD 3的读
exec 3>&-                                 # 关闭FD 3的写

