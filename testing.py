import numpy as np
import pandas as pd
import os

import matplotlib. pyplot as plt
signal = np.sin(np.linspace(1,20,100))

plt.plot(signal)

def hooray(sig):
    phrase = "Nix Hooray"
    if max(sig) > .1:
        phrase = "Hooray"
    return phrase

hooray(signal)