#Research of BTC-USD tendency during the last 2 years

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

btc = pd.read_excel("BTC_USD 2012-2019 - final dataset.xlsx", index_col = 0, parse_dates = True)
btc_price = btc["Price"]
fig = plt.figure(figsize = (12, 8))
subfig = fig.add_subplot(1, 1, 1)
subfig.set_ylabel("Price", fontsize=20)
subfig.set_xlabel("Date", fontsize=20)
btc_price.plot(ax = subfig, color = "b", label = 'BTC-USD')
btc_price.rolling(window = 60).mean().plot(ax = subfig, label = "MA (60)", color = "r", linestyle = "-." )
btc_price.ewm(span = 360).mean().plot(ax = subfig, label = "EWMA (3600)", color = "g", linestyle = "--" )
subfig.set_title("BTC-USD", fontsize=30)
subfig.legend(loc = "best")
fig.savefig("BTC-USD (2012-2019).png")