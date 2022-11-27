import os
from pandas import pd
import requests
from tqdm import tqdm
from UrlFeaturizer import UrlFeaturizer

# %%

print(os.getcwd())
os.chdir('..\Dataset')

# %%
l = ['DefacementSitesURLFiltered.csv', 'phishing_dataset.csv',
     'Malware_dataset.csv', 'spam_dataset.csv', 'Benign_list_big_final.csv']


emp = UrlFeaturizer("").run().keys()

# %%
A = pd.DataFrame(columns=emp)
t = []
for j in l:
    print(j)
    d = pd.read_csv(j, header=None).to_numpy().flatten()
    for i in tqdm(d):
        try:
            temp = UrlFeaturizer(i).run()
            temp["File"] = j.split(".")[0]
            t.append(temp)
        except requests.Timeout as err:
            pass

# %%
A = A.append(t)
A.to_csv("../Dataset/feature.csv")
