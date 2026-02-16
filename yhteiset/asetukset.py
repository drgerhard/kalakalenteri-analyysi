import os

# Haetaan kansion sijainti
PROJEKTI_JUURI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Polut tiedostoihin
EXCEL_POLKU = os.path.join(PROJEKTI_JUURI, "data", "kalakalenteri.xlsx")
# Luodaan raportti-kansio, jos sitä ei ole, ja tallennetaan sinne txt-tiedosto
RAPORTTI_POLKU = os.path.join(PROJEKTI_JUURI, "raportti", "analyysi_raportti.txt")