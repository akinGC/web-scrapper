from constants.shopping_list import shopping_site 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse


def search_for_item(driver, search_item_name):
	search_box = driver.find_element(By.ID, "twotabsearchtextbox")
	search_box.send_keys(search_item_name)
	search_box.send_keys(Keys.RETURN)
	time.sleep(3)
	


def get_page_source(driver,url, should_perform_search=False, search_item_name=None):
	
	driver.get(url)
	time.sleep(2)
	if should_perform_search :
		search_for_item( driver,search_item_name)

	return driver.page_source


def update_page_param(driver, count):
    url = driver.current_url
    parts = urlparse(url)
    query = parse_qs(parts.query)
    query['page'] = [str(count)]
    new_query = urlencode(query, doseq=True)
    return urlunparse(parts._replace(query=new_query))