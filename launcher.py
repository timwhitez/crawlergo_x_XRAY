#!/usr/bin/python3
# coding: utf-8

import simplejson
import subprocess
import requests
import warnings
warnings.filterwarnings(action='ignore')

def opt2File(paths):
	try:
		f = open('crawl_result.txt','a')
		f.write(paths + '\n')
	finally:
		f.close()

def opt2File2(subdomains):
	try:
		f = open('sub_domains.txt','a')
		f.write(subdomains + '\n')
	finally:
		f.close()


def request0(req):
	proxies = {
	'http': 'http://127.0.0.1:7777',
	'https': 'http://127.0.0.1:7777',
	}
	urls0 =req['url']
	headers0 =req['headers']
	method0=req['method']
	data0=req['data']
	try:
		if(method0=='GET'):
			a = requests.get(urls0, headers=headers0, proxies=proxies,timeout=30,verify=False)
			opt2File(urls0)
		elif(method0=='POST'):
			a = requests.post(urls0, headers=headers0,data=data0, proxies=proxies,timeout=30,verify=False)
			opt2File(urls0)
	except:
		return

def main(data1):
	target = data1
	cmd = ["./crawlergo", "-c", "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe","-t", "10","--custom-headers","{\"User-Agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36\", \"Accept-Language\": \"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7\"}","-f","smart","--fuzz-path","--robots-path", "--output-mode", "json", target]
	rsp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, error = rsp.communicate()
	result = simplejson.loads(output.decode().split("--[Mission Complete]--")[1])
	req_list = result["req_list"]
	sub_domain = result["sub_domain_list"]
	print(data1)
	print("[crawl ok]")
	for subd in sub_domain:
		opt2File2(subd)
	for req in req_list:
		request0(req)
		#opt2File(req['url'])
	print("[request ok]")



if __name__ == '__main__':
	file = open("targets.txt")
	for text in file.readlines():
		data1 = text.strip('\n')
		main(data1)
