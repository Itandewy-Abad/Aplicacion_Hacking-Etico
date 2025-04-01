import nmap

def escanear_puertos(ip, puertos="1-65535"):
    escaner = nmap.PortScanner()
    print(f"Escaneando {ip} en los puertos {puertos}...")
    escaner.scan(ip, puertos, arguments='-T4 -Pn')
    
    puertos_abiertos = []
    
    for puerto in escaner[ip]['tcp']:
        if escaner[ip]['tcp'][puerto]['state'] == 'open':
            puertos_abiertos.append(puerto)
    
    if puertos_abiertos:
        print("Puertos abiertos:")
        for p in puertos_abiertos:
            print(f"- {p}")
    else:
        print("No se encontraron puertos abiertos.")

if __name__ == "__main__":
    objetivo = input("Ingrese la IP o dominio a escanear: ")
    opcion = input("Ingrese el tipo de escaneo (1: puerto específico, 2: rango de puertos, 3: todos los puertos): ")
    
    if opcion == "1":
        puerto = input("Ingrese el puerto a escanear: ")
        escanear_puertos(objetivo, puerto)
    elif opcion == "2":
        rango = input("Ingrese el rango de puertos (ejemplo: 20-80): ")
        escanear_puertos(objetivo, rango)
    elif opcion == "3":
        escanear_puertos(objetivo)
    else:
        print("Opción no válida.")
