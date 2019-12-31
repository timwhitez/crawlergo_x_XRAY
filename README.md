# crawlergo_x_XRAY

360 0Kee-Team 公开的 crawlergo动态爬虫 结合 长亭XRAY扫描器的被动扫描功能 (其它被动扫描器同理)

https://github.com/0Kee-Team/crawlergo

https://github.com/chaitin/xray/tree/280f02d757c5682870450171f14cbade9d188687

## Usage: 

1. 下载xray最新的release, 下载crawlergo最新的release

### 2. 把launcher.py和targets.txt放在crawlergo.exe同目录下

3. 配置好并启动xray被动扫描(脚本默认配置为127.0.0.1:7777)若修改端口请同时修改launcher.py文件中的proxies

![image](https://raw.githubusercontent.com/timwhitez/crawlergo_x_XRAY/master/img/0.png)

![image](https://raw.githubusercontent.com/timwhitez/crawlergo_x_XRAY/master/img/1.png)

4. 配置好launcher.py的cmd变量中的crawlergo爬虫配置(主要是chrome路径改为本地路径), 默认为

./crawlergo -c C:\Program Files (x86)\Google\Chrome\Application\chrome.exe -t 20 -f smart --fuzz-path --output-mode json target

![image](https://raw.githubusercontent.com/timwhitez/crawlergo_x_XRAY/master/img/4.png)

配置参数详见crawlergo官方文档

5. 把目标url写进targets.txt,一行一个url

![image](https://raw.githubusercontent.com/timwhitez/crawlergo_x_XRAY/master/img/3.png)

6. 用python3运行launcher.py

7. 生成的sub_domains为爬虫爬到的子域名, crawl_result为爬虫爬到的url
