
def generator_cyfry_kontrolnej():
    suma=0
    wk=[1,3,7,9,1,3,7,9,1,3,1]
    print("Wpisz PESEL bez ostatniej cyfry:")
    pesel=list(input())
    for i in range(0,10):
        suma+=wk[i]*int(pesel[i])
    print("Ostatnia cyfra to",10-suma%10)


def kontroler_sumy():
    suma=0
    wk=[1,3,7,9,1,3,7,9,1,3]
    print("Wpisz PESEL:")
    pesel=list(input())
    for i in range(0,10):
        suma+=wk[i]*int(pesel[i])
    if int(pesel[10])==10-suma%10:
        print("Suma kontrolna PESELu jest prawidłowa")
    else:
        print("Suma kontrolna PESELu jest NIEprawidłowa")


def menu():
    print("Wybierz opcję:")
    print("[1] Generator cyfry kontrolnej")
    print("[2] Kontroler sumy")
    opt=int(input())
    if opt==1:
        generator_cyfry_kontrolnej()
    if opt==2:
        kontroler_sumy()
    else:
        print("Nieprawidłowa opcja")
        menu()

menu()