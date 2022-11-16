from biblio import *
from testMy import *

c = []

inserisci(c, 12.0, "Colin", "Il mondo silenzioso di Nicholas Quinn", 2012, ("G", 15))
inserisci(c, "Wowowowow","Colin","Il mondo paxxo",2012,("B", 15))
inserisci(c, "Brodie", "Colin", "Il mondo rumoroso", 2012, ("H", 15), "Mi piace se ti muovi")


d = serializza(c)
e = crea_copia(d)
print(d)
newCat = d[:]


newCat = newCat.replace("(", "")
newCat = newCat.replace(")", "")
newCat = newCat.replace(",", "")
cat = list(newCat.split("\n"))
print(cat)





