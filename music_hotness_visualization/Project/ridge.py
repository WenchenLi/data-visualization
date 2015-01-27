#python ridge.py

import numpy as np
from sklearn import linear_model
import csv

hotness = []
attributes = []

with open('pca.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		line = row[0]
		itemList = line.split('; ')
		hotness.append(float(itemList[0]))
		attribute = []
		for i in range(1, len(itemList)):
			attribute.append(float(itemList[i]))
		attributes.append(attribute)

hotnessArr = np.array(hotness)
attributesArr = np.array(attributes)

clf = linear_model.Ridge(alpha = .5)
clf.fit(attributesArr, hotnessArr)

#clf.predict(attributesArrTest)