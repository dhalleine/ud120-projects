#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]

sorted_data = {}
for f in data_dict:
  bonus = data_dict[f]['bonus']
  if bonus:
    sorted_data[bonus] = f

import collections
sorted_data = collections.OrderedDict(sorted(sorted_data.items()))
for sd in sorted_data:
  print "%s - %s" % (sorted_data[sd], sd)

data_dict.pop('TOTAL')
data = featureFormat(data_dict, features)

### your code below

for point in data:
  salary = point[0]
  bonus = point[1]
  matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()



