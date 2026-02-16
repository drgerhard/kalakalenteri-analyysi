from yhteiset.asetukset import EXCEL_POLKU, RAPORTTI_POLKU
from yhteiset.excel_lukija import lue_excel
from analyysi.tilastot import laske_perustilastot
from analyysi.suodatus import laske_kaikki_keskiarvot

def main():
    df = lue_excel(EXCEL_POLKU)
    stats = laske_perustilastot(df)
    ryhmat = laske_kaikki_keskiarvot(df)

    with open(RAPORTTI_POLKU, "w", encoding="utf-8") as f:
        f.write("LAAJENNETTU KALAKALENTERI-ANALYYSI\n")
        f.write("==================================\n\n")
        
        f.write(f"Reissuja: {stats['paivien_maara']}\n")
        f.write(f"Arvosana ka: {stats['keskiarvo']:.2f}\n")
        f.write(f"Ilmanpaine ka: {stats['paine_keskiarvo']:.1f}\n")
        f.write(f"Kalastusaika yhteensä: {stats['aika_yhteensa']} h\n\n")

        for otsikko, tiedot in ryhmat.items():
            f.write(f"--- Keskiarvot: {otsikko} ---\n")
            for kategoria, arvo in tiedot.items():
                f.write(f"  {kategoria}: {arvo:.2f}\n")
            f.write("\n")

if __name__ == "__main__":
    main()