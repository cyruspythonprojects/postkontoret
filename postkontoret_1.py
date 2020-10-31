paket = 0
pris = 0

def inputFunc():
    while(True):
        try:
            paket = float(input("Hur mycket väger paketet (i kg): "))
            if type(paket) != float:
                break
            else:
                return paket
        except Exception as e:
            print("ERROR: ",e)
            print("Försök igen.")
            
paket = inputFunc()
       
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