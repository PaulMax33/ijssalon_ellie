# In 'presentatie.py'

def presenteer(mijn_dict, totaal):
    for item, prijs in mijn_dict.items():
        print(f"{item} : {prijs} euro")
    
    print("==========================")
    print(f"totaal : {totaal} euro")

