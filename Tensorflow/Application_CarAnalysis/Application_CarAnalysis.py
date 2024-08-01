# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn

# Read the dataset
dataFrame = pd.read_excel("C:\\Users\\Arif Furkan\\OneDrive\\Belgeler\\Python_kullanirken\\merc.xlsx")
print(dataFrame.head())
print(dataFrame.describe())
print(dataFrame.isnull().sum())
# Show the distribution of price
sbn.displot(dataFrame["price"])
plt.show()

# Examine the correlation of numerical data
numeric_df = dataFrame.select_dtypes(include=np.number) # The select_dtypes method allows you to select specific data types in the DataFrame. The include=np.number expression selects only columns containing numeric data types.
print(numeric_df.corr()) # Calculates the correlations between the columns in the numeric_df DataFrame. The corr() method calculates the Pearson correlation coefficients and returns the results as a correlation matrix.
print(numeric_df.corr()["price"].sort_values()) # Retrieves the correlations of the price column with other columns, sorts them, and prints them. corr()["price"] selects the "price" column from the correlation matrix. The sort_values() method sorts these correlations by their values.

# Show the relationship between mileage and price
sbn.scatterplot(x="mileage", y="price", data=dataFrame)
plt.show()

# Remove the top 1% most expensive cars
dataFrame.sort_values("price", ascending=False).head(25) # The ascending=False parameter sorts in descending order. The head(25) method retrieves and prints the first 25 rows of the sorted DataFrame.
print(len(dataFrame))
print(len(dataFrame) * 0.01)
ninetyNinePercentDf = dataFrame.sort_values("price", ascending=False).iloc[131:] # iloc[131:] retrieves all rows from the 131st index onwards.
print(ninetyNinePercentDf)
print(ninetyNinePercentDf.describe)

plt.figure(figsize=(7, 5))
sbn.histplot(ninetyNinePercentDf["price"])
plt.show()

# Prepare the data
dataFrame = dataFrame.drop("transmission", axis=1) # "transmission": Specifies the name of the column to be removed. In this example, the "transmission" column is removed.
print(dataFrame.groupby("year").mean()["price"])
x = dataFrame["price"].values
y = dataFrame.drop("price", axis=1).values
print(x)
print(y)
print(dataFrame[dataFrame.year != 1970].groupby("year").mean()["price"])

# Split the data into training and test sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=10)
len(x_train) # test_size=0.3 sets 30% of the dataset as the test set. Therefore, 70% of the dataset remains as the training set.
len(x_test) # random_state=10 is a seed for the random number generator, ensuring reproducible results.

# Scale the data
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
x_train = x_train.reshape(-1, 1)
x_test = x_test.reshape(-1, 1)
x_train = scaler.fit_transform(x_train) # The fit_transform() method applies the scaler to the training set and transforms it. It calculates the scaling factor based on the training set and uses this factor to transform the training set.
x_test = scaler.transform(x_test) # The transform() method uses the scaling factor calculated from the training set to transform the test set.

# Create and train the neural network model
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

x_train.shape # This line checks the shape of the training dataset, showing the number of training examples and the dimension of features.
model = Sequential()
model.add(Dense(12, activation="relu"))
model.add(Dense(12, activation="relu"))
model.add(Dense(12, activation="relu"))
model.add(Dense(12, activation="relu"))
model.add(Dense(1))
# This part creates an ANN model. The model is defined sequentially. First, a model is created with the Sequential() function. Then, layers are added with the add() method.
# In this example, four hidden layers with 12 neurons each (with ReLU activation function) and one output layer (with a linear activation function) are defined. This creates a fully connected neural network, disregarding the input dimension.
model.compile(optimizer="adam", loss="mse") # The compile() method compiles the model. It specifies the optimizer ("adam") and the loss function (mean squared error - "mse") to be used by the model.
model.fit(x=x_train, y=y_train, validation_data=(x_test, y_test), batch_size=250, epochs=300) # The batch size is set to 250, and the training is performed over 300 epochs.

# Evaluate the model's performance
from sklearn.metrics import mean_squared_error, mean_absolute_error
tahminDizisi = model.predict(x_test) # This line calculates the predictions of the model on the test set. The predict() method makes predictions on the input data using the model.
print(tahminDizisi)
y_test = np.arange(0, len(y_test), 1)

# Visualize the predictions
plt.scatter(y_test, tahminDizisi)
plt.plot(y_test, y_test, linestyle="-", marker="o", color="g")
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual Values vs. Predicted Values")
plt.show()
