#By Adam Staveski and Rees Sweeney-Taylor
import csv
with open('vegetables.csv') as f:
	reader = csv.DictReader(f)
	vegetables = list(reader)
	print(vegetables)

import json
with open('vegetables.json','w') as g:
	json.dump(vegetables,g,indent=4)