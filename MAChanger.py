import subprocess, os, random, netifaces

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

menu1 = "\t INTERFAZ A EJECUTAR EL CAMBIO\n"
menu2 = "\t NUEVA DIRECCIÓN MAC\n"

def clean_screen(): # Función para limpiar pantalla.
    os.system("clear")

def check_interfaces(): # Revisa las interfaces de red disponibles en el equipo.
    interfaces = netifaces.interfaces()
    return interfaces

def select_interface(): # Muestra las interfaces de red en orden.
    print(menu1)
    interfaces = check_interfaces() # Obtener las interfaces disponibles.
    for interface in interfaces:
        print(f"[{interfaces.index(interface)}] {interface}") # Mostrar las interfaces disponibles.
    choice = int(input("\n[?] Elija una opción: "))
    
    return interfaces[choice] # Devuelve la interfaz de red seleccionada.

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

def select_mac(): # Selecciona una MAC, aleatoria con la función random_mac() o manualmente.
    print(menu2)
    print("[0] MAC Random\n[1] MAC Manual")
    choice = input("\n[?] Elija una opción: ")

    if choice == "0":
        mac = random_mac() # Genera una MAC aleatoria.
        return mac
    elif choice == "1":
        mac = input("[?] Indique la MAC que desea: ") # Pide una MAC al usuario.
        return mac
    else:
        print("[!] La opción indicada no es correcta, MAC aleatoria por default seleccionada.")
        mac = random_mac() # Genera una MAC aleatoria.
        return mac



def change_mac(mac, interface): # Toma como argumento una MAC y cambia la actual por esa.
    subprocess.call(f"sudo ifconfig {interface} down", shell=True)
    subprocess.call(f"sudo ifconfig {interface} hw ether {mac}", shell=True)
    subprocess.call(f"sudo ifconfig {interface} up", shell=True)
    print(f"\n--------------- ( ͡❛ ͜ʖ ͡❛) MAC de {interface} cambiada correctamente a {mac} ( ͡❛ ͜ʖ ͡❛) ---------------\n")
    subprocess.call(f"sudo ifconfig {interface}", shell=True) # Muestra la información de la interfaz seleccionada.

def main(): # Función principal del código.
    clean_screen() # Limpiar pantalla al inicio del código.

    print(LOGO)
    print(INFO)
    interface = select_interface() # Obtiene la interfaz de red a trabajar.

    clean_screen() # Limpiar pantalla luego de obtener la interfaz a trabajar.

    print(LOGO)
    print(INFO)
    print(f"Interfaz Seleccionada: {interface}\n")
    mac = select_mac() # Obtiene la mac que se establecerá.
    

    change_mac(mac, interface) #Cambia la dirección MAC


if __name__ == "__main__": # Inicializador.
    main()
