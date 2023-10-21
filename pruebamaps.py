import pandas as pd
import time
from tqdm import tqdm
from selenium import webdriver
from parsel import Selector
from selenium.webdriver.common.by import By
chromedrive_path = './chromedriver'

	
xls = pd.ExcelFile('estaciones_proyectos.xlsx')
estaciones = pd.read_excel(xls, sheet_name='errores')
medicion = []
id_permiso = []
metro = []
linea = []
for i, data in tqdm(estaciones.iterrows()):
    url = f"https://www.google.com/maps/dir/{data['latitude']}%09{data['longitude']}/{data['Ubicación']}/"
    driver = webdriver.Chrome()
    driver.get(url) 
    id_permiso.append(data['id_permiso'])
    metro.append(data['Estación'])
    linea.append(data['Linea'])
    button = driver.find_element(By.XPATH, '//div[@data-travel_mode="2"]')
    button.click()
    time.sleep(1)
    page_content = driver.page_source

    response = Selector(page_content)
    results = response.xpath('//div[@class="XdKEzd"]/div[@class="ivN21e tUEI8e fontBodyMedium"]/text()')
    # print(results[0].get())
    medicion.append(results[0].get() if results else "error")
    driver.quit()
columnas = ['id_permiso','Estación', 'Linea', 'Medición']
df = pd.DataFrame(list(zip(id_permiso,metro,linea,medicion)), columns=columnas)
df.to_excel('nuevo_excel.xlsx',index=False)