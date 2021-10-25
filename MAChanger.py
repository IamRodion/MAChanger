import subprocess, os, random

INFO = "[i] Creado por __Rodion__. (github.com/RodionButEncapsulated)\n"

LOGO = """
 ,ggg, ,ggg,_,ggg,                   ,gggg,                                                                       
dP""Y8dP""Y88P""Y8b                ,88"'"Y8b, ,dPYb,                                                              
Yb, `88'  `88'  `88               d8"     `Y8 IP'`Yb                                                              
 `"  88    88    88              d8'   8b  d8 I8  8I                                                              
     88    88    88             ,8I    "Y88P' I8  8'                                                              
     88    88    88    ,gggg,gg I8'           I8 dPgg,     ,gggg,gg   ,ggg,,ggg,     ,gggg,gg   ,ggg,    ,gggggg, 
     88    88    88   dP"  "Y8I d8            I8dP" "8I   dP"  "Y8I  ,8" "8P" "8,   dP"  "Y8I  i8" "8i   dP""'"8I 
     88    88    88  i8'    ,8I Y8,           I8P    I8  i8'    ,8I  I8   8I   8I  i8'    ,8I  I8, ,8I  ,8'    8I 
     88    88    Y8,,d8,   ,d8b,`Yba,,_____, ,d8     I8,,d8,   ,d8b,,dP   8I   Yb,,d8,   ,d8I  `YbadP' ,dP     Y8,
     88    88    `Y8P"Y8888P"`Y8  `"Y8888888 88P     `Y8P"Y8888P"`Y88P'   8I   `Y8P"Y8888P"888888P"Y8888P      `Y8
                                                                                         ,d8I'                    
                                                                                       ,dP'8I                     
                                                                                      ,8"  8I                     
                                                                                      I8   8I                     
                                                                                      `8, ,8I                     
                                                                                       `Y8P"                      """

def clean_screen():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def random_mac(): # Genera una dirección MAC aleatoria.
    chars = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    mac = ""

    group1 = (random.choice(chars) + "2") # El primer grupo debe ser par.
    group2 = (random.choice(chars) + random.choice(chars))
    group3 = (random.choice(chars) + random.choice(chars))
    group4 = (random.choice(chars) + random.choice(chars))
    group5 = (random.choice(chars) + random.choice(chars))
    group6 = (random.choice(chars) + random.choice(chars))

    mac = f"{group1}:{group2}:{group3}:{group4}:{group5}:{group6}"

    return mac

def change_mac(mac, interface): # Toma como argumento una MAC y cambia la actual por esa.
    subprocess.call(f"sudo ifconfig {interface} down", shell=True)
    subprocess.call(f"sudo ifconfig {interface} hw ether {mac}", shell=True)
    subprocess.call(f"sudo ifconfig {interface} up", shell=True)
    print(f"\n--------------- ( ͡❛ ͜ʖ ͡❛) MAC cambiada correctamente a {mac} ( ͡❛ ͜ʖ ͡❛) ---------------\n")
    subprocess.call(f"sudo ifconfig {interface}", shell=True) # Muestra la información de la interfaz seleccionada.

def main(): # Función principal del código.
    clean_screen() # Limpiar pantalla al inicio del código.

    print(LOGO)
    print(INFO)    

    interface = input("[?] Ingrese la interfaz a hacer el cambio. (Enter para wlan0): ")
    mac = input("[?] Ingrese la nueva dirección MAC (Enter para una aleatoria): ")

    if mac == "":
        mac = random_mac()
        if interface == "":
            interface = "wlan0"
            change_mac(mac, interface) #Cambia la dirección MAC
        else:
            change_mac(mac, interface) #Cambia la dirección MAC
    else:
        if interface == "":
            interface = "wlan0"
            change_mac(mac, interface) #Cambia la dirección MAC
        else:
            change_mac(mac, interface) #Cambia la dirección MAC



if __name__ == "__main__": # Inicializador.
    main()
