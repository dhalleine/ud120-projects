#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# Question 1
print "There are %d distinct people in the Enron dataset" % len(enron_data)

# Question 2
print "There are %d features for each person" % len(enron_data["SKILLING JEFFREY K"])

# Question 3
pois = 0
for _, instance in enron_data.iteritems():
  if instance['poi']:
    pois += 1
print "There are %d pois" % pois

# Question 4
print "Total stock value of James Prentice is %d" % enron_data["PRENTICE JAMES"]['total_stock_value']

# Question 5
print "There are %d emails from Wesley Colwell to poi" % enron_data["COLWELL WESLEY"]['from_this_person_to_poi']


