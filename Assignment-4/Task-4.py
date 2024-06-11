#converting temp from celsius to fahreinheit

def Cel_to_Fah(C):
    F = (9 / 5) * C + 32
    return F
C = float(input("Enter the celsius value to be converted"))
F=Cel_to_Fah(C)
print("Fahreinheit value is:",F)
#converting temp from fahreinheit to celsius

def Fah_to_Cel(F):
    C= (F - 32) * 5 / 9
    return C
F=float(input("Enter the Fahreinheit value to be converted"))
C=Fah_to_Cel(F)
print("Celsius value is:",C)



