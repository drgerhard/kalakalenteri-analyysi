import pandas as pd

def lue_excel(polku):
    try:
        df = pd.read_excel(polku, engine="openpyxl")
        return df

    except FileNotFoundError:
        raise FileNotFoundError(f"Excel-tiedostoa ei löytynyt: {polku}")

    except PermissionError:
        raise PermissionError(f"Ei oikeutta lukea tiedostoa: {polku}")

    except ValueError as e:
        raise ValueError(f"Virheellinen Excel-muoto: {e}")

    except Exception as e:
        raise Exception(f"Tuntematon virhe Excelin lukemisessa: {e}")