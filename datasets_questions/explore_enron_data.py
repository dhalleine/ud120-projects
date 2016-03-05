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

# Question 6
print "Value of stock options exercised by Jeff Skilling: %d" % enron_data["SKILLING JEFFREY K"]['exercised_stock_options']

# Question 7
print "Who in Lay, Skilling and Fastow took home the most money"
print "Lay took: %d" % enron_data["LAY KENNETH L"]['total_payments']
print "Skilling took: %d" % enron_data["SKILLING JEFFREY K"]['total_payments']
print "Fastow took: %d" % enron_data["FASTOW ANDREW S"]['total_payments']

# Question 8
print "This guy didn't take anything: %s" % enron_data["HUGHES JAMES A"]['total_payments']

# Question 8
people_with_quantified_salary = 0
people_with_known_email = 0
for _, name in enumerate(enron_data):
  if enron_data[name]['salary'] != 'NaN':
    people_with_quantified_salary += 1
  if enron_data[name]['email_address'] != 'NaN':
    people_with_known_email += 1
print "There are %d people in this dataset without quantified salary" % people_with_quantified_salary
print "There are %d people in this dataset with a known email address" % people_with_known_email

# Question 9
num_people_with_unknow_total_payments = 0
num_people = 0
for _, name in enumerate(enron_data):
  num_people += 1
  if enron_data[name]['total_payments'] == 'NaN':
    num_people_with_unknow_total_payments += 1
print "Number of people with a specified total payment: %d/%d (%d %%)" % (num_people_with_unknow_total_payments, num_people, num_people_with_unknow_total_payments * 100 / num_people)

# Question 10
num_poi_with_unknown_payments = 0
num_people = 0
for _, name in enumerate(enron_data):
  num_people += 1
  if enron_data[name]['poi'] and enron_data[name]['total_payments'] == 'NaN':
    num_poi_with_unknown_payments += 1
print "Number of poi with unknown total payment: %d/%d (%d %%)" % (num_poi_with_unknown_payments, num_people, num_poi_with_unknown_payments * 100 / num_people)

# Question 11
num_people_with_unknown_payments = 0
num_people = 0
for _, name in enumerate(enron_data):
  num_people += 1
  if enron_data[name]['total_payments'] == 'NaN':
    num_people_with_unknown_payments += 1
num_people_with_unknown_payments += 10 # Fake new 10 people in this category
num_people += 10
print "Number of people with unknown total payment: %d/%d (%d %%)" % (num_people_with_unknown_payments, num_people, num_people_with_unknown_payments * 100 / num_people)

# Question 12
num_poi = 0
num_poi_with_unknown_stock = 0
for _, name in enumerate(enron_data):
  if enron_data[name]['poi']:
    num_poi += 1
    if enron_data[name]['total_stock_value'] == 'NaN':
      num_poi_with_unknown_stock += 1
num_poi += 10 # Fake new 10 people in this category
num_poi_with_unknown_stock += 10
print "Number of poi is %d and %d have unknown stock value (%d %%)" % (num_poi, num_poi_with_unknown_stock, num_poi_with_unknown_stock * 100 / num_poi)

