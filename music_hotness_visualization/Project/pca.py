#python pca.py > pca.csv
from __future__ import division
import numpy as np
from sklearn.decomposition import PCA, KernelPCA
from sklearn.datasets import make_circles
from itertools import chain


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


attributesFlat = list(chain(*attributes))
numMax = max(attributesFlat)

attributesNorm = []
for item in attributes:
	itemNorm = [x/numMax for x in item]
	attributesNorm.append(itemNorm)

hotnessArr = np.array(hotness)
attributesArr = np.array(attributesNorm)

kpca = KernelPCA(n_components = 7, kernel="poly", fit_inverse_transform=True, gamma=10)
attributesArrKPCA = kpca.fit_transform(attributesArr)

j = 0

for item in attributesArrKPCA:
	print str(hotness[j])+';',
	j = j + 1
	for i in range(len(item)-1):
		print str(item[i])+';',
	print str(item[-1])
