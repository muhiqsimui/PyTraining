

import pandas as pd
import numpy as np

dataset=pd.read_csv('sample_data/birth-jakarta.csv')
dataset.to_csv('databirth.csv',index=False)
dataset.head()

dataset.tail()

pd.read_csv('databirth.csv')

datahtml=pd.read_html('https://en.wikipedia.org/wiki/Indonesia')

type(datahtml)

datahtml
