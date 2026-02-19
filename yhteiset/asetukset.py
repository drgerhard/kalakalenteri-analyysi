from pathlib import Path


PROJEKTI_JUURI = Path(__file__).resolve().parent.parent


EXCEL_POLKU = PROJEKTI_JUURI / "data" / "Kalakalenteri.xlsx"
RAPORTTI_KANSIO = PROJEKTI_JUURI / "raportti"
RAPORTTI_TIEDOSTO = RAPORTTI_KANSIO / "analyysi_raportti.txt"


RAPORTTI_KANSIO.mkdir(parents=True, exist_ok=True)