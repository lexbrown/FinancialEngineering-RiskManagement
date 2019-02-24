# Test OLS

import numpy as np #optional
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

raw_set = pd.read_excel('OLS_testset.xlsx')
print(raw_set.describe())

figols =plt.figure(figsize = (10, 5))
subfigols = figols.add_subplot(1,1,1)
dep_v = raw_set['y']
indep_v = raw_set['x']

subfigols.scatter(x = indep_v, y = dep_v)

x_reg = sm.add_constant(indep_v)
results = sm.OLS(dep_v, x_reg).fit()
b0, b1 = results.params

subfigols.plot(indep_v, b0 + b1 * indep_v)

print(results.summary())
