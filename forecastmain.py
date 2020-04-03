#Author: Manish Shah
#Created on: April 1, 2020

from bs4 import BeautifulSoup
import requests
import os
from packages import citiesurl
import re
import sys

print("""
Created on: April 1, 2020
Author: Manish Kumar Shah
Gmail: mkshah141@gmail.com
""")

def forecast():
	print("**Wellcome to Weather Forecaster1.2**")
	print("""
		1.Assam (AS)
		2.Arunachal Pradesh (AR)
		3.Andhra Pradesh (AP)
		4.Bihar (BR)
		5.Chhattisgarh(CG)
		6.Goa (GA)
		7.Gujarat (GJ)
		8.Haryana (HR)
		9.Himachal Pradesh (HP)
		10.Jammu and Kashmir (JK)
		11.Jharkhand (JK)
		12.Karnataka (KA)
		13.Kerala (KL)
		14.Madhya Pradesh (MP)
		15.Maharashtra (MH)
		16.Manipur (MN)
		17.Meghalaya (ML)
		18.Mizoram (MZ)
		19.Nagaland (NL)
		20.Odisha (OR)
		21.Punjab (PB)
		22.Rajasthan (RJ)
		23.Sikkim (SK)
		24.Tamil Nadu (TN)
		25.Telangana (TS)
		26.Tripura (TR)
		27.Uttar Pradesh (UP)
		28.Uttarakhand (UK)
		29.West Bengal (WB)
	""")
	selectstate = input("Select your State(1-28): ")
	if selectstate == '1':
		print("""
			1. Guwahati
			2. Silchar
			3. Nagaon
			4. Tinsukia
			5. Dibrugarh
			6. Jorhat
			7. Tezpur
	      	      """)
		userinput = input("Select any choice from the cities name given below:- ")
		url = citiesurl.geturlassam(userinput)	#I have to work with this variable
	elif selectstate == '2':
		print("""
			1. Along
			2. Itanagar
			3. Tawang
			4. Ziro
			5. Bomdila
	      	      """)
		userinput = input("Select any choice from the cities name given below:- ")
		url = citiesurl.geturlarunachal(userinput)	#I have to work with this variable
	elif selectstate == '3':
		print("""
			1. Visakhapatnam
	      	      """)
		userinput = input("Select any choice from the cities name given below:- ")
		url = citiesurl.geturlandhra(userinput)	#I have to work with this variable
	
	agent = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
	page = requests.get(url, headers=agent)
	soup = BeautifulSoup(page.content, 'lxml') #= bs4 element
	#print(soup.prettify())


	#alldata is a tag of bs4 element
	alldata = soup.find_all(class_='day-panel')

	#This will give us all the required data we just need to arrange it nicely
	datas = []
	for h in alldata:
	    datas.append(h.text.strip())

	#Code for Current Weather Report
	Current_Weather_Report = re.split(r'[\n\t]+', datas[0])
	print("\t",Current_Weather_Report[0])
	print("\t Time: ",Current_Weather_Report[1])
	print("\t Temperature: ",Current_Weather_Report[2],Current_Weather_Report[3])
	print("\t",Current_Weather_Report[4],Current_Weather_Report[5])
	print("\t",Current_Weather_Report[6])

	#Code for Today Weather Report
	Today_Weather_Report = re.split(r'[\n\t]+', datas[1])
	print("\n\t",Today_Weather_Report[0],"Weather Report")
	print("\t Month/Day: ",Today_Weather_Report[1])
	print("\t Temperature: ",Today_Weather_Report[2],Today_Weather_Report[3])
	print("\t",Today_Weather_Report[4],Today_Weather_Report[5])
	print("\t",Today_Weather_Report[6])

	#Code for Tonight Weather Report
	Tonight_Weather_Report = re.split(r'[\n\t]+', datas[2])
	print("\n\t",Tonight_Weather_Report[0],"Weather Report")
	print("\t Month/Day: ",Tonight_Weather_Report[1])
	print("\t Temperature: ",Tonight_Weather_Report[2],Tonight_Weather_Report[3])
	print("\t",Tonight_Weather_Report[4],Tonight_Weather_Report[5])
	print("\t",Tonight_Weather_Report[6])

	#Code for Tommorrow Weather Report
	Tommorrow_Weather_Report = re.split(r'[\n\t]+', datas[3])
	print("\n\t",Tommorrow_Weather_Report[0],"Weather Report")
	print("\t Month/Day: ",Tommorrow_Weather_Report[1])
	print("\t Temperature: ",Tommorrow_Weather_Report[2],Tommorrow_Weather_Report[3])
	print("\t",Tommorrow_Weather_Report[4],Tommorrow_Weather_Report[5])

forecast()
while True:
	yesorno = input("Do you want to run this program again: (y/n): ")
	if yesorno == 'y':
		os.system("clear")
		forecast()
	elif yesorno == 'n':
		print("Thank You!!! Have a Good Day ahed.")
		sys.exit(0)
	else:
		print("You have not entered correct input Exiting...")
		sys.exit(0)
