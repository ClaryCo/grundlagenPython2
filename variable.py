# variable

a = 10
b = 20
c = 30

summe = a + b

print("Summe von ",a," + ", b, " = ",summe)

aktion = input ("Welche Aktion willst du?: (+/-/*/:)" )
print("Aktion",aktion, " wird ausgeführt...")

if (aktion == "*"):
    print("Multiplikation")

zahl = input("Welche Zahl wählst du?")
zahl = int (zahl)

zahl2 = int("23")

zahlA = "123"
zahlB = "456"
print(zahlA+zahlB)
# Ausgabe: 123456,weil es sich hier um einen String handelt!

zahlC = 987
text = str(zahlC)


#Taschenrechner
aktion = input ("Welche Aktion willst du?: (+/-/*/:)" )
zahl1 = input ("Gib deine 1. Zahl ein: ")
zahl2 = input ("Gib deine 2. Zahl ein: ")

if ( aktion == "+" ):
    ausgabe = int(zahl1)+int(zahl2)
if( aktion == "-"):
    ausgabe = int (zahl1)-int(zahl2)
if(aktion == " * "):
    ausgabe = int (zahl1)*int(zahl2)
if (aktion == " : "):
    ausgabe = int(zahl1):int(zahl2)
    
print(ausgabe)
