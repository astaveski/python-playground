#By Adam Staveski and Rees Sweeney-Taylor
import csv
import json

with open('superheroes.json', 'r') as s:
	superheroes = json.load(s)

with open('superheroes.csv', 'w') as f:
	writer=csv.writer(f)
	writer.writerow(['name','age','secretIdentity', 'powers', 'squadName','homeTown','formed','secretBase','active'])

	members = superheroes['members']
	for hero in members:
		hero_name = hero['name']
		hero_age = hero['age']
		hero_secretIdentity = hero['secretIdentity']
		hero_powers = hero['powers']
		hero_squadname = superheroes['squadName']
		hero_homeTown = superheroes['homeTown']
		hero_formed = superheroes['formed']
		hero_secretBase = superheroes['secretBase']
		hero_active = superheroes['active']

		writer.writerow([hero_name,hero_age,hero_secretIdentity,hero_powers,hero_squadname,hero_homeTown,hero_formed,hero_secretBase,hero_active])