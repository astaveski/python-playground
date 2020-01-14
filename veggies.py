#By Adam Staveski and Rees Sweeney-Taylor
vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

import csv
with open('vegetables.csv', 'w') as f:
	writer=csv.writer(f)
	writer.writerow(['name','color','length'])
	for veg in vegetables:
		veg_name = veg["name"]
		veg_color = veg["color"]
		veg_length = len(veg_name)
		row = [veg_name,veg_color,veg_length]
		writer.writerow(row)