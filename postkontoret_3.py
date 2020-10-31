paket_1 = 0
paket_2 = 0
pris = 0

def chkPrice(paket):
    if paket <= 3:
        return 205
    elif paket <= 5:
        return 240    
    elif paket <= 10:
        return 300
    elif paket <= 15:
        return 350
    elif paket <= 20:
        return 395 
    elif paket > 20:
        return 500    

def inputFunc():
    while(True):
        try:
            paket_1 = float(input("Hur mycket väger paketet det första paketet (i kg): "))
            if type(paket_1) != float or paket_1 == 0:
                return 0
                break
            paket_2 = float(input("Hur mycket väger paketet det andra paketet (i kg): "))
            if type(paket_2) != float:
                break
            else:
                return paket_1+paket_2
        except Exception as e:
            print("ERROR: ",e)
            print("Försök igen.")
            

def mainLoop():
    while True:
        print("Skriv 0 om ni vill avsluta")
        paket = inputFunc()
        if paket == 0:
            break
        print("Total vikt: ", paket,"kg")
        print("Det kostar:", chkPrice(paket))

mainLoop()
print("Thank you, come again.")