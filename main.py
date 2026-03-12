"""projekt_4.py: Čtvrtý projekt do Engeto Online Tester s Pythonem

author: Vítězslav Dlábek
email: vitezslavdlabek@gmail.com
"""


ukoly = []
def hlavni_menu(): #vizualizace základního rozhraní pro další využití programu.
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
        else:
            print("Neplatný vstup")
        
def pridat_ukol(): #Funkce přidá úkol na seznam úkolu na základě uživatelem navoleného názvu a popisu úkolu. V případě neplatných hodnot uživatele upozorní.
    while True:
        nazev = input("\nZadejte název úkolu nebo zadejte 'zpět' pro návrat: ")
        if nazev == "zpět":
            return
        while len(nazev) == 0:
            print("\nNezadali jste název úkolu.")
            nazev = input("\nZadejte název úkolu nebo zadejte 'zpět' pro návrat: ")
            if nazev == "zpět":
                return
        while len(nazev) > 50:
            print("Maximalní délka názvu je 50 znaků")
            nazev = input("\nZadejte název úkolu nebo zadejte 'zpět' pro návrat: ")
            if nazev == "zpět":
                return
        popis = input("\nZadejte popis úkolu nebo zadejte 'zpět' pro návrat: ")
        if popis == "zpět":
                return
        while len(popis) == 0:
            print("\nNezadali jste popis úkolu.")
            popis = input("\nZadejte popis úkolu nebo zadejte 'zpět' pro návrat: ")
            if popis == "zpět":
                return
        else:
            ukoly.append(nazev + " - " + popis)
            print(f"Úkol '{nazev}' byl přidán.")
            return

def zobrazit_ukoly(): #Funkce pro vyobrazení aktuálního seznamu úkolů
        if len(ukoly) == 0:
            print("\nSeznam úkolů je prázdný")
        else:
            print("\nSeznam úkolů:")
            for x in ukoly:
                print(f'{ukoly.index(x)+1}. {x}')

def odstranit_ukol(): #Funkce umožnuje uživateli smazat jim výbraný úkol ze seznamu úkolu.
    if len(ukoly) == 0:
            print("\nSeznam úkolů je prázdný")
    else:
        while True:
            try:
                zobrazit_ukoly()
                odstraneni = input("\nZadejte číslo úkolu, který chcete odstranit nebo zadejte 'zpět' pro návrat: ")
                if odstraneni == "zpět":
                    return
                elif len(odstraneni) == 0:
                        print("\nNebylo zadáno žádné číslo úkolu.")
                elif not odstraneni.isnumeric():
                    print("\nZadaná hodnota není číslo.")
                elif odstraneni == "0":
                     print("\nÚkol číslo '0' neexistuje")
                else: 
                    print(f"\nÚkol '{ukoly[int(odstraneni) - 1].split("-")[0]}' byl odstraněn.")
                    ukoly.pop(int(odstraneni) - 1)
                    return
            except IndexError:
                print(f"\nÚkol číslo '{odstraneni}' neexistuje.")
    
hlavni_menu()