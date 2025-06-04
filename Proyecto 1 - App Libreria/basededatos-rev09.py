import pandas as pd
import os
from pandas import ExcelWriter 
from colorama import Back, Fore, Style, init
init(autoreset=True)
import time

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

logo = '''
,--.  ,--,-----. ,------.,------,------.,--. ,---.      ,-----. ,------.  ,---. ,--.  ,--,--,--.   ,--,------,--.    
|  |  |  |  |) /_|  .--. |  .---|  .--. |  |/  O  \     |  |) /_|  .--. '/  O  \|  ,'.|  |  |\  `.'  /|  .---|  |    
|  |  |  |  .-.  |  '--'.|  `--,|  '--'.|  |  .-.  |    |  .-.  |  '--'.|  .-.  |  |' '  |  | \     / |  `--,|  |    
|  '--|  |  '--' |  |\  \|  `---|  |\  \|  |  | |  |    |  '--' |  |\  \|  | |  |  | `   |  |  \   /  |  `---|  '--. 
`-----`--`------'`--' '--`------`--' '--`--`--' `--'    `------'`--' '--`--' `--`--'  `--`--'   `-'   `------`-----' 
'''
init

def menu():
    while True:   
        print(Fore.CYAN + "-" * 30)
        print(Back.LIGHTCYAN_EX + Fore.GREEN + Style.BRIGHT + f"{'Menú de Inventario':^30}")
        print(Fore.CYAN + "-" * 30)
        print(Fore.CYAN +'1. Agregar artículo')
        print(Fore.CYAN +'2. Ver stock')
        print(Fore.CYAN +'3. Buscar artículo')
        print(Fore.CYAN +'4. Salida de Stock')
        print(Fore.CYAN +'5. Eliminar Artículo')
        print(Fore.CYAN +'6. Ver todos')
        print(Fore.CYAN +'7. Salir')
        print( )
        opcion = input(Fore.CYAN + 'Selecciona una opción: ')
        
        if opcion == "1":
            opcion_uno()
        elif opcion == "2":
            opcion_dos()
        elif opcion == "3":
            opcion_tres()
        elif opcion == "4":
            opcion_cuatro()
        elif opcion == "5":
            opcion_cinco()
        elif opcion == "6":
            print()
            print(datos_con_encabezado_ok)
            time.sleep(15)
            menu()
        elif opcion == "7":
            opcion_siete()
            break
        else:
            print(Fore.RED + "Por favor, ingrese una opción válida.")
            time.sleep(3)
            clear()
            return menu()


lista_usuarios= ["PEPE"]
lista_contrasenia= ["123"]

def nuevo_usuario(): # Permite crear un usuario nuevo para acceder al sistema
    while True:
        print( )
        nuevo_usuario = input(Fore.BLUE + "Por favor, elija un nombre de usuario: ").upper()
        if nuevo_usuario in lista_usuarios:
            print(Fore.RED + "Usuario no disponible. Por favor, elija otro usuario.")
        else:
            nueva_contrasenia = input(Fore.BLUE + "Ingrese una contraseña para el nuevo usuario: ")
            lista_usuarios.append(nuevo_usuario) # Agrega el usuario nuevo al sistema
            lista_contrasenia.append(nueva_contrasenia) # Agrega el contrasenia nueva al sistema
            print(Fore.GREEN + "Usuario creado con éxito.")
            time.sleep(2)
            return acceso_sistema()


def usuario_existente(): # Inicia sesion con un usuario ya creado
    usuario_existente = input("Por favor, elija un usuario: ").upper()
    if usuario_existente in lista_usuarios:
        indice = lista_usuarios.index(usuario_existente)
        contrasenia = input("Ingrese su contraseña: ")
        
        if contrasenia in lista_contrasenia[indice]: # Verifica la contraseña en el mismo índice
            print(Fore.GREEN + "Acceso concedido.")
            clear()
            menu()
        else:
            print(Fore.RED + "Contraseña incorrecta. Intente nuevamente.")
            time.sleep(3)
            acceso_sistema()
    else:
        print(Fore.RED + "Usuario no encontrado. Intente nuevamente o registre un usuario nuevo.")
        time.sleep(3)
        acceso_sistema()


