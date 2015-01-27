#python svm.py > svm.csv
from __future__ import division
import numpy as np
from sklearn import svm
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

genreUniq = list(set(genre))
numClass = len(genreUniq)

genreTrain = copy.deepcopy(genre[:40])
genreTest = copy.deepcopy(genre[40:])
attributesTrain = copy.deepcopy(attributes[:40])
attributesTest = copy.deepcopy(attributes[40:])

clf = svm.SVC()
clf = svm.SVC()
clf.fit(attributesTrain, genreTrain)
predictList = clf.predict(attributesTest)

count = 0
for i in range(len(predictList)):
	if predictList[i] == genreTest[i]:
		count = count + 1

for i in range(len(predictList)):
	print str(genreTest[i])+';',
	print str(predictList[i])+';',
	for j in range(len(attributesTest[i])-1):
		print str(attributesTest[i][j])+';',
	print attributesTest[i][-1]
print 

print 'accuracy rate: ' + str( count/len(genreTest) )