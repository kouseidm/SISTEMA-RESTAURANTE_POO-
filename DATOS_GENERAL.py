from tabulate import tabulate
Lista_mesas= []
Lista_mozos= []
lista_mesas_asignadas = []
lista_clientes = []
def menu():
    print("--" * 30)
    print("<< MENU PRINCIPAL >>".center(60))
    print("--" * 30)
    print("[1] Registros        🍽️")
    print("[2] Tomar mozo       👨")
    print("[3] Tomar pedido     🍔")
    print("[4] Calcular pago    💵")
    print("[5] Finalizar pedido 🍽️")
    print("[6] Ver reportes     📈")
    print("[7] Salir  ")
    print("--" * 30)
    print("<< ...SISTEMA RESTAURANTE -- BIENVENIDOS ...>>".center(60))
    print("--" * 30)
    
def Guardar_mesas(numero_mesa, zona_mesa, capacidad_mesa, estado_mesa):
    mesas = { "numero_mesa": numero_mesa,
                "zona_mesa": zona_mesa,
                "capacidad_mesa": capacidad_mesa,
                "estado_mesa": estado_mesa}
    Lista_mesas.append(mesas)

def Mostrar_mesas():
    if not Lista_mesas:
        print("No hay mesas registradas")
    else:
        print("Mesas registradas:")
        print(tabulate(Lista_mesas, headers="keys", tablefmt="grid"))
        

def Guardar_mozos( id_mozo, nombre_mozo, telefono_mozo, estado_mozo, capacidad_mozo, lista_mesas_asignadas):
    mozos = { "id_mozo": id_mozo,
                "nombre_mozo": nombre_mozo,
                "telefono_mozo": telefono_mozo,
                "estado_mozo": estado_mozo,
                "capacidad_mozo": capacidad_mozo,
                "mesa_asignadas": lista_mesas_asignadas}
    Lista_mozos.append(mozos)

def Mostrar_mozos():
    if not Lista_mozos:
        print("No hay mozos registrados")
    else:
        print("Mozos registrados:")
        print(tabulate(Lista_mozos, headers="keys", tablefmt="grid"))
        
def Registrar_mesas():
    print("Registro de mesas".center(80, "-"))
    print("-" * 80)
    while True:
        existe_mesa = False
        numero_mesa = int(input("Ingrese el numero de  mesa a registrar (1 - 100): "))
        if 1<= numero_mesa <= 100:
            for  id  in Lista_mesas:
                if id["numero_mesa"] == numero_mesa:
                    existe_mesa = True
                    break
        if not existe_mesa:
            break
        else:
            print("Error, el numero de mesa no es correcto")
    
    while True:
        zona_mesa = input("Ingrese la zona de disponibilidad de la mesa (sala/terraza): ").lower()
        if zona_mesa in ["sala","terraza"]:
            break
        else:
            print("Error, la zona no es correcta")
            
    while True:
        try:
            capacidad_mesa = int(input("Ingrese la capacidad de la mesa: "))
            if 1<= capacidad_mesa <= 20:
                break
            else:
                print("Error, la capacidad de la mesa no es correcta")
        except ValueError:
            print("Error en los datos de ingreso")
    
    while True:
        estado_mesa = input("Ingrese el estado de la mesa (libre/ocupada/reservada): ").lower()
        if estado_mesa in ["libre","ocupada","reservada"]:
            break
        else:
            print("Error, el estado de la mesa no es correcto")
    print("-" * 80)
    print("Mesa registrada correctamente".center(80))
    print("-" * 80)
    Guardar_mesas(numero_mesa, zona_mesa, capacidad_mesa, estado_mesa)

def Registrar_mozos():
    print("-" * 80)
    print("Registro de mozos".center(80, "-"))
    print("-" * 80)
    
    while True:
        existe_mozo = False
        id_mozo = input("Ingrese el id del mozo (4 digitos): ")
        if len(id_mozo) == 4:
            for id in Lista_mozos:
                if id["id_mozo"] == id_mozo:
                    existe_mozo = True
                    break
            if not existe_mozo:
                break
        else:
            print("Error, el id del mozo no es correcto")
    nombre_mozo = input("Ingrese el nombre y apellido del mozo: ")
    
    while True:
        try:
            telefono_mozo = input("Ingrese el telefono del mozo (9 digitos): ")
            if len(str(telefono_mozo)) == 9:
                break
            else:
                print("Error, el telefono del mozo no es correcto")
        except ValueError:
            print("Error en los datos de ingreso")
    
    while True:
        estado_mozo = input("Ingrese el estado del mozo (activo/inactivo): ").lower()
        if estado_mozo in ["activo","inactivo"]:
            break
        else:
            print("Error, el estado del mozo no es correcto")
            
    capacidad_mozo = 4
    Guardar_mozos(id_mozo, nombre_mozo, telefono_mozo, estado_mozo, capacidad_mozo,lista_mesas_asignadas)
    print("-" * 80)
    print("Mozo registrado correctamente".center(80))
    print("-" * 80)
    
    
def Asiganar_mozo():
    Mostrar_mozos()
    if not Lista_mozos:
        print("No hay mozos registrados")
    
    id_mozo = input("Ingrese el id del mozo a asignar (4 digitos): ")
    for id in Lista_mozos:
        if id["id_mozo"] == id_mozo :
            if id["estado_mozo"] == "activo":
                break
            else:
                print("Error, el mozo no esta disponible")
                break
    else:
        print("Error, el id del mozo no es correcto")
        return
    
    if len(lista_mesas_asignadas) == 4:
        id["estado_mozo"] = "inactivo"
        print("-" * 80)
        print("Error, el mozo no puede atender mas mesas")
        print("-" * 80)
        return
    
    while True:
        try:
            numero_mesa = int(input("Ingrese el numero de mesa a reservar (1 - 100): "))
            if 1<= numero_mesa <= 100:
                break
            else:
                print("Error, el numero de mesa no es correcto")
        except ValueError:
            print("Error en los datos de ingreso")
            
    for id in Lista_mesas:
        if id["numero_mesa"] == numero_mesa:
            mesas_asignadas = id["numero_mesa"]
            lista_mesas_asignadas.append(mesas_asignadas)
            if id["estado_mesa"] == "libre":
                id["estado_mesa"] = "reservada"
                print("-" * 80)
                print("Mesa reservada correctamente".center(80))
                print("-" * 80)
            else:
                print("Error, la mesa no esta disponible")









# Alexis Huaman-----------------------------------------------------------------------------------------
def cartas():
        print("--" * 30)
        print("<< BIENVENIDO AL MENU >>".center(60))
        print("Seleccionar que desea: ")
        print("1. Platos")
        print("2. Postres")
        print("3. Bebidas")
        print("[0. Salir]")
def carta_platos():
    platos = {
        1: ["Lomo Saltado", 35.00],
        2: ["Ceviche", 35.00],
        3: ["Causa limeña", 25.00],
        4: ["Arroz con pollo", 20.00],
        5: ["Aji de gallina", 20.00],
        6: ["Pollo a la brasa", 24.00],
        7: ["Papa Rellena", 25.00],
        8: ["Chicharron de pescado", 30.00],
        9: ["Tallarines verdes", 25.00],
        10: ["Tallarines Rojos", 25.00]
        }
    print("--" * 30)
    print("<< MENU DE PLATILLOS DE FONDO >>".center(60))
    print("--" * 30)
    print("Platillos:", " "*28, "Precio:")
    for i, (nombre_precios) in enumerate(platos.values(), start=1):
        print(f"{i}. {nombre_precios[0]:<40} s/. {nombre_precios[1]}")
    print("[0. Regresar]  ")
    print("--" * 30)
    return platos
def carta_postres():
    postres= {
        1: ["Mazamorra morada", 12.00],
        2: ["Arroz con leche", 12.00],
        3: ["Suspiro a la limeña", 10.00],
        4: ["Picarones", 15.00],
        5: ["Alfajores", 10.00],
        6: ["Torta de chocolates", 18.00],
        7: ["Turron", 15.00],
        8: ["King kong de manjar blanco",12.00]
    }
    print("--" * 30)
    print("<< MENU DE POSTRES >>".center(60))
    print("Postres:", " "*30, "Precios:")
    for num, nombre_precios in enumerate(postres.values(),start=1):
        print (f"{num}.{nombre_precios[0]:<40} s/. {nombre_precios[1]}")
    print("[0. Regresar]  ")
    print("--" * 30)
    return postres
