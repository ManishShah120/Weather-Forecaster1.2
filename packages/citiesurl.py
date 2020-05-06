import os

def geturlassam(choice):
	if choice == '1' or choice == "Guwahati":
		print("\t Weather Report of Guwahati")
		print("Scraping Data...")
		return "https://www.accuweather.com/en/in/guwahati/186893/weather-forecast/186893"
	elif choice == '2' or choice == "Silchar":
		print("\t Weather Report of Silchar")
		print("Scraping Data...")
		return "https://www.accuweather.com/en/in/silchar/186891/weather-forecast/186891"
	elif choice == '3' or choice ==  "Nagaon":
		print("\t Weather Report of Nagaon")
		print("Scraping Data...")
		return "https://www.accuweather.com/en/in/nagaon/186884/weather-forecast/186884"
	elif choice == '4' or choice == "Tinsukia":
		print("\t Weather Report of Tinsukia")
		print("Scraping Data...")
		return "https://www.accuweather.com/en/in/tinsukia/186885/weather-forecast/186885"
	elif choice == '5' or choice =="Dibrugarh":
		print("\t Weather Report of Dibrugarh")
		print("Scraping Data...")
		return "https://www.accuweather.com/en/in/dibrugarh/186892/weather-forecast/186892"
	elif choice == '6' or choice =="Jorhat":
		print("\t Weather Report of Jorhat")
		print("Scraping Data...")
		return "https://www.accuweather.com/en/in/jorhat/186887/weather-forecast/186887"
	elif choice == '7' or choice =="Tezpur":
		print("\t Weather Report of Tezpur")
		print("Scraping Data...")
		return "https://www.accuweather.com/en/in/tezpur/186888/weather-forecast/186888"

def geturlarunachal(choice):
	if choice == '1' or choice == "Along":
		print("\t Weather Report of Along")
		print("Scraping Data...")
		return "https://www.accuweather.com/en/in/along/3350032/weather-forecast/3350032"
	elif choice == '2' or choice == "Itanagar":
		print("\t Weather Report of Itanagar")
		print("Scraping Data...")
		return "https://www.accuweather.com/en/in/itanagar/357099/weather-forecast/357099"
	elif choice == '3' or choice == "Tawang":
		print("\t Weather Report of Tawang")
		print("Scraping Data...")
		return "https://www.accuweather.com/en/in/tawang/357115/weather-forecast/357115"
	elif choice == '4' or choice == "Ziro":
		print("\t Weather Report of Ziro")
		print("Scraping Data...")
		return "https://www.accuweather.com/en/in/ziro/357142/weather-forecast/357142"
	elif choice == '5' or choice == "Bomdila":
		print("\t Weather Report of Bomdila")
		print("Scraping Data...")
		return "https://www.accuweather.com/en/in/bomdila/357148/weather-forecast/357148"
		
def geturlandhra(choice):
	if choice == '1' or choice == 'Visakhapatnam':
		print("\t Weather Report of Visakhapatnam")
		print("Scraping Data...")
		return "https://www.accuweather.com/en/in/visakhapatnam/202192/weather-forecast/202192"

# In this way you can add all the states cities url
'''
def geturlSTATENAME(choice):
	if choice == '1' or choice == 'CITYNAME':
		print("\t Weather Report of CITYNAME")
		print("Scraping Data...")
		return "URL OF THE CITY FROM THAT STATE"
'''
# Also don't forget to add the cities and name in the forecastmain.py file
