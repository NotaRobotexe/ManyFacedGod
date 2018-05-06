import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import re 
import requests
import random

def get_mail(driver):
	time.sleep(1)
	element = driver.find_element_by_id("email")
	mail = element.text
	return str(mail)
	
def new_mail(driver):
	driver.get("https://www.minuteinbox.com/delete")

def get_code(driver):
	code = 0
	while(True):
		el = driver.find_element_by_id('schranka')
		raw = el.text
		if("Facebook" in raw):
			split_raw = raw.split(" ")
			index = split_raw.index("Facebook")
			code = split_raw[index-3]
			code = code[10:]
			break

		time.sleep(0.500)
	
	return code

def get_10_random_names():
	names_webpage = requests.get('http://random-name-generator.info/')
	names_html = names_webpage.text 
	
	raw_names = names_html[names_html.find("nameList")+23:names_html.find("clear: both")-35]
	raw_names = raw_names.replace("li","")
	raw_names = raw_names.replace(">","")
	raw_names = raw_names.replace("<","")
	raw_names = raw_names.replace("\n",",")
	raw_names = raw_names.replace("\t","")
	raw_names = raw_names.replace(" ","*")
	
	names = raw_names.split(",")
	return names[0]

def get_password():
	i=0
	password=""
	while(i<8):
		password += random.choice("1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
		i+=1
	return password	
	
def write_data_to_database(password,mail,name,dat_name):
	database = open(dat_name+".mfg","a")
	database.write(name+"*" + password+"*"+mail+"\n")
	database.close()
	