def acceso_sistema():
        clear()
        print(Style.BRIGHT + Fore.CYAN + logo)
        print(Fore.BLUE + "-" * 30)
        print(Back.LIGHTGREEN_EX + Fore.BLUE + Style.BRIGHT + f"{"BIENVENIDO":^30}")
        print(Fore.BLUE + "-" * 30)
        ingreso_usuario = input(Fore.BLUE + "Ingrese [0] para iniciar sesión o [1] para crear una cuenta nueva: ")
        clear()
        if ingreso_usuario == "0":
            usuario_existente()
        elif ingreso_usuario == "1":
            nuevo_usuario()
        else:
            print(Fore.RED + "Por favor, ingrese una opción válida.")
            time.sleep(1)
        clear()
        acceso_sistema()


def opcion_uno(): # 1. Agregar de articulo
    articulo_ingreso = input(Fore.CYAN + "Por favor, indique el código del producto a agregar: \n" ).strip().upper()
    
    if articulo_ingreso in datos.index:
        descripcion = datos.loc[articulo_ingreso, 'Descripcion']
        categoria = datos.loc[articulo_ingreso, 'Categoria']
        stock_actual = datos.loc[articulo_ingreso, 'Stock']
        
        print()
        separador = ("-" * 62)
        print(Fore.BLUE + separador)
        print(Fore.GREEN + "Actualmente su producto tiene las siguientes características:")
        print(Fore.BLUE + separador)
        
        print(Back.LIGHTGREEN_EX + Fore.BLUE + Style.BRIGHT + f"{"Código":^10} {"Descripción":^10} {"Categoría":^10} {"Stock":^8}")
        print(Fore.BLUE + f"{articulo_ingreso.upper():^10} {descripcion.upper():^10} {categoria.upper():^10} {stock_actual:^8}\n")
        cantidad_nuevo_stock = int(input(Fore.BLUE + "Indique la cantidad a actualizar: "))
        print()
        print(Fore.YELLOW + "¿Está seguro que desea confirmar su operación?")
        print()
        respuesta = input(Fore.YELLOW + "Escriba 'S' si desea confirmar la operación o 'N' si desea cancelar: \n").upper()
        if respuesta == 'S':
            nuevo_stock = stock_actual + cantidad_nuevo_stock
            datos.loc[articulo_ingreso, 'Stock'] = nuevo_stock
            
            guardar_datos_en_excel()
            print(Fore.GREEN + f"Producto actualizado. Ahora tiene {nuevo_stock} unidades del producto {descripcion}.")
            time.sleep(5)
            clear()
            while True:
                opcion = menu()
                if opcion == "1":
                    opcion_uno()
                elif opcion == "2":
                    opcion_dos()
                elif opcion == "3":
                    opcion_tres()
                elif opcion == "4":
                    opcion_cuatro()
                elif opcion == "5":
                    opcion_cinco()
                elif opcion == "6":
                    print(datos_con_encabezado_ok)
                    time.sleep(15)
                elif opcion == "7":
                    opcion_siete()
                break
        else:
            print(Fore.RED + "¡Su operación fue cancelada con éxito!")
            time.sleep(3)
            clear()
            menu()
    else:
        print()
        print(Fore.MAGENTA + "Su producto es nuevo, por favor indique lo siguiente: \n")
        descripcion_art_ingreso = input(Fore.BLUE + "Por favor, ingrese la descripción del nuevo producto: \n").strip().upper()
        print()
        categoria_art_ingreso = input(Fore.BLUE + "Por favor, ingrese la categoría del nuevo producto: \n").strip().upper()
        print()
        stock_nuevo_producto = int(input(Fore.BLUE + "Indique la cantidad del nuevo producto: \n"))
        print()
        unidad_de_medida = input(Fore.BLUE + "Por favor, ingrese la unidad de medida del nuevo producto: \n").strip().upper()
        print()
        datos.loc[articulo_ingreso] = [descripcion_art_ingreso, categoria_art_ingreso, stock_nuevo_producto, unidad_de_medida]
        guardar_datos_en_excel()
        print(Fore.GREEN + "Producto ingresado con éxito al inventario.\n")
        time.sleep(4)
        
        separador = ("-" * 62)
        print(Fore.GREEN + separador)
        print(Back.LIGHTGREEN_EX + Fore.BLUE + Style.BRIGHT + f"{"Código":^10} {"Descripción":^10} {"Categoría":^10} {"Stock":^8} {"Unidad":^8}")
        print(Fore.BLUE + f"{articulo_ingreso.upper():^10} {descripcion_art_ingreso.upper():^10} {categoria_art_ingreso.upper():^10} {stock_nuevo_producto:^8} {unidad_de_medida:^8}\n")
        print(Fore.GREEN + separador)
        clear()
        menu()


def opcion_dos(): # 2. Ver Stock
    articulo_stock = input(Fore.BLUE + "Indique el código del artículo que desea consultar stock: \n").strip().upper()
    
    if articulo_stock in datos.index:
        stock = datos.loc[articulo_stock, 'Stock']
        descripcion = datos.loc[articulo_stock, 'Descripcion']
        separador = ("-" * 65)
        print(Fore.GREEN + separador)
        print(Fore.BLUE + f"El stock disponible para el artículo {articulo_stock} - {descripcion} es: {stock}")
        print(Fore.GREEN + separador)
        time.sleep(5)
        clear()
        menu()
    else:
        print(Fore.RED + f"El artículo {articulo_stock} no se encuentra en el inventario")
        respuesta = input(Fore.YELLOW + "¿desea agregar el articulo? Escriba 'S' para confirmar o 'N' para cancelar:\n ").strip().upper()
        if respuesta == "S":
                opcion_uno() 
        else:
            print(Fore.RED + "¡Su operación fue cancelada con éxito!")
        time.sleep(3)
        clear()
        menu()


def opcion_tres():  # 3. Buscar artículo por código o por palabra clave
    consulta = input("Indique el código del artículo o una palabra clave para buscar en la descripción: \n").strip().upper()
    
    # Verificar si la consulta es un código de artículo
    if consulta in datos.index:
        descripcion = datos.loc[consulta, 'Descripcion']
        categoria = datos.loc[consulta, 'Categoria']
        stock = datos.loc[consulta, 'Stock']
        unidad = datos.loc[consulta, 'Unidad de medida']
        print()
        print(Fore.MAGENTA + "Su producto se encuentra en el inventario con las siguientes características: ")
        separador = (Fore.GREEN + "-" * 77)
        print(separador)
        print(Back.LIGHTGREEN_EX + Fore.BLUE + Style.BRIGHT + f"{"Código":^10} {"Descripción":^10} {"Categoría":^10} {"Stock":^8} {"Unidad":^8}")
        print(Fore.BLUE + f"{consulta.upper():^10} {descripcion.upper():^10} {categoria.upper():^10} {stock:^8} {unidad:^8}\n") 
        time.sleep(5)
        clear()
        menu()
    else:
        # Si no es un código de artículo, buscar por palabra clave en la descripción
        encontrados = datos[datos['Descripcion'].str.upper().str.contains(consulta)]
        
        if not encontrados.empty:
            print(Fore.MAGENTA + "Se encontraron los siguientes artículos que contienen la palabra en la descripción:")
            print(encontrados)
            time.sleep(8)
            clear()
            menu()
        else:
            print(Fore.RED + f"No se encontraron artículos que coincidan con '{consulta}' en el código o la descripción.")
            time.sleep(3)
            clear()
        menu()


def opcion_cuatro(): # 4. Salida de Stock
    articulo_salida = input(Fore.BLUE + "Por favor, indique el código del artículo para realizar una salida: \n").strip().upper()
    if articulo_salida in datos.index:
        stock_actual = int(datos.loc[articulo_salida, 'Stock'])
        cantidad_salida = int(input(Fore.BLUE + "Indique la cantidad a egresar: \n"))   
        if stock_actual < cantidad_salida:
            print(Fore.RED + f"Stock insuficiente. Stock actual: {stock_actual}\n")
            time.sleep(5)
            clear()
            menu()
        else:
            print(f"Actualmente tiene en stock {stock_actual} unidades del artículo {articulo_salida}."+ Fore.YELLOW +"¿Está seguro que desea confirmar su operación?")
            respuesta = input(Fore.YELLOW + "Escriba 'S' si desea confirmar la operación o 'N' si desea cancelar: \n").upper()
            if respuesta == 'S':
                nuevo_stock = stock_actual - cantidad_salida
                datos.loc[articulo_salida, 'Stock'] = nuevo_stock
                guardar_datos_en_excel()
                print(Fore.GREEN + f"Operación realizada correctamente. Nuevo stock del artículo {articulo_salida}: {nuevo_stock}")
                time.sleep(5)
                clear()
                menu()
            else:
                print(Fore.RED + "¡Su operación fue cancelada con éxito!")
                time.sleep(3)
                clear()
                menu()
    else:
        print(Fore.RED + f"El artículo {articulo_salida} no se encuentra en el inventario.")
        time.sleep(3)
        clear()
        menu()


def opcion_cinco(): # 5. Eliminar artículo
    articulo_eliminar = input(Fore.BLUE + "Por favor, ingrese el código del artículo que desea eliminar: \n").strip().upper()
    
    if articulo_eliminar in datos.index:
        descripcion = datos.loc[articulo_eliminar, 'Descripcion']
        categoria = datos.loc[articulo_eliminar, 'Categoria']
        stock_actual = datos.loc[articulo_eliminar, 'Stock']
        print()
        print(Fore.MAGENTA + "Actualmente su producto tiene las siguientes características: ")
        separador = (Fore.GREEN + "-" * 65)
        print(separador)
        print(Back.LIGHTGREEN_EX + Fore.BLUE + Style.BRIGHT + f"{"Código":^10} {"Descripción":^10} {"Categoría":^10} {"Stock":^8}")
        print(Fore.BLUE + f"{articulo_eliminar.upper():^10} {descripcion.upper():^10} {categoria.upper():^10} {stock_actual:^8}\n")
        time.sleep(2)
        print(Fore.YELLOW + "¿Está seguro que desea confirmar su operación?")
        respuesta = input(Fore.BLUE + "Escriba 'S' si desea confirmar la operación o 'N' si desea cancelar: \n").upper()
        if respuesta == 'S':
            datos.drop(index=articulo_eliminar, inplace=True)
            guardar_datos_en_excel()
            print(Fore.GREEN + f"Operación realizada correctamente. Se eliminó el producto {descripcion}.")
            time.sleep(4)
            clear()
            menu()
        else:
            print(Fore.RED + "¡Su operación fue cancelada con éxito!")
            time.sleep(3)
            clear()
            menu()
    else:
        print(Fore.RED + f"El artículo {articulo_eliminar} no se encuentra en el inventario.")
        time.sleep(3)
        clear()
        menu()


def opcion_siete(): # 7. Salir
    respuesta = input(Fore.YELLOW + "¿Está seguro que desea salir del sistema? Escriba 'S' para confirmar o 'N' para cancelar: \n").upper()
    if respuesta == "S":
        print(Fore.GREEN + "Saliendo del sistema. ¡Gracias por utilizar nuestro programa!")
        time.sleep(3)
        clear()
        acceso_sistema()
    else:
        print(Fore.RED + "Operación cancelada. Continúa en sesión.")
        time.sleep(2)
        clear()
        menu() # fix


def guardar_datos_en_excel():
    try:
        with ExcelWriter(ruta_excel, engine='openpyxl', mode='w') as writer:
            datos.to_excel(writer, sheet_name='Hoja1', index=True)
        print(Fore.GREEN + "Datos guardados correctamente en el archivo Excel. \n")
    except Exception as e:
        print(Fore.RED + f"Error al guardar los datos en el archivo Excel: {e}")


# Especifica la ruta del archivo Excel
ruta_excel = r'C:\Users\Nb122\Desktop\Ejercicios de Phyton\TP INTEGRADOR\Base de datos .xlsx'

# Lee el archivo Excel y carga los datos en un DataFrame de pandas
datos = pd.read_excel(ruta_excel, sheet_name='Hoja1', index_col=0)

# Lee el archivo Excel con el encabezado modificado y carga los datos en un DataFrame de pandas
datos_con_encabezado_ok = pd.read_excel(ruta_excel, sheet_name='Hoja1', index_col=0, header=[0,1])


# Llamada al sistema de acceso
acceso_sistema()
