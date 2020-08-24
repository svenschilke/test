import numpy as np
import pandas as pd
import os

import matplotlib. pyplot as plt
signal = np.sin(np.linspace(1,20,100))

plt.plot(signal)

if max(signal) > 10:
    print("Hooray")
else:
    print("non horray")