import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("data/train.csv")

print(data.sort_values(by="SalePrice", ascending=False).head(1))


