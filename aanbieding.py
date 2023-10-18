# Gebruik de functie 1
def mijn_functie_1(input):
    # Definieer een dictionary
    argumenten = {
        2: 4,
        4: 16,
        10: 100,
        12: 144
    }
    
    # Probeer input op te zoeken in de dictionary en geef de bijbehorende waarde terug
    if input in argumenten:
        return argumenten [input]
    else:
        return None  # Als het argument niet in de tabel voorkomt
    
# Gebruik de functie 2
resultaat = mijn_functie_1(2)
print(resultaat)

def mijn_functie_2(input):
    # Definieer een dictionary
    argumenten = {
       12.3: [15, 9, 36, 4],
       12.2: [14, 10, 24, 6],
       10.5: [15, 5, 50, 2],
       100.20: [120, 80, 2000, 5]
    }
    
    # Probeer input op te zoeken in de dictionary en geef de bijbehorende waarde terug
    if input in argumenten:
        return argumenten [input]
    else:
        return None  # Als het argument niet in de tabel voorkomt
    
# Gebruik de functie
resultaat = mijn_functie_2(12.3)
print(resultaat)