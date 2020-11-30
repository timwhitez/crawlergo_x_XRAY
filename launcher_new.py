#!/usr/bin/python3
# coding: utf-8
import simplejson
import threading
import subprocess
import requests
import warnings
import json
from fake_useragent import UserAgent

ua = UserAgent()

warnings.filterwarnings(action='ignore')

def get_random_headers():
    headers = {'User-Agent': ua.random}

    return headers


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



def main(data1):
	target = data1
	cmd = ["./crawlergo/crawlergo", "-c", "/root/crawlergo_x_XRAY/crawlergo/chrome-linux/chrome","-t", "5","-f","smart","--fuzz-path","--custom-headers",json.dumps(get_random_headers()), "--push-to-proxy", "http://127.0.0.1:7777/", "--push-pool-max", "10","--output-mode", "json" , target]
	rsp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, error = rsp.communicate()
	try:
		result = simplejson.loads(output.decode().split("--[Mission Complete]--")[1])
	except:
		return
	req_list = result["req_list"]
	sub_domain = result["sub_domain_list"]
	print(data1)
	print("[crawl ok]")
	for subd in sub_domain:
		opt2File2(subd)
	print("[scanning]")



if __name__ == '__main__':
	file = open("targets.txt")
	for text in file.readlines():
		data1 = text.strip('\n')
		main(data1)
