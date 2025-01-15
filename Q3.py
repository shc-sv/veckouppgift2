# Veckouppgift 2

# Q3: Sportresultat
def sport_result():
    print("Matchen är över, nu ska vi räkna ut resultatet!")
    tottenham = input("Hur många mål gjorde Tottenham? ")
    liverpool = input("Hur många mål gjorde Liverpool? ")
    tottenham = int(tottenham)
    liverpool = int(liverpool)

    # Version 2 and version 3
    if tottenham == liverpool:
        print("De blev oavgjort.")
    else:
        if tottenham > liverpool:
            goal_difference = tottenham - liverpool
            print(f"Tottenham vann med {goal_difference} mål!")
        else:
            goal_difference = liverpool - tottenham
            print(f"Liverpool vann med {goal_difference} mål!")
    