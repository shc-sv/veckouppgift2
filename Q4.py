# Veckouppgift 2

# Q4: Temperaturomvandling

def temperaturomvandling():
    # Version 1
    c = input("Skriv in en temperatur i grader Celsius: ")
    c = float(c)
    f = round(1.8 * c + 32, 1)
    print(f"Det blir {f} grader Fahrenheit.")

    # Version 2
    choice = input("Vill du ange temperaturen i Celsius (C) eller Fahrenheit (F). Ange C eller F här: ")
    choice = choice.upper()
    if choice == 'C':
        c = input(f"Skriv in en temperatur i grader Celsius: ")
        c = float(c)
        f = round(1.8 * c + 32, 1)
        print(f"Det blir {f} grader Fahrenheit.")
    elif choice == 'F':
        f = input(f"Skriv in en temperatur i grader Fahrenheit: ")
        f = float(f)
        c = round((f - 32) / 1.8, 1)
        print(f"Det blir {c} grader Celsius.")
    else:
        print("Tyvärr, felinmatning! Du kan bara välja mellan Celsius (C) och Fahrenheit (F).")

    # Version 3
    if c < 10:
        print("Se till att ha vinterkläder på dig, temperaturen är låg idag.")
    elif c >= 20:
        print("Det är dags att packa badkläder – solen väntar!")
