import pandas as pd  # TÄMÄ PUUTTUI

def laske_kaikki_keskiarvot(df):
    # Nyt 'pd' on määritelty ja tämä rivi toimii:
    df["Arvosana"] = pd.to_numeric(df["Arvosana"], errors='coerce')
    
    tulokset = {}
    sarakkeet = ["Pilvinen", "Satoiko", "Uittotyyli", "Kuun 1-8 vaiheet", "Tuulen suunta"]
    
    for sarake in sarakkeet:
        if sarake in df.columns:
            tulokset[sarake] = df.groupby(sarake)["Arvosana"].mean()
            
    return tulokset