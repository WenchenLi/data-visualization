#python ridgeFull.py > ridgeFull.csv

import numpy as np
from sklearn import linear_model
import copy
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

hotnessTrain = copy.deepcopy(hotness[:40])
hotnessTest = copy.deepcopy(hotness[40:])
attributesTrain = copy.deepcopy(attributes[:40])
attributesTest = copy.deepcopy(attributes[40:])

hotnessTrainArr = np.array(hotnessTrain)
hotnessTestArr = np.array(hotnessTest)
attributesTrainArr = np.array(attributesTrain)
attributesTestArr = np.array(attributesTest)

clf = linear_model.Ridge(alpha = .5)
clf.fit(attributesTrainArr, hotnessTrainArr)

predictArr = clf.predict(attributesTestArr)


for i in range(len(predictArr)):
	print str(hotnessTestArr[i])+';',
	print str(predictArr[i])+';',
	for j in range(len(attributesTestArr[i])-1):
		print str(attributesTestArr[i][j])+';',
	print attributesTestArr[i][-1]
print 


print 'average residual error: ' + str( np.mean( abs(predictArr - hotnessTestArr) ) )