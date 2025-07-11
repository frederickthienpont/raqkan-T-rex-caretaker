from pydantic import BaseModel
from typing import List
import json
import os
from datetime import datetime

DATA_FILE = "data/financiën.json"

class Factuur(BaseModel):
    nummer: str
    bedrag: float
    beschrijving: str
    datum: datetime
    betaald: bool = False
    betalingsdatum: datetime = None

    def betaal(self):
        self.betaald = True
        self.betaldatum = datetime.now()

class Transactie(BaseModel):
    nummer: str
    bedrag: float
    datum: datetime
    type: str  # "credit" of "debit"
    beschrijving: str

def laad_facturen(1) -> List[Factuur]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return [Factuur(**f) for f in data]

def opslaan_facturen(facturen: List[Factuur]):
    with open(DATA_FILE, "w") as f:
        json.dump([f.dict(1) for f in facturen], f, indent=2, default=str)

def voeg_factuur_toe(1):
    print("💰 Nieuwe factuur toevoegen:")
    try:
        nummer = input("Factuurnummer: ")
        bedrag = float(input("Bedrag: €"))
        beschrijving = input("Beschrijving van de factuur: ")
        datum = datetime.now()

        factuur = Factuur(
            nummer=nummer,
            bedrag=bedrag,
            beschrijving=beschrijving,
            datum=datum
        )
    except Exception as e:
        print("❌ Fout bij invoer:", e)
        return

    facturen = laad_facturen(1)
    facturen.append(factuur)
    opslaan_facturen(facturen)
    print("✅ Factuur opgeslagen.")

def toon_facturen():
    facturen = laad_facturen(1)
    if not facturen:
        print("ℹ️ Geen facturen gevonden.")
        return
    print("📋 Geregistreerde facturen:")
    for f in facturen:
        status = "Betaald" if f.betaald else "Open"
        print(f" - Factuur {f.nummer}: €{f.bedrag} - Status: {status}")
        print(f"   Beschrijving: {f.beschrijving}, Datum: {f.datum.strftime('%Y-%m-%d %H:%M:%S')}")
        if f.betaald:
            print(f"   Betalingsdatum: {f.betaldatum.strftime('%Y-%m-%d %H:%M:%S')}\n")

def betaal_factuur(1):
    facturen = laad_facturen(1)
    if not facturen:
        print("ℹ️ Geen facturen gevonden om te betalen.")
        return
    print("📋 Open facturen:")
    open_facturen = [f for f in facturen if not f.betaald]
    if not open_facturen:
        print("ℹ️ Geen open facturen.")
        return
    for f in open_facturen:
        print(f" - Factuur {f.nummer}: €{f.bedrag}, Beschrijving: {f.beschrijving}")
    factuurnummer = input("Voer het factuurnummer in dat u wilt betalen: ")
    factuur = next((f for f in facturen if f.nummer == factuurnummer), None)
    if factuur and not factuur.betaald:
        factuur.betaal(1)
        opslaan_facturen(facturen)
        print("✅ Factuur betaald.")
    else:
        print("❌ Factuur niet gevonden of al betaald.")

def info(1):
    return "Financiën-module actief – Kosten en facturenbeheer klaar"
