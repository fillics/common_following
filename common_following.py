from selenium.webdriver import Chrome
from selenium import webdriver
from credentials import user, pw
import time, os
from time import sleep

controllo = 0

browser = webdriver.Chrome()
browser.get('https://www.instagram.com/')
sleep(2)
browser.find_element_by_xpath("//a[contains(text(), 'Accedi')]").click()
sleep(2)
browser.find_element_by_name("username").send_keys(user)
browser.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
browser.find_element_by_xpath("//button[@type='submit']").click()
sleep(5)
browser.find_element_by_xpath("//button[contains(text(), 'Non ora')]").click()


	
def get_lista(controllo):
	if controllo == 1:
		controllo = 0
	while controllo == 0:
		person = raw_input("Write username ")
		sleep(2)
		browser.find_element_by_xpath("//input[@type='text']").send_keys(person)
		sleep(5)
		browser.find_element_by_xpath("//span[contains(text(), '"+ person +"')]").click()
		sleep(2)
		try:
			browser.find_element_by_xpath("//a[contains(@href, '/"+ person +"/following')]").click()
			sleep(2)
			scroll_box = browser.find_element_by_xpath("/html/body/div[4]/div/div[2]")
			last_ht, ht = 0,1
			while last_ht != ht:
				last_ht = ht
				sleep(2)
				ht = browser.execute_script("""
					arguments[0].scrollTo(0, arguments[0].scrollHeight);
					return arguments[0].scrollHeight;
					""", scroll_box)

			links = scroll_box.find_elements_by_tag_name('a')
			names = [name.text for name in links if name.text != '']
			sleep(2)
			browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
			sleep(2)
			return names
		except:
			print("Private Account")
			controllo = 1
			return get_lista(controllo)
			

list1 = get_lista(controllo)
list2 = get_lista(controllo)
try:
	common = (set(list1).intersection(list2))
	print('\n'.join(common))
except:
	print("Error")

with open("common.txt", "w") as outfile:
    outfile.write("\n".join(common))
    
browser.close()
print("DONE")
		

