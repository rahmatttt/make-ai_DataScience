# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 19:48:36 2019

@author: Rahmat Hendrawan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#create random data

df = pd.DataFrame(np.random.randn(50,4), columns=['A','B','C','D'])

df.plot()
plt.show()

# %matplotlib qt supaya grafiknya muncul di window baru
