import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

df = pd.read_excel("spill_prediction.xlsx", sheet_name="main2")

x = ["AWAL", "AKHIR", "DURASI"]
y = "FRESHWATER"

X_train, X_test, y_train, y_test = train_test_split(
    df[x], df[y], test_size=0.3, random_state=42
)

model = xgb.XGBRegressor(objective="reg:squarederror", random_state=42)
model.fit(
    X_train, y_train, eval_set=[(X_train, y_train), (X_test, y_test)], verbose=100
)
