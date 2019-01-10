#Research of BTC-USD tendency during the last 2 years

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

btc = pd.read_csv("BTC_USD Bitfinex Historical Data", index_col = 0, parse_dates = True)
btc_price = btc["Price"]
fig = plt.figure(figsize = (16, 8))
subfig = fig.add_subplot(1, 1, 1)
subfig.set_ylabel("Price", fontsize=20)
subfig.set_xlabel("Date", fontsize=20)
btc_price.plot(ax = subfig)
subfig.add_title("BTC-USD", fontsize=30)
fig.savefig("BTC-USD (2017-2018).png")
