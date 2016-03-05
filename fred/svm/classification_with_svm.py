import pandas as pd
from sklearn import svm
import stupid_classifier
import display_classification


# Load the data from the CSV file to a Panda frame
data = pd.read_csv('data/banana.csv')

# Add some new features for later
data['At1_square'] = data.apply(lambda x: x['At1'] ** 2, axis=1)
data['At1_cube'] = data.apply(lambda x: x['At1'] ** 3, axis=1)
data['At2_square'] = data.apply(lambda x: x['At2'] ** 2, axis=1)
data['At2_cube'] = data.apply(lambda x: x['At2'] ** 3, axis=1)
data['At1_x_At2'] = data.apply(lambda x: x['At1'] * x['At2'], axis=1)
data['At1_square_x_At2_square'] = data.apply(lambda x: (x['At1'] ** 2) * (x['At2'] ** 2), axis=1)

# Display the data to have a good overview of the repartition
display_classification.display_data(data)

# Split the data into a training data (75%) and a testing data (25%)
data_train = data[:int((len(data) * 0.75))]
data_test = data[int((len(data) * 0.75)):]

# 1. Train a linear classifier with the default parameters
classifier_1 = svm.SVC(kernel='linear')
classifier_1.fit(data_train[['At1', 'At2']], data_train['Class'])
print "Classifier 1 accuracy = %f" % classifier_1.score(data_test[['At1', 'At2']], data_test['Class'])
display_classification.display_boundary(data, classifier_1)

# 2. Comparison of this classifier with a stupid classifier which always return false
classifier_2 = stupid_classifier.StupidClassifier(-1.0)
print "Classifier 2 accuracy = %f" % classifier_2.score(data_test[['At1', 'At2']], data_test['Class'])
display_classification.display_boundary(data, classifier_2)

# 3. Train a classifier with the RBF kernel
classifier_3 = svm.SVC(kernel='rbf')
classifier_3.fit(data_train[['At1', 'At2']], data_train['Class'])
print "Classifier 3 accuracy = %f" % classifier_3.score(data_test[['At1', 'At2']], data_test['Class'])
display_classification.display_boundary(data, classifier_3)

# 4. Train a classifier with the sigmoid kernel
classifier_4 = svm.SVC(kernel='sigmoid')
classifier_4.fit(data_train[['At1', 'At2']], data_train['Class'])
print "Classifier 4 accuracy = %f" % classifier_4.score(data_test[['At1', 'At2']], data_test['Class'])
display_classification.display_boundary(data, classifier_4)

# 5. Train a linear classifier with extended features
classifier_5 = svm.SVC(kernel='linear')
classifier_5.fit(data_train[['At1', 'At2', 'At1_square']], data_train['Class'])
print "Classifier 5 accuracy = %f" % classifier_5.score(data_test[['At1', 'At2', 'At1_square']], data_test['Class'])
display_classification.display_boundary(data, classifier_5, lambda X: [[x[0], x[1], x[0]**2] for x in X])

# 6. Train a linear classifier with more extended features
classifier_6 = svm.SVC(kernel='linear')
classifier_6.fit(data_train[['At1', 'At2', 'At1_square', 'At1_cube', 'At2_square', 'At2_cube', 'At1_x_At2', 'At1_square_x_At2_square']], data_train['Class'])
print "Classifier 6 accuracy = %f" % classifier_6.score(data_test[['At1', 'At2', 'At1_square', 'At1_cube', 'At2_square', 'At2_cube', 'At1_x_At2', 'At1_square_x_At2_square']], data_test['Class'])
display_classification.display_boundary(data, classifier_6, lambda X: [[x[0], x[1], x[0]**2, x[0]**3, x[1]**2, x[1]**3, x[0]*x[1], (x[0]**2)*(x[1]**2)] for x in X])




