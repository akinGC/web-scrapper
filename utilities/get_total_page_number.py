
def get_total_page_number(soup):
	no_pages_span = soup.find('span', {'class': "s-pagination-item s-pagination-disabled"})
	no_pages = int(no_pages_span.text.strip()) if no_pages_span else 1
	return no_pages