import pandas as pd
import predictor as pr


def transform_port(port):
    df = pd.read_excel("spill_prediction.xlsx", sheet_name="data2loc")
    df.set_index("WILAYAH", inplace=True)
    port_code = df.loc[port.upper(), "KODE"]
    return port_code


def days_to_hour(days):
    return days * 24


def predict_fresh_water(port1, port2, durr):
    feature = ["AWAL", "AKHIR", "DURASI"]
    port1 = transform_port(port1)
    port2 = transform_port(port2)
    durr = days_to_hour(durr)
    predict_feature = pd.DataFrame(data=[[port1, port2, durr]], columns=feature)
    result = pr.model.predict(predict_feature)
    return result
