# Veckouppgift 2

# Q2: Balder
'''
•	Varför just tre värden?
Tre värden handlar om att kontrollera både om längden är större än 130 cm, mindre än 130 cm, och att säkerställa att exakt 130 cm hanteras korrekt.
•	Varför dessa värden?
130 cm är en vanlig standard, men kan givetvis variera beroende på sammanhanget.
•	Skulle det vara bra att lägga till testvärdet 129 cm?
129 cm är ett bra testvärde för att bekräfta att programmet korrekt identifierar gränsvärdet.
'''

def balder():
    height = input("Hur lång är du? Ange här (i cm): ")
    height = int(height)
    if height >= 130:
        print("Du får åka!")
    else:
        print("Du får inte åka!")