import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
import pickle
from UrlFeaturizer import UrlFeaturizer

os.chdir("../")
os.chdir("D://SPKT//Năm 4//HK 1//Tiểu luận chuyên ngành - CNPM//Virtual assistant//Deep learning//URL Feature Engineering and Classification//Models//")
import warnings
warnings.filterwarnings("ignore")

order = ['bodyLength', 'bscr', 'dse', 'dsr', 'entropy', 'hasHttp', 'hasHttps',
       'has_ip', 'numDigits', 'numImages', 'numLinks', 'numParams',
       'numTitles', 'num_%20', 'num_@', 'sbr', 'scriptLength', 'specialChars',
       'sscr', 'urlIsLive', 'urlLength']
def main(url):
	a = UrlFeaturizer(url).run()
	test = []
	for i in order:
		test.append(a[i])
	encoder = LabelEncoder()
	encoder.classes_ = np.load('NN_lblenc.npy',allow_pickle=True)
	scalerfile = 'NN_scaler.sav'
	scaler = pickle.load(open(scalerfile, 'rb'))
	model = load_model("NN.h5")#
	test = pd.DataFrame(test).replace(True,1).replace(False,0).to_numpy().reshape(1,-1)
	predicted = np.argmax(model.predict(scaler.transform(test)),axis=1)
	print(url + " là trang web " + encoder.inverse_transform(predicted)[0])


if __name__ == '__main__':
	main('https://online.hcmute.edu.vn')