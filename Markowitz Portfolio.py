#Markovitz Portfolio

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mp_set = pd.read_excel('Markowitz Portfolio - 2.xlsx', sheet_name = 'daily return')
mp_cov = np.cov(mp_set[['Аэрофлот','Яндекс','Сбербанк','НЛМК','Лукойл']], rowvar = False)
mp_covx2 = 2 * mp_cov

temp_mtx = np.linalg.inv(mp_covx2)