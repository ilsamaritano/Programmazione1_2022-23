"""
LIBRO -> tupla (cognomeautore, nomeautore, titolo, collocazione, anno, note)
CATALOGO -> lista di tuple separate da \n

"""
from testMy import *


def inserisci(cat, cognome, nome, titolo, anno, collocazione, note=[]):
    if type(cat) != list:
        risposta = None
    elif type(cognome) != str or type(nome) != str or type(titolo) != str:
        risposta = None
    elif type(collocazione[0]) != str and (type(collocazione[1]) and collocazione[1] > 0) != int:
        risposta = None
    elif type(anno) != int and anno >= 0:
        risposta = None
    elif (type(note) != list) and (type(note) != str):
        risposta = None
    else:  # Dopo aver controllato i valori di tutti i campi procedo all'inserimento
        if note == []:
            # Se non ci sono note viene appesa una tupla con 5 valori
            tupla = (cognome, nome, titolo,  collocazione, anno)
            cat.append(tupla)
            risposta = True
        elif type(note) == str:
            # Se c'è la nota controllo che sia del formato corretto e inserisco la tupla con 6 valori
            tupla = (cognome, nome, titolo, collocazione, anno,
                     note)
            cat.append(tupla)
            risposta = True

    return risposta


def serializza(cat):
    riga = ""
    if type(cat) == list:
        for elemento in cat:
            riga += str(elemento) + "\n"
    return riga


def crea_copia(cat):
    # Si fa una clonazione con slice
    newCat = cat[:]
    return newCat


def sono_uguali(cat1, cat2):
    if len(cat1) != len(cat2):  # Se la lunghezza dei due cataloghi è diversa sono necessariamente diversi
        return False
    else:
        # Creo due nuovi cataloghi con all'interno tuple contenenti solo cognome, nome, titolo e anno.
        newCat1 = []
        newCat2 = []
        for record1 in cat1:
            nuovo = (record1[0], record1[1], record1[2], record1[4])
            newCat1.append(nuovo)
        for record2 in cat2:
            nuovo2 = (record2[0], record2[1], record2[2], record2[4])
            newCat2.append(nuovo2)
        for tupla in newCat1:
            if tupla not in newCat2:
                return False
        return True


def concatena(cat1, cat2):
    nuovo = cat1  # Il nuovo catalogo viene inizializzato con il primo catalogo
    for elemento in cat2:
        # Per ogni elemento viene visto se non si trova nel catalogo (e ha note differenti) esso viene aggiunto
        if elemento not in nuovo:
            if len(elemento) == 4:
                nuovo.append(elemento)
            else:
                # Rimuovo la nota (ultimo elemento)
                catalogo1 = [x[:-1] for x in cat1]
                index = catalogo1.index(elemento[:-1])
                # for tupla in elemento:
                nota = cat1[index][5]
                # Concateno le note dei due libri
                notacombinata = elemento[5] + nota
                elemento = list(elemento)
                elemento[5] = notacombinata
                elemento = tuple(elemento)
                # Inserisco l'elemento con la nota concatenata
                nuovo[index] = elemento

    ordina(nuovo)  # ordine lessicografico
    return nuovo


def cancella(cat,  titolo, anno=None):
    if ((type(titolo) != str) or (anno != None and type(anno) != int)):
        return None
    else:
        counter = 0  # Counter per l'indice dell'elemento da rimuovere
        eliminati = 0  # Counter per gli elementi rimossi
        for elemento in cat:
            if (elemento[2].lower() == titolo.lower() and (anno == None or elemento[3] == anno)):
                cat.pop(counter)
                eliminati += 1
            counter += 1  # IL RETURN NONE

    return eliminati


def cerca(cat, pctitolo):
    for elemento in cat:
        # La funzione find() restituisce -1 se l'elemento non viene trovato
        # Cerca anche se il titolo viene digitato in minuscolo
        minuscolo = elemento[2].lower()
        if elemento[2].find(pctitolo) != -1 or minuscolo.find(pctitolo) != -1:
            trovato = True
            break
        else:
            trovato = False
    return trovato


def ordina(cat):
    # Ordino per cognome, nome, anno e infine titolo
    cat.sort(key=lambda key: (key[0], key[1], key[3], key[2]))

    return None
