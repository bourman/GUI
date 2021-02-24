from time import sleep 
from selenium import webdriver 
from csv import reader 

contacts = []
path = r"c:/"
with open (path, "r") as f:
  csv_reader = reader(f)
  for row in csv_reader:
    contacts.append(row[0])
    
driver = webdriver.Chrome(executable_path=r"C:/")
driver.get ("https://web.whatsapp.com/")




