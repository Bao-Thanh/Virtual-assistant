#%%
from statistics import mean
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from cmath import nan
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from tqdm import tqdm
import os
import seaborn as sns
from decimal import Decimal
from sklearn.metrics import accuracy_score, classification_report
from keras import backend as K
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout, Masking, Embedding
from keras.utils import np_utils
from keras.layers import BatchNormalization, SeparableConv2D, MaxPooling2D, Activation, Flatten, Dropout, Dense
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold   
import joblib 

#%%
data = pd.read_csv("../Dataset/data.csv", error_bad_lines=False)
print(data.head())

# %%
data = data.dropna()

# data["strength"] = data["strength"].map({0: "Weak", 
#                                          1: "Medium",
#                                          2: "Strong"})
print(data.sample(5))

# %%
def word(password):
    character=[]
    for i in password:
        character.append(i)
    return character
 
# %%
y = np.array(data["strength"])
data = data.drop(columns="strength")
 
#%%
tdif = TfidfVectorizer(tokenizer=word)
x = np.array(data["password"])
x = tdif.fit_transform(x)


#%%
xtrain, xtest, ytrain, ytest = train_test_split(x, y, 
                                                test_size=0.2, 
                                                random_state=42)
#%%
def r2score_and_rmse(model, train_data, labels): 
    r2score = model.score(train_data, labels)
    from sklearn.metrics import mean_squared_error
    prediction = model.predict(train_data)
    mse = mean_squared_error(labels, prediction)
    rmse = np.sqrt(mse)
    return r2score, rmse      
def store_model(model, model_name = ""):
    # NOTE: sklearn.joblib faster than pickle of Python
    # INFO: can store only ONE object in a file
    if model_name == "": 
        model_name = type(model).__name__
    joblib.dump(model,'../models/' + model_name + '_model.pkl')
def load_model(model_name):
    # Load objects into memory
    #del model
    model = joblib.load('../models/' + model_name + '_model.pkl')
    #print(model)
    return model

#%%
model = RandomForestClassifier() # n_estimators: no. of trees
model.fit(xtrain, ytrain)
# Compute R2 score and root mean squared error
print('\n____________ RandomForestClassifier ____________')
r2score, rmse = r2score_and_rmse(model, xtrain, ytrain)
print('\nR2 score (on training data, best=1):', r2score)
print("Root Mean Square Error: ", rmse.round(decimals=1))
store_model(model)      
# Predict labels for some training instances
#print("Input data: \n", train_set.iloc[0:9])
print("\nPredictions: ", model.predict(xtrain[0:9]).round(decimals=1))
print("Labels:      ", list(ytrain[0:9]))



# %%
print(model.score(xtest, ytest))

# %%
