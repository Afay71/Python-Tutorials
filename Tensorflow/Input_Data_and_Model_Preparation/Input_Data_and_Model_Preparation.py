# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sbn 
import sklearn
import tensorflow as tf

# Load the dataset
dataFrame = pd.read_excel("C:\\Users\\Arif Furkan\\OneDrive\\Belgeler\\Python_kullanirken\\bisiklet_fiyatlari.xlsx")
print(dataFrame)
sbn.pairplot(dataFrame)
plt.show()
print(dataFrame.describe())

# Split the data into Test/Train sets
from sklearn.model_selection import train_test_split
y = dataFrame["Price"].values
x = dataFrame[["BikeFeature1", "BikeFeature2"]].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=18)

# Scaling (Transforming the size of the data)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

# Creating the model
from tensorflow import keras
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

# Define the model
model = Sequential([
    Dense(4, activation="relu", input_shape=(2,)),
    Dense(4, activation="relu"),
    Dense(4, activation="relu"),
    Dense(1)
])

# Compile and train the model
model.compile(optimizer="rmsprop", loss="mse")
history = model.fit(x_train, y_train, epochs=250, verbose=0)

# Visualize and print the training loss
loss = history.history["loss"]
sbn.lineplot(x=range(len(loss)), y=loss)
plt.show()
trainLoss = model.evaluate(x_train, y_train, verbose=0)
testLoss = model.evaluate(x_test, y_test, verbose=0)
print(trainLoss)
print(testLoss)

# Test data predictions and actual values
testPredictions = model.predict(x_test)
print(testPredictions)
predictionDf = pd.DataFrame(y_test, columns=["Actual Y"])
print(predictionDf)

# Evaluate and visualize the predictions
testPredictions = pd.Series(testPredictions.reshape(330,))
predictionDf = pd.concat([predictionDf, testPredictions], axis=1)
predictionDf.columns = ["Actual Y", "Predicted Y"]
print(predictionDf)
sbn.scatterplot(x="Actual Y", y="Predicted Y", data=predictionDf)
plt.show()

# Calculate and print Mean Absolute Error and Mean Squared Error
from sklearn.metrics import mean_absolute_error, mean_squared_error
print(mean_absolute_error(predictionDf["Actual Y"], predictionDf["Predicted Y"]))
print(mean_squared_error(predictionDf["Actual Y"], predictionDf["Predicted Y"]))

# Predict new bike features
newBikeFeatures = [[1751, 1750]]
newBikeFeatures = scaler.transform(newBikeFeatures)
model.predict(newBikeFeatures)

# Reload and use the saved model
from tensorflow.python.keras.models import load_model
model.save("bike_model.h5")
loadedModel = load_model("bike_model.h5")
loadedModel.predict(newBikeFeatures)

