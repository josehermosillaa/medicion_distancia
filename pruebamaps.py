from selenium import webdriver

chromedrive_path = './chromedriver'
driver = webdriver.Chrome()
url = 'https://www.google.com/maps/dir/-33.451555%09-70.642371/Bandera+%26+Catedral,+Santiago,+Regi%C3%B3n+Metropolitana/@-33.4429626,-70.6537405,16z/data=!3m1!4b1!4m12!4m11!1m3!2m2!1d-70.644469!2d-33.448255!1m5!1m1!1s0x9662c5a48deb345d:0x86bab168cee06472!2m2!1d-70.6526371!2d-33.4375024!3e2?entry=ttu'
	

driver.get(url)
page_content = driver.page_source
from parsel import Selector
response = Selector(page_content)
results = response.xpath('//div[@class="XdKEzd"]/div[@class="ivN21e tUEI8e fontBodyMedium"]/text()')
print(results[0].get())

