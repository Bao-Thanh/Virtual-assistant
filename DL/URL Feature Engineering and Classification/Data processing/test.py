# %%
from socket import timeout
import pandas as pd
import tqdm

from UrlFeaturizer import UrlFeaturizer

# %%
df = pd.read_csv('../Dataset/malicious_url_train_dataset.csv')

# %%
emp = UrlFeaturizer('').run().keys()
A = pd.DataFrame(columns=emp)

# %%

url = []
for i in df['url']:
    temp = UrlFeaturizer(i).run()
    url.append(temp)

# %%
