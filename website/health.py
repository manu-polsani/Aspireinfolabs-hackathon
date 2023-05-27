#!/usr/bin/env python
# coding: utf-8

# In[3]:

import pandas as pd
from sklearn.cluster import KMeans

# Importing the dataset
data = pd.read_csv('health_data.csv')  # Replace 'clustered_dataset.csv' with the actual path to your dataset file

# Preprocessing the dataset (if needed)
# ...

# Selecting the features for clustering (if needed)
# features = data[['feature1', 'feature2', ...]]

# Creating the K-means model
kmeans = KMeans(n_clusters=2)  # Replace 2 with the desired number of clusters

# Fitting the model to the data
kmeans.fit(data)

# Getting the cluster labels
labels = kmeans.labels_


# In[ ]:

def calc(Steps, weight, sleep_duration, calories_burn, Water_Intake):
    # Convert input features to numeric values
    Steps = float(Steps)
    weight = float(weight)
    sleep_duration = float(sleep_duration)
    calories_burn = float(calories_burn)
    Water_Intake = float(Water_Intake)

    # Create input array
    input_data = [[Steps, weight, sleep_duration, calories_burn, Water_Intake]]

    # Make prediction
    prediction = kmeans.predict(input_data)  # Replace 'kmeans' with your KMeans model object

    # Initialize counters
    UnHealthy = 0
    Healthy = 0

    # Count predictions
    if prediction == [0]:
        UnHealthy += 1
    else:
        Healthy += 1

    # Return the counters
    return UnHealthy, Healthy






#add random values to KK according to the parameters mentioned above to check the proabily of attrition of the employee