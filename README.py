#ggT calculator
import sys
sys.set_int_max_str_digits(999999)
print("Hallo! Ich kann dir den ggT und den von zwei Zahlen berechnen")
a = int(input("Zahl eins "))
b = int(input("Zahl zwei "))
a_ende = a
b_ende = b
f = 1
Vertauscher = 0
Rechnung = list()
#Hier benutze ich den Eudlikischen Algorithmus 
while f != 0 :
  if a < b :
    Vertauscher = a
    a = b
    b = Vertauscher
  a_neu = a
  a = a_neu % b
  f = a
  Rechnung.append(f)
Ergebnis = Rechnung[(len(Rechnung)-2)]
print("Der größte gemeinsame Nenner von " + str(a_ende) + " und " + str(b_ende) + " ist: ")
print(str(Ergebnis))
