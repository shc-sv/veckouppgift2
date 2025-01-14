from Q2 import q2

def print_hi(name):
    print(f'Hej, {name}!')  # Press Ctrl+F8 to toggle the breakpoint.

# Q1
# Skriptet gör: Interaktion med användare, rabbatberäkning och resultat(respons)
def q1():
    is_member = False
    level1 = 100
    level2 = 300
    discount = 0

    price = input("Välkomen, köp något dyrt? Skriv in ord. priset här: ")
    price = float(price)

    # 1) Eftersom priset som är högre än level2 är självklart högre än level1,
    #    måste vi ändra if-sats för att säkerställa att vi inte tillämpar flera rabbater samtidigt.
    '''     
    if price > level1:
        print("Grattis! Du har avancerat till nivå 1 och får 10% rabbat. ")
        discount = discount + 10
    if price > level2:
        print("Grattis! Du har avancerat till nivå 2 och får 25% rabbat. ")
        discount = discount + 25
    '''
    if price > level1:
        if price >= level2:
            print("Grattis! Du har avancerat till nivå 2 och får 25% rabbat. ")
            discount = discount + 25
        else:
            print("Grattis! Du har avancerat till nivå 1 och får 10% rabbat. ")
            discount = discount + 10

    final_price = price * (100 - discount) / 100

    # 2) Omvandla float till sträng
    print("Efter rabbater blir priset... " + str(final_price))

if __name__ == '__main__':
    print_hi('kära kund')
    print("")
    print("Q1:")
    q1()
    print("")
    print("Q2:")
    q2()
    print("")
    print("Q3:")




