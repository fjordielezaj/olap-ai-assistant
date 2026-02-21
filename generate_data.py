import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Configuration according to the guide (Source 6.1)
n_rows = 10000
regions = ['North America', 'Europe', 'Asia Pacific', 'Latin America']
categories = {
    'Electronics': ['Phones', 'Laptops', 'Accessories'], 
    'Furniture': ['Chairs', 'Tables', 'Beds'], 
    'Office Supplies': ['Paper', 'Pens', 'Binders'], 
    'Clothing': ['Shirts', 'Pants', 'Shoes']
}
segments = ['Consumer', 'Corporate', 'Home Office']

# Data Generation
data = []
start_date = datetime(2022, 1, 1)

for i in range(n_rows):
    date = start_date + timedelta(days=np.random.randint(0, 1095))
    cat = np.random.choice(list(categories.keys()))
    subcat = np.random.choice(categories[cat])
    qty = np.random.randint(1, 10)
    price = np.round(np.random.uniform(10, 1000), 2)
    revenue = np.round(qty * price, 2)
    cost = np.round(revenue * np.random.uniform(0.5, 0.8), 2)
    
    data.append([
        date, date.year, f"Q{(date.month-1)//3+1}", date.month, date.strftime('%B'),
        np.random.choice(regions), "CountryX", cat, subcat, 
        np.random.choice(segments), qty, price, revenue, cost, revenue - cost
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    'order_date', 'year', 'quarter', 'month', 'month_name', 
    'region', 'country', 'category', 'subcategory', 
    'customer_segment', 'quantity', 'unit_price', 'revenue', 'cost', 'profit'
])

# Save to data/ folder
if not os.path.exists('data'): 
    os.makedirs('data')

df.to_csv('data/global_retail_sales.csv', index=False)
print("File 'global_retail_sales.csv' was created successfully in the data/ folder!")