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
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

#%%
data = pd.read_csv("../Dataset/data.csv", error_bad_lines=False)
print(data.head())

# %%
data = data.dropna()

data["strength"] = data["strength"].map({0: "Weak", 
                                         1: "Medium",
                                         2: "Strong"})
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
model = RandomForestClassifier()
model.fit(xtrain, ytrain)

#%%
pickle.dump(model, open('../models/RandomForestClassifier.pkl', 'wb'))
pickle.dump(tdif, open('../models/tdif.pkl', 'wb'))

#%%
ypred = model.predict(xtest)

# %%
cm = confusion_matrix(ytest,ypred)
print(cm)
print(accuracy_score(ytest,ypred))

# %%
print(classification_report(ytest,ypred))

# %%
model2 = pickle.load(open('../models/RandomForestClassifier.pkl', 'rb'))
tf = pickle.load(open('../models/tdif.pkl', 'rb'))
password = '043779417@Lh'
test = tf.transform([password]).toarray()
output = model2.predict(test)
print(password + ' is ' + output)

# %%
