#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here

    difference = predictions - net_worths
    error = [e[0] for e in difference ** 2]
    threshold = sorted(error)[-len(predictions)/10:][0]

    for i, age in enumerate(ages):
      worth = net_worths[i][0]
      pred = predictions[i]
      error = ((worth - pred) ** 2)[0]
      if error < threshold:
        cleaned_data.append((age[0], worth, error))

    return cleaned_data

