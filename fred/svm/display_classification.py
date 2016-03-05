import numpy as np
import matplotlib.pyplot as plt

def display_data(data):
  data_pos = data[data['Class'] > 0]
  data_neg = data[data['Class'] < 0]
  plt.scatter(x=data_pos['At1'], y=data_pos['At2'], c='b')
  plt.scatter(x=data_neg['At1'], y=data_neg['At2'], c='r')
  plt.show()

def display_boundary(data, classifier, convert_input_function=lambda x: x):
  data_pos = data[data['Class'] > 0]
  data_neg = data[data['Class'] < 0]
  x_min, x_max = data['At1'].min() - 0.5, data['At1'].max() + 0.5
  y_min, y_max = data['At2'].min() - 0.5, data['At2'].max() + 0.5
  xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.2), np.arange(y_min, y_max, 0.02))
  Z = classifier.predict(convert_input_function(np.c_[xx.ravel(), yy.ravel()]))
  Z = Z.reshape(xx.shape)
  plt.scatter(x=data_pos['At1'], y=data_pos['At2'], c='b')
  plt.scatter(x=data_neg['At1'], y=data_neg['At2'], c='r')
  plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.5)
  plt.show()

