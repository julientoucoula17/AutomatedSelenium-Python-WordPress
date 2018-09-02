from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import xlrd



####################################### WORDPRESS ################################################################
website = eval('input("Enter your wordpress site(ex: www.google.com)   :  ")')+"/wp-admin/user-new.php?user_id=40"
Login = eval('input("Enter your username: ")')
Password = eval('input("Enter your Password: ")')
###################################################################################################################

loc = eval('input("Enter the path of the spreadsheet: ")')
#loc = ("C:/Users/tijul/AppData/Local/Programs/Python/Python36-32/user.xlsx")
 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
 
sheet.cell_value(0, 0)

# Program to extract a particular row value 
number_row = sheet.nrows


driver = webdriver.Firefox()
driver.get(website) 

user=driver.find_element_by_xpath("""//*[@id="user_login"]""")
user.send_keys(Login)

password=driver.find_element_by_xpath("""//*[@id="user_pass"]""")
password.send_keys(Password)

driver.find_element_by_xpath("""//*[@id="rememberme"]""").click()

driver.find_element_by_xpath("""//*[@id="wp-submit"]""").click()



time.sleep(4)

#In my case, var helps me build the identifier.
var = 0
for i in range(0,number_row):
	print(sheet.row_values(i))
	for j in sheet.row_values(i):
		if var == 0 or var == 1:
			var+=1	
			print(j)
			##########  add users #################
			id_new_user=driver.find_element_by_xpath("""//*[@id="user_login"]""")
			id_new_user.send_keys(j.lower())
		else:
			var=0
			mail_new_user=driver.find_element_by_xpath("""//*[@id="email"]""")
			mail_new_user.send_keys(j)

	#driver.find_element_by_xpath("""//*[@id="role"]""").click()
	driver.find_element_by_xpath("""/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form[2]/table[1]/tbody/tr[3]/td/select/option[4]""").click()
	driver.find_element_by_xpath("""//*[@id="noconfirmation"]""").click()
	time.sleep(2)
	driver.find_element_by_xpath("""//*[@id="createusersub"]""").click()
	time.sleep(4)
	driver.find_element_by_xpath("""/html/body/div[1]/div[1]/div[2]/ul/li[5]/ul/li[3]/a""").click()
	time.sleep(3)
#driver.close()
