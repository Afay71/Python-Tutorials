# -*- coding: utf-8 -*-
from lib2to3.pgen2.pgen import DFAState
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn
import tensorflow

# Load the dataset
df = pd.read_excel("C:\\Users\\Arif Furkan\\OneDrive\\Belgeler\\Python_kullanirken\\maliciousornot.xlsx")
print(df)
print(df.info())
print(df.describe())
print(df.corr()["Type"].sort_values())

# Show the distribution of the dataset
sbn.countplot(x="Type", data=df)
plt.show()

# Visualize the correlation matrix
df.corr()["Type"].sort_values().plot(kind="bar")
plt.show()

# Prepare the data
y = df["Type"].values
x = df.drop("Type", axis=1).values

# Split the data into training and test sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=15)

# Scale the data
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(x_train)
MinMaxScaler(copy=True, feature_range=(0, 1))
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

# Model 1: Without Early Stopping
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping

x_train.shape
model = Sequential()
model.add(Dense(units=30, activation="relu"))
model.add(Dense(units=15, activation="relu"))
model.add(Dense(units=15, activation="relu"))
model.add(Dense(units=1, activation="relu"))
model.compile(loss="binary_crossentropy", optimizer="adam")
model.fit(x=x_train, y=y_train, epochs=700, validation_data=(x_test, y_test), verbose=1)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)  
plt.plot(model.history.history['loss'], label='Training Loss')
plt.plot(model.history.history['val_loss'], label='Validation Loss')
plt.title('Model 1 Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

# Model 2: With Early Stopping
model = Sequential()
model.add(Dense(units=30, activation="relu"))
model.add(Dense(units=15, activation="relu"))
model.add(Dense(units=15, activation="relu"))
model.add(Dense(units=1, activation="relu"))
model.compile(loss="binary_crossentropy", optimizer="adam")
early_stopping = EarlyStopping(monitor="val_loss", mode="min", verbose=1, patience=25)
model.fit(x=x_train, y=y_train, epochs=700, validation_data=(x_test, y_test), verbose=1, callbacks=[early_stopping])

plt.subplot(1, 2, 2)  
plt.plot(model.history.history['loss'], label='Training Loss')
plt.plot(model.history.history['val_loss'], label='Validation Loss')
plt.title('Model 2 Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

# Model 3: With Dropout

model = Sequential()
model.add(Dense(units=30, activation="relu"))
model.add(Dropout(0.6))
model.add(Dense(units=15, activation="relu"))
model.add(Dropout(0.6))
model.add(Dense(units=15, activation="relu"))
model.add(Dropout(0.6))
model.add(Dense(units=1, activation="sigmoid"))
model.compile(loss="binary_crossentropy", optimizer="adam")
model.fit(x=x_train, y=y_train, epochs=700, validation_data=(x_test, y_test), verbose=1)

plt.subplot(1, 3, 3)  
plt.plot(model.history.history['loss'], label='Model 3 Training Loss')
plt.title('Model 3 Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend() 