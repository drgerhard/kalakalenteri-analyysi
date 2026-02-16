import pandas as pd

def laske_perustilastot(df):
    tulos = {}
    
    # Pakotetaan numeeriset sarakkeet numeroiksi (virheet -> NaN)
    # Tämä estää aiemman 'datetime' -virheen
    arvosanat = pd.to_numeric(df["Arvosana"], errors='coerce')
    paineet = pd.to_numeric(df["Ilmanpaine"], errors='coerce')
    ajat = pd.to_numeric(df["Kalastus aika"], errors='coerce')

    tulos["paivien_maara"] = len(df)
    tulos["keskiarvo"] = arvosanat.mean()
    tulos["paine_keskiarvo"] = paineet.mean()
    tulos["aika_yhteensa"] = ajat.sum()
    tulos["paras"] = arvosanat.max()

    return tulos