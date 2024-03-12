from datetime import datetime
import MetaTrader5 as mt5
import pytz
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

if not mt5.initialize():
    print("initialize() failed")
    mt5.shutdown()

print(mt5.terminal_info())
# get data on MetaTrader 5 version
print(mt5.version())

timezone = pytz.timezone("Etc/UTC")
utc_from = datetime(year=2024, month=3, day=11, tzinfo=timezone)
euraud_ticks = mt5.copy_ticks_from("EURAUD", utc_from, 1000, mt5.COPY_TICKS_ALL)
print(euraud_ticks)

mt5.shutdown()

# DATA
print("euraud_ticks(", len(euraud_ticks), ")")
for val in euraud_ticks[:10]:
    print(val)

# PLOT
# create DataFrame out of the obtained data
ticks_frame = pd.DataFrame(euraud_ticks)
# convert time in seconds into the datetime format
ticks_frame["time"] = pd.to_datetime(ticks_frame["time"], unit="s")
# display ticks on the chart
plt.plot(ticks_frame["time"], ticks_frame["ask"], "r-", label="ask")
plt.plot(ticks_frame["time"], ticks_frame["bid"], "b-", label="bid")

# display the legends
plt.legend(loc="upper left")

# add the header
plt.title("EURAUD ticks")

# display the chart
plt.show()
