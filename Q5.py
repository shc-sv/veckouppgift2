# Veckouppgift 2

# Q5: Miniräknare

def calculator():
    input_data = input("Ange tre tal, separerade med mellanslag här: ")

    # split(): delar upp strängen i en lista baserat på mellanslag
    # map(): konvertera varje del till ett flyttal
    num1, num2, num3 = map(int, input_data.split())

    # 1): Summan av tre tal
    summa = num1 + num2 +num3
    print(f"Summan av {num1}, {num2} och {num3} blir {summa}.")

    # 3): Två lika? Tre lika?
    # Här nedan hanterar vi lika-fall, antingen två lika eller 3 lika
    if num1 == num2 == num3:
        print("Alla tre talen är lika!")
        print(f"Det mellersta talet är {num1}.")
    elif (num1 == num2) and (num2 != num3):
        print(f"De två första talen är lika!")
        print("Det mellersta talet ska inte räknas ut!")
    elif (num1 == num3) and (num1 != num2):
        print("Det första och tredje talet är lika!")
        print("Det mellersta talet ska inte räknas ut!")
    elif (num2 == num3) and (num1 != num2):
        print("De två sista talen är lika!")
        print("Det mellersta talet ska inte räknas ut!")
    else:
        # 2): Vilket är det största tal?
        # 4): Vilket är det mellersta tal?
        # Här nedan hanterar vi inget lika-fall.
        print("Inga tal är lika!")
        # num1, num2, num3 eller num1, num3, num2
        if num1 > num2 > num3:
            print(f'Det första talet {num1} är det största talet. Det andra talet {num2} är det mellersta talet.')
        elif num1 > num3 > num2 :
            print(f'Det första talet {num1} är det största talet. Det tredje talet {num3} är det mellersta talet.')

        # num2, num1, num3 eller num2, num3, num1
        if num2 > num1 > num3:
            print(f'Det andra talet {num2} är det största talet. Det första talet {num1} är det mellersta talet.')
        elif num2 > num3 > num1:
            print(f'Det andra talet {num2} är det största talet. Det tredje talet {num3} är det mellersta talet.')

        # num3, num2, num1 eller num3, num1, num2
        if num3 > num2 > num1:
            print(f'Det tredje talet {num3} är det största talet. Det andra talet {num2} är det mellersta talet.')
        elif num3 > num1 > num2:
            print(f'Det tredje talet {num3} är det största talet. Det första talet {num1} är det mellersta talet.')




