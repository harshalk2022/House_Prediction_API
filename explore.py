from sklearn.datasets import fetch_california_housing
import pandas as pd 


data = fetch_california_housing()

df = pd.DataFrame(data.data, columns=data.feature_names)

df["Price"] = data.target
print("Shape", df.shape)
print("="*50)
print(df.head())
print("="*50)
print(df.describe())