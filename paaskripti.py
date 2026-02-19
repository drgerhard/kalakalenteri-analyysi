import sys
from yhteiset.asetukset import EXCEL_POLKU, RAPORTTI_TIEDOSTO
from yhteiset.excel_lukija import lue_excel
from analyysi.tilastot import laske_perustilastot
from analyysi.suodatus import laske_kaikki_keskiarvot

def aja_analyysi():
    print(f"Luetaan tiedostoa: {EXCEL_POLKU}")
    
    try:
        
        data = lue_excel(EXCEL_POLKU)
        
        
        stats = laske_perustilastot(data)
        ryhmat = laske_kaikki_keskiarvot(data)

        
        with open(RAPORTTI_TIEDOSTO, "w", encoding="utf-8") as f:
            f.write("LAAJENNETTU KALAKALENTERI-ANALYYSI\n")
            f.write("==================================\n\n")
            f.write(f"Reissuja: {stats.get('paivien_maara', 0)}\n")
            f.write(f"Arvosana ka: {stats.get('keskiarvo', 0):.2f}\n")
            f.write(f"Ilmanpaine ka: {stats.get('paine_keskiarvo', 0):.1f}\n")
            f.write(f"Kalastusaika yhteensä: {stats.get('aika_yhteensa', 0)} h\n\n")

            for otsikko, tiedot in ryhmat.items():
                f.write(f"--- Keskiarvot: {otsikko} ---\n")
                for kategoria, arvo in tiedot.items():
                    f.write(f"  {kategoria}: {arvo:.2f}\n")
                f.write("\n")
        
        print(f"Analyysi valmis! Raportti löytyy: {RAPORTTI_TIEDOSTO}")

    except FileNotFoundError:
        print(f"VIRHE: Tiedostoa ei löytynyt polusta: {EXCEL_POLKU}")
    except Exception as e:
        print(f"Tapahtui odottamaton virhe: {e}")

if __name__ == "__main__":
    aja_analyysi()
