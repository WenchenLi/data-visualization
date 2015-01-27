#python read.py

import csv

title = []
genre = []
hotness = []
attributes = []

with open('data.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		line = row[0]
		itemList = line.split('; ')
		title.append(itemList[0])
		genre.append(itemList[1])
		hotness.append(float(itemList[2]))
		attribute = []
		for i in range(3, len(itemList)):
			attribute.append(float(itemList[i]))
		attributes.append(attribute)