def carta_bebidas():
    bebidas = {
        1: ["Chicha morada", 18.00],
        2: ["Chicha de jora", 18.00],
        3: ["CocaCola", 10.00],
        4: ["InkaCola", 10.00],
        5: ["Jugo natural", 10.00],
        6: ["Cafe", 6.00],
        7: ["Pisco Sour", 20.00],
        8: ["Chilcano de pisco", 18.00]
    }
    print("--" * 30)
    print("<< MENU DE BEBIDAS >>".center(60))
    print("--" * 30)
    print("Bebidas:", " "*30, "Precio:")
    for num, nombre_precios in enumerate(bebidas.values(), start=1):
        print(f"{num}.{nombre_precios[0]:<40} s/. {nombre_precios[1]}")
    print("[0. Regresar]  ")
    print("--" * 30)
    return bebidas



def guardar_cliente(numero_mesa, mozo_asignado, pedido):
    cliente = {
        "N_Mesa": numero_mesa,
        "N_Mozo" : mozo_asignado,
        "Pedido" : pedido
    }
    lista_clientes.append(cliente)
def mostrar_cliente():
    if not lista_clientes:
        print("La lista esta vacia")
    else:
        print(tabulate(lista_clientes,headers="keys",tablefmt="grid"))
        
def registrar_pedido():
    while True:
        existe_mesa = False
        numero_mesa = int(input("Ingrese el numero de  mesa a registrar (1 - 100): "))
        if 1<= numero_mesa <= 100:
            for  id  in Lista_mesas:
                if id["numero_mesa"] == numero_mesa:
                    existe_mesa = True
                    break
        if not existe_mesa:
            break
        else:
            print("Error, el numero de mesa no es correcto")     
    print("--" * 30)
    print("<< BIENVENIDO AL MENU >>".center(60))
    print("Seleccionar que desea: ")
    print("1. Platos")
    print("2. Postres")
    print("3. Bebidas")
    print("[0. Salir]")
    while True:
        opcion = int(input ("Ingresar opcion: "))
        if opcion == 1:
            platos = carta_platos()
            while True:
                opcion = input("Elegir opcion de plato: ")
                if 1<= opcion <= 10:
                    pedido = platos[pedido] # platos[pedido] = nombre, precio
                    break
                else:
                    print("No existe opcion.")
                #PARA LA MESA 10, CON EL MOZO PEPE, SE AÑADIO EL PEDIDO DE UNA "X"
        elif opcion == 2:
            carta_postres()
        elif opcion == 3:
            carta_bebidas()
        elif opcion == 0:
            break
        else:
            print("Opcion no existente")
            
    mozo_asignado = None
    for mozo in Lista_mozos:
        if numero_mesa in mozo["mesa_asignadas"]:
            mozo_asignado = mozo["nombre_mozo"]
            break
    if mozo_asignado:
        print("El mozo que atiende la mesa es: ", mozo_asignado)
    else:
        print("No hay un mozo asignado a esta mesa.")
    guardar_cliente(numero_mesa, mozo_asignado, pedido)
    
    
    
# -------------------------------------------------------------------------------------------------
def main():
    while True:
        menu()
        while True:
            try:
                opcion = int(input("Seleccione una opción: "))
                if 1 <= opcion <= 7:
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
        if opcion == 1:
            print("1. Registrar mesas")
            print("2. Registrar mozos")
            while True:
                try:
                    subopcion = int(input("Seleccione una opción: "))
                    if 1 <= subopcion <= 2:
                        break
                    else:
                        print("Opción inválida. Intente nuevamente.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
            if subopcion == 1:   
                Registrar_mesas()
            elif subopcion == 2:
                Registrar_mozos()
            else:
                print("Opcion no valida")
                
        elif opcion == 2:
            Asiganar_mozo()
        elif opcion == 3:
            print("1. Añadir items")
            print("2. Eliminar items")
            print("3. Registrar hora de inicio y final")
            print("[0. Regresar]")
            while True:
                try:
                    opcion = int(input ("Ingresar opcion: "))
                    if  opcion == 1:
                        registrar_pedido()
                        mostrar_cliente()
                    elif opcion == 2:
                        print("Funcion eliminar pedido")
                    elif opcion == 2:
                        pass
                except ValueError:
                    print("Valor incorrecto")
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            print("1. Mostrar mesas")
            print("2. Mostrar mozos")
            while True:
                try:
                    subopcion = int(input("Seleccione una opción: "))
                    if 1 <= subopcion <= 2:
                        break
                    else:
                        print("Opción inválida. Intente nuevamente.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
            if subopcion == 1:
                Mostrar_mesas()
            elif subopcion == 2:
                Mostrar_mozos()
            else:
                print("Opcion no valida")
        elif opcion == 7:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
main()