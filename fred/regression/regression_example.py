import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.cross_validation import train_test_split


DATASET_SIZE = 100
POLYNOMIAL_ORDER_MAX = 20


def display_data(data):
  """ Display the data in a graph """
  plt.scatter(x=data['X'], y=data['Y'], c='b')
  plt.ylim([0, 25])
  plt.show()

def display_prediction(model, data, order):
  """ Display the model prediction in a graph """
  range_index = pd.DataFrame([[x / 100.0] for x in range(500)], columns=['X'])
  if order >= 2:
    for order in range(2, order + 1):
      feature_name = 'X%d' % order
      range_index[feature_name] = range_index.apply(lambda x: x['X'] ** order, axis=1)
  predictions = model.predict(range_index)
  plt.scatter(x=data['X'], y=data['Y'], c='b')
  plt.plot(range_index['X'], predictions, c='r')
  plt.show()

def rss(v1, v2):
  return sum((v1 - v2) ** 2) / len(v1)


# Generate a random dataset
data = pd.DataFrame(np.random.random(DATASET_SIZE) * 5.0, columns=['X'])
data['Y'] = data.apply(lambda x: (0.6 * x['X'] ** 4 - 6.0 * x['X'] ** 3 + 20.8 * x['X'] ** 2 - 30.1 * x['X'] + 21.4) + np.random.randn(), axis=1)

# Add some polynomial features
features = ['X']
for order in range(2, POLYNOMIAL_ORDER_MAX):
  feature_name = 'X%d' % order
  data[feature_name] = data.apply(lambda x: x['X'] ** order, axis=1)
  features += [feature_name]

# Split the data into a training set and a testing set
X_train, X_test, Y_train, Y_test = train_test_split(data[features], data['Y'], test_size=0.25)

# Display the data to have a good overview of the repartition
display_data(data)

# Train the linear classifier for polynomial features from 1 to 9
metrics = np.empty([POLYNOMIAL_ORDER_MAX, 3])
for order in range(1, POLYNOMIAL_ORDER_MAX):
  X_train_ = X_train[features[:order]]
  X_test_ = X_test[features[:order]]
  model = LinearRegression()
  model.fit(X_train_, Y_train)
  loss = rss(Y_train, model.predict(X_train_))
  accuracy = rss(Y_test, model.predict(X_test_))
  metrics[order][0] = order
  metrics[order][1] = loss
  metrics[order][2] = accuracy
  print "Model %d   loss = %f  accuracy = %f" % (order, loss, accuracy)
  display_prediction(model, data, order)


# Display the accuracy and the loss given the order, to see the underfit and overfit regions
plt.plot(metrics[1:,0], metrics[1:,1], c='g')
plt.plot(metrics[1:,0], metrics[1:,2], c='r')
plt.yscale('log')
plt.show()


