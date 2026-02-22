"""projekt_4.py: Čtvrtý projekt do Engeto Online Tester s Pythonem

author: Vítězslav Dlábek
email: vitezslavdlabek@gmail.com
"""


ukoly = []
def hlavni_menu():
    while True:
        print("""
Správce úkolů - Hlavni menu
1. Přidat nový úkol
2. Zobrazit všechny úkoly 
3. Odstranit úkol
4. Konec programu""")
        vyber = input("\nVyberte možnosti (1-4):")
        if vyber == "1":
            pridat_ukol()
        elif vyber == "2":
            zobrazit_ukoly()
        elif vyber == "3":
            odstranit_ukol()
        elif vyber == "4":
            print("\nKonec programu...")
            break
        elif len(vyber) == 0:
            print("\nNebyla vybrána žádná možnost.")
        elif not vyber.isnumeric():
            print("\nZadaná hodnota musí být číslo.")
        elif vyber not in range(1,5):
            print("\nVybraná hodnota musí být v rozmezí 1 - 4.")
def pridat_ukol():
    while True:
        nazev = input("Zadejte název úkolu: ")
        while len(nazev) == 0:
            print("\nNezadali jste název úkolu.")
            nazev = input("Zadejte název úkolu: ")       
        popis = input("Zadejte popis úkolu: ")
        while len(popis) == 0:
            print("\nNezadali jste popis úkolu.")
            popis = input("Zadejte popis úkolu: ")
        else:
            ukoly.append(nazev + " - " + popis)
            print(f"Úkol '{nazev}' byl přidán.")
            break
def zobrazit_ukoly():
        if len(ukoly) == 0:
            print("\nSeznam úkolů je prázdný")
        else:
            print("\nSeznam úkolů:")
            for x in ukoly:
                print(f'{ukoly.index(x)+1}. {x}')
def odstranit_ukol():
    if len(ukoly) == 0:
            print("\nSeznam úkolů je prázdný")
    else:
        while True:
            try:
                odstraneni = input("\nZadejte číslo úkolu, který chcete odstranit: ")
                if len(odstraneni) == 0:
                        print("\nNebylo zadáno žádné číslo úkolu.")
                elif not odstraneni.isnumeric():
                    print("\nZadaná hodnota není číslo.")
                
                else: 
                    print(f"\nÚkol '{ukoly[int(odstraneni) - 1].split("-")[0]}' byl odstraněn.")
                    ukoly.pop(int(odstraneni) - 1)
                    break
            except IndexError:
                print(f"\nÚkol číslo '{odstraneni}' neexistuje.")
    
hlavni_menu()