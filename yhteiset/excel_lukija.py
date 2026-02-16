import pandas as pd

def lue_excel(polku):
    df = pd.read_excel(polku, engine="openpyxl")
    return df
