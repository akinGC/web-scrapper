import pandas as pd

def create_csv(laptop_title,laptop_price, laptop_rating,product ):
	df = pd.DataFrame({
			'Title': laptop_title,
			'Price': laptop_price,
			'Rating': laptop_rating
		})
	df.to_csv(f'{product}.csv', index=False)
	