#!/usr/bin/python3
# coding: utf-8

import queue
import simplejson
import threading
import subprocess
import requests
import warnings
warnings.filterwarnings(action='ignore')

urls_queue = queue.Queue()
tclose=0

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



def request0():
	while tclose==0 or urls_queue.empty() == False:
		if(urls_queue.qsize()==0):
			continue
		print(urls_queue.qsize())
		req =urls_queue.get()
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
			continue
	return

def main(data1):
	target = data1
	cmd = ["./crawlergo", "-c", "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe","-t", "20","-f","smart","--fuzz-path", "--output-mode", "json", target]
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
		urls_queue.put(req)
	print("[scanning]")



if __name__ == '__main__':
	file = open("targets.txt")
	t = threading.Thread(target=request0)
	t.start()
	for text in file.readlines():
		data1 = text.strip('\n')
		main(data1)
	tclose=1
