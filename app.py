from constants.shopping_list import items_to_fetch 
from search import perform_data_collection



def initialize_search():
	for searchItem in items_to_fetch:
		perform_data_collection(searchItem)



initialize_search()