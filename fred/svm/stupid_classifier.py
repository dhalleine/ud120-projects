from sklearn.base import BaseEstimator, ClassifierMixin
import numpy as np

class StupidClassifier(BaseEstimator, ClassifierMixin):
  """A stupid classifier which always return the same value"""

  def __init__(self, value_to_return=1.0):
    self.value_to_return = value_to_return

  def fit(self, X, y=None):
    # Nothing, this classifier doesn't learn
    pass

  def _meaning(self, x):
    return True

  def predict(self, X, y=None):
    if isinstance(X, np.ndarray):
      return np.array([self.value_to_return for x in X])
    else:
      return [self.value_to_return for x in X.iterrows()]

  def score(self, X, y=None):
    from sklearn.metrics import accuracy_score
    return accuracy_score(y, self.predict(X))


