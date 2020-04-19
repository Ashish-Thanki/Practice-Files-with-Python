"""download the latest pandas-datareader using pip install before you continue"""

import pandas_datareader as data
import datetime
import matplotlib.pyplot as plt

Symbols = ["TSLA", "F", "TM", "RACE"]
start = datetime.datetime(2020, 2,1)
end = datetime.datetime(2020, 4, 2 )

cars_df = data.DataReader(Symbols, "stooq", start=start, end=end)["Close"]
print(cars_df)
returns = cars_df.pct_+change()
graph = plt.scatter(returns.TSLA, returns.TM)
plt.show()
plt.scatter(returns.mean(), returns.std())
plt.xlabel("Expected Returns")
plt.ylabel("Standard deviation")

for label, x,y in zip(returns.columns, returns.mean(), returns.std()):
    plt.annotate(label,
                 xy = (x, y), xytext = (100,-100),
    textcoords = "offset points", ha = "right", va = "bottom",
                 bbox = dict(boxstyle = "round,pad=0.1", fc = "yellow", alpha =0.9),
                 arrowprops = dict(arrowstyle = '->', connectionstyle ="arc,rad=0"))
    plt.show()
