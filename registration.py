import pyautogui
import linecache
import subprocess
import time
import asyncio
import psutil
from proxybroker import Broker
import signal, os 
from PIL import ImageGrab
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from mail import *
import threading ,queue,urllib3
from urllib3.contrib.socks import SOCKSProxyManager

def reg(name1,name2,mail,password):
	time.sleep(0.5)
	pyautogui.click(1098, 327, button='left')
	time.sleep(0.1)
	pyautogui.click(1098, 327, button='left')
	pyautogui.typewrite(name1)
	time.sleep(0.5)
	pyautogui.click(1283, 326, button='left')
	time.sleep(0.1)
	pyautogui.click(1283, 326, button='left')
	pyautogui.typewrite(name2)
	time.sleep(0.5)
	pyautogui.click(1084, 374, button='left')
	time.sleep(0.1)
	pyautogui.click(1084, 374, button='left')
	pyautogui.typewrite(mail[:len(mail)-4])
	time.sleep(0.8)
	pyautogui.typewrite(mail[len(mail)-4:])
	time.sleep(0.8)
	pyautogui.click(1068,426, button='left')
	time.sleep(0.1)
	pyautogui.click(1068,426, button='left')
	pyautogui.typewrite(mail)
	time.sleep(0.5)
	pyautogui.click(1071,469, button='left')
	time.sleep(0.1)
	pyautogui.click(1071,469, button='left')
	pyautogui.typewrite(password)
	time.sleep(0.5)
	pyautogui.click(1095,555, button='left')
	time.sleep(0.1)
	pyautogui.click(1095,555, button='left')
	time.sleep(0.6)
	pyautogui.press('pagedown')
	time.sleep(0.8)
	pyautogui.click(1161,555, button='left')
	time.sleep(0.1)
	pyautogui.click(1161,555, button='left')
	time.sleep(0.6)
	pyautogui.press('pagedown')
	time.sleep(0.6)
	pyautogui.click(1161,555, button='left')
	time.sleep(0.6)
	pyautogui.click(1059,595, button='left')
	time.sleep(0.5)
	pyautogui.click(1059,595, button='left')
	time.sleep(0.5)
	pyautogui.click(1149,711, button='left')

def confirm_mail( code ):
	time.sleep(0.3)
	pyautogui.click(720,278, button='left')
	pyautogui.typewrite(code)
	time.sleep(0.3)
	pyautogui.click(1169,336, button='left')
	
return_add = []
used = 10
async def show(proxies):
    global return_add
    while(1):
        proxy = await proxies.get()
        if proxy is None: break
        ip = str(proxy).split(" ")
        return_add.append(ip[5].replace(">",""))

def get_new_proxy():
	global used
	if(used==10):
		proxies = asyncio.Queue()
		broker = Broker(proxies)
		tasks = asyncio.gather(broker.find(types=['HTTP', 'HTTPS'], limit=10),
		show(proxies))

		loop = asyncio.get_event_loop()
		loop.run_until_complete(tasks)
		used=0
	else:
		used = used +1


	return return_add[used]

def CheckIfLoaded():
	color = [0,0,0]
	while(True):
		px=ImageGrab.grab().load()
		color = px[1204,650]
		time.sleep(0.2)
		if(color[1]<170 and color[1] > 140 and color[0]<110 and color[0] > 80 and color[2]<90 and color[2] > 50):
			break

def TestProxt(proxy,time):
	try:
		pr = urllib3.ProxyManager('http://'+proxy)
		pr.request('GET', 'https://www.facebook.com', timeout=time)
	except:
		try:
			prs = SOCKSProxyManager('socks5://'+proxy)
			prs.request('GET', 'https://www.facebook.com', timeout=time)
		except:
			return 0
		else:
			return 1
	else:
		return 1

urllib3.disable_warnings()
driver = webdriver.PhantomJS()
acount_created = 0

while(acount_created < 200):
	proxy = get_new_proxy()
	status = TestProxt(proxy,2)
	if(status == 1):
		p = subprocess.Popen("chromium\chrome.exe --start-maximized --proxy-server=\""+ proxy+"\" --incognito  www.facebook.com")	
		CheckIfLoaded()

		new_mail(driver)

		mail=get_mail(driver)
		password = get_password()
		raw_name = get_10_random_names()
		name= raw_name.split("*")

		reg(name[0],name[1],mail,password)
		confirm_mail(get_code(driver))
		
		write_data_to_database(password,mail,raw_name,"data")
		time.sleep(5)
		p.terminate()
		acount_created = acount_created+1
		print("acount created: "+ str(acount_created))
	else:
		print("bad proxy")
	
	
	
	