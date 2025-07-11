from bs4 import BeautifulSoup 

from utilities.create_csv import create_csv
from utilities.search_for_item import get_page_source
from utilities.search_for_item import update_page_param
from utilities.get_total_page_number import get_total_page_number
from constants.shopping_list import shopping_site 
from selenium import webdriver
import time 

laptop_title = []
laptop_price = []
laptop_rating = []

def perform_data_collection(search_item_name):
	driver = webdriver.Chrome()
	soup = BeautifulSoup(get_page_source(driver, shopping_site, True, search_item_name), 'html.parser')

	no_pages = get_total_page_number(soup)

	# Loop through all pages
	for i in range(1, no_pages):

		page_url = update_page_param(driver,i)
		soup = BeautifulSoup(get_page_source(driver, page_url), 'html.parser')

		products = soup.find_all('div', { "data-component-type": "s-search-result" })

		for product in products:
			title_element = product.find(
				'a',
				class_=lambda value: (
					value
					and 'a-link-normal' in value
					and 'a-text-normal' in value
					and any(cls.startswith('s-line-clamp-') for cls in value.split())
				)
			)



			price_element = product.find('span', {"class": "a-price-whole"})
			rating_element = product.find('span', {"class": "a-icon-alt"})
	
			if title_element and price_element:
				title_text = title_element.text.strip()
				price_text = price_element.text.strip().replace(',', '')

				try:
					
					laptop_title.append(title_text)
					laptop_price.append('₹' + price_text)
					rating_text = rating_element.text.strip() if rating_element else "No rating"
					laptop_rating.append(rating_text)
				except ValueError:
					continue
	
	create_csv(laptop_title,laptop_price, laptop_rating,search_item_name )
	laptop_title.clear()
	laptop_price.clear()
	laptop_rating.clear()
	driver.quit()
