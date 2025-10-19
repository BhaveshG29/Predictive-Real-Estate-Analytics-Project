import pandas as pd

train_data = pd.read_csv("data/train.csv")
train_data.index = train_data["Id"]

print(train_data[(train_data["SalePrice"]>200000) & (train_data["SaleCondition"]=='Normal') & (train_data["YrSold"]>=2010)][["YrSold", "SaleCondition", "SalePrice"]])

