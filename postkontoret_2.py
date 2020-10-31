paket_1 = 0
paket_2 = 0
pris = 0

def inputFunc():
    while(True):
        try:
            paket_1 = float(input("Hur mycket väger det första paketet (i kg): "))
            if type(paket_1) != float:
                break
            paket_2 = float(input("Hur mycket väger det andra paketet (i kg): "))
            if type(paket_2) != float:
                break
            else:
                return paket_1+paket_2
        except Exception as e:
            print("ERROR: ",e)
            print("Försök igen.")
            
paket = inputFunc()

print("Total vikt: ", paket,"kg")

if paket <= 3:
    pris = 205
elif paket <= 5:
    pris = 240    
elif paket <= 10:
    pris = 300
elif paket <= 15:
    pris = 350
elif paket <= 20:
    pris = 395 
elif paket > 20:
    pris = 500

print("Det kostar:", pris)    