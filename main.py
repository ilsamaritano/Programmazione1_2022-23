# Script di test Assegnamento 1 622AA 2022/23 (non modificare)
from testMy import *
from biblio import *

def test_finale():
    #contiamo i test falliti
    testFalliti=0
    print("==========> Inizio nuovo test <=============\n\n")
    # creo un catalogo
    c = []

    # test inserimento e serializza
    print("==========> Test inserimento e serializza")
    #
    testFalliti += testEqual(inserisci(c, "Dexter", "Colin", "Il mondo silenzioso di Nicholas Quinn", 2012, ("G", 15)),True)
    a = serializza(c)
    print(a)
    #
    testFalliti += testEqual(inserisci(c,"Adams", "Douglas", "Guida galattica per gli autostoppisti",1980,("F",212),"Traduzione Laura Serra. "), True)
    a = serializza(c)
    print(a)
    #
    testFalliti += testEqual(inserisci(c,"Dexter", "Colin","L'ultima corsa per Woodstock", 2010, ("G",14)), True)
    a = serializza(c)
    print(a)
    #
    testFalliti += testEqual(inserisci(c,"Dexter", "Colin","Niente vacanze per l'ispettore Morse", 2012, ("G",16)), True)
    a = serializza(c)
    print(a)
    #
    testFalliti += testEqual(inserisci(c, "Simenon", "Georges", "Gli intrusi", 2015, ("T", 33), "Donazione Giachi"),True)
    a = serializza(c)
    print(a)
    #
    testFalliti += testEqual(inserisci(c,1.23, "Georges", "Gli intrusi", 2015, ("T", 33)), False)
    #
    b = serializza(c)
    if (a != b):
        testFalliti +=1

    # test cerca
    print("==========> Test cerca")
    testFalliti +=testEqual(cerca(c,"intrusi"),True)
    testFalliti += testEqual(cerca(c, "autostoppisti"), True)
    testFalliti +=testEqual(cerca(c, "sss"),False)

    # test crea_copia
    print("==========> Test crea copia ")
    b = crea_copia(c)
    for i in range(len(b)):
        if c[i] != b[i]:
            print("Indice i =",i," c[i] e b[i] non sono uguali")
            testFalliti +=1
            break
    c1= serializza(c)
    b1 = serializza(b)
    testFalliti += testEqual((c1 == b1),True)


    # test sono_uguali
    print("""==========> Test sono_uguali """)
    testFalliti +=testEqual(sono_uguali(c,b),True)
    inserisci(b,"Dexter","Colin","Le figlie di Caino",2017,("G",22), "Copia danneggiata. ")
    print(serializza(b))
    testFalliti += testEqual(sono_uguali(c, b), False)

    # test concatena
    print("""==========> Test concatena """)
    inserisci(c, "Dexter", "Colin", "Le figlie di Caino", 2017, ("G", 22), "In prestito biblioteca Lazzerini. ")
    print(serializza(c))
    d = concatena(c,b)
    print(serializza(d))
    testFalliti +=testEqual(cerca(d,"Caino"),True)
    testFalliti += testEqual(cerca(d, "caino"), True)
    testFalliti += testEqual(cerca(d, "Assenzio"), False)

    #test cancella
    print("""==========> Test cancella """)
    testFalliti +=testEqual(cancella(d,"le figlie di caino"), 1)
    testFalliti += testEqual(cancella(d, "Guerra e Pace"), 0)
    testFalliti += testEqual(cerca(d, "caino"), False)

    #test ordina
    d = concatena(b, c)
    ordina(d)
    print(serializza(d))
    # controllo ordinamento
    for i in range(len(d)-1):
        if d[i][0].lower() > d[i+1][0].lower():
            testFalliti+=1

    # abbiamo finito ?
    if testFalliti == 0:
        print("\t****Test completati -- effettuare la consegna come da README")
    else:
        print("Test falliti: ",testFalliti)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_finale()
