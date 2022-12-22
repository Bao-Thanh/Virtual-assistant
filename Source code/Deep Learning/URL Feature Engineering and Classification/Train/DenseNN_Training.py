# %%
# Import các thư viện
from cmath import nan
import pickle
from socket import timeout
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from tqdm import tqdm
import asyncio
from async_timeout import timeout
import os
import seaborn as sns
from decimal import Decimal
from sklearn.metrics import accuracy_score, classification_report
from keras import backend as K
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout, Masking, Embedding
from keras.utils import np_utils

# %%
df = pd.read_csv('../Dataset/feature.csv')


# %% Interview dữ liệu
print('\n____________ Dataset info ____________')
print(df.info())

# %%
print('\n____________ Counts on File feature ____________')
print(df['File'].value_counts())


'''Data visualization: trực quan hóa dữ liệu'''

# %%
df.drop(columns='Unnamed: 0', inplace=True)
df.replace(True, 1, inplace=True)
df.replace(False, 0, inplace=True)

# %%
y = df["File"].copy()
df = df.drop(columns="File")


# %%
encoder = LabelEncoder()
Y = encoder.fit_transform(y)

# %%
scaler = MinMaxScaler(feature_range=(0, 1))
X = scaler.fit_transform(df)
X = pd.DataFrame(X)

# %%


def recall_m(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall


def precision_m(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision


def f1_m(y_true, y_pred):
    precision = precision_m(y_true, y_pred)
    recall = recall_m(y_true, y_pred)
    return 2*((precision*recall)/(precision+recall+K.epsilon()))


'''Keras Sequential Model'''
# %%


input_dim = len(df.columns)
model = Sequential()
model.add(Dense(256, input_dim=input_dim, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(5, activation='softmax'))

# %%
model.compile(loss='categorical_crossentropy', optimizer='adam',
              metrics=['accuracy', f1_m, precision_m, recall_m])

# %%
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.25, random_state=42)

# %%
model.fit(X_train, np_utils.to_categorical(y_train),
          epochs=50, validation_split=0.3, batch_size=128)

# %%
y_pred = model.predict(X_test)

# %%
predicted = np.argmax(y_pred, axis=1)

# %%
print(accuracy_score(y_test, predicted))

# %%
target_names = ['Benign', 'Defacement', 'Malware', 'Phishing', 'Spam']
print(classification_report(y_test, predicted, target_names=target_names))

# %%
model.save("../Models/DenseNN.h5")
np.save('../Models/DenseNN_lblenc.npy', encoder.classes_)
scalerfile = '../Models/DenseNN_scaler.sav'
pickle.dump(scaler, open(scalerfile, 'wb'))