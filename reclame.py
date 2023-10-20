# Aanbieding 

def aanbieding_1(smaak, prijs, korting):
    # Bereken de nieuwe prijs na korting
    nieuwe_prijs = prijs * (1 - korting)
    
    # Genereer de tekst met de aanbieding
    aanbieding_tekst = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs:.2f} euro voor {nieuwe_prijs:.2f} euro."
    
    return aanbieding_tekst

smaak = "aardbei"
prijs = 4
korting = 0.1

resultaat = aanbieding_1(smaak, prijs, korting)
print(resultaat)

# Totale inkomsten deze week

def inkomsten_totaal(inkomsten_per_dag, btw):
    # Bereken het totaal van de inkomsten
    totaal_inkomsten = sum(inkomsten_per_dag)
    
    # Bereken het bedrag aan btw
    btw_bedrag = totaal_inkomsten * btw
    
    # Genereer de tekst met het totaal en het btw-bedrag
    resultaat_tekst = f"Het totaal van alle inkomsten van deze week is {totaal_inkomsten:.2f} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden."
    
    return resultaat_tekst

inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
btw = 0.09

resultaat = inkomsten_totaal(inkomsten_per_dag, btw)
print(resultaat)

# Laagste en hoogste waarde inkomsten per dag

def laag_en_hoog(mijn_lijst):
    # Gebruik functies 'min' en 'max' om de laagste en hoogste waarde te vinden
    laagste_waarde = min(mijn_lijst)
    hoogste_waarde = max(mijn_lijst)
    
    # Maak een lijst met de laagste en hoogste waarden
    resultaat_lijst = [laagste_waarde, hoogste_waarde]
    
    return resultaat_lijst

inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]

resultaat = laag_en_hoog(inkomsten_per_dag)
print("Laagste en hoogste inkomsten van deze week:", resultaat)

# Gemiddelde inkomsten deze week

def gemiddelde(mijn_lijst):
    # Gebruik de ingebouwde functie 'sum' om de som van de waarden in de lijst te berekenen
    totaal = sum(mijn_lijst)
    
    # Bereken het gemiddelde door de som te delen door het aantal waarden in de lijst
    gemiddelde_inkomsten = totaal / len(mijn_lijst)
    
    # Genereer de tekst met het gemiddelde bedrag
    resultaat_tekst = f"De gemiddelde inkomsten deze week zijn {gemiddelde_inkomsten:.2f} euro."
    
    return resultaat_tekst

inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]

resultaat = gemiddelde(inkomsten_per_dag)
print(resultaat)

# Meervoudig

def meervoudig(invoer_lijst):
    if len(invoer_lijst) < 5 or len(invoer_lijst) > 10:
        return []  # Lege lijst retourneren als de lengte van de invoerlijst niet binnen het vereiste bereik valt

    # Gebruik de functie laag_en_hoog om de laagste en hoogste waarden te vinden
    hoogste, laagste = laag_en_hoog(invoer_lijst)

    # Maak een lijst met de hoogste en laagste waarden
    resultaat_lijst = [hoogste, laagste]

    return resultaat_lijst

invoer_lijst = [10, 5, 3, 2, 1, 2, 9]

resultaat = meervoudig(invoer_lijst)
print("Laagste en hoogste waarden:", resultaat)

# In 'reclame.py'

from aanbieding import mijn_functie_2  # Importeer mijn_functie_2 uit 'aanbieding.py'
from reclame import meervoudig  # Importeer de eerder gedefinieerde meervoudig functie

def combinatie(invoer_lijst_2):
    # Roep de functie meervoudig aan met de gegeven lijst
    korte_lijst = meervoudig(invoer_lijst_2)

    # Roep mijn_functie_2 aan met de korte lijst en retourneer het resultaat
    resultaat = mijn_functie_2(korte_lijst)

    return resultaat
