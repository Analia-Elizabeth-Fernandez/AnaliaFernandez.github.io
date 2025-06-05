import pandas as pd
import os
from pandas import ExcelWriter 
from colorama import Back, Fore, Style, init
init(autoreset=True)
import time
import requests

url = "https://github.com/Analia-Elizabeth-Fernandez/AnaliaFernandez.github.io/raw/main/Base%20de%20datos%20.xlsx"
response = requests.get(url)

if response.status_code == 200:
    with open("Base de datos.xlsx", 'wb') as f:
        f.write(response.content)
    
    try:
        datos = pd.read_excel("Base de datos.xlsx", sheet_name='Hoja1', index_col=0, engine='openpyxl')
        print("Datos cargados correctamente:")
        print(datos.head())
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
else:
    print("No se pudo descargar el archivo.")

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

# Función para obtener entradas, con soporte para modo producción (variables de entorno)
def obtener_entrada(prompt, var_env):
    if os.getenv("PRODUCTION") == "1":
        valor = os.getenv(var_env)
        print(Fore.BLUE + f"{prompt} {valor}")
        return valor
    else:
        return input(Fore.BLUE + prompt)

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
        print()
        opcion = obtener_entrada('Selecciona una opción: ', 'OPCION_MENU')
        
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
            clear()
        elif opcion == "7":
            opcion_siete()
            break
        else:
            print(Fore.RED + "Por favor, ingrese una opción válida.")
            time.sleep(3)
            clear()

lista_usuarios= ["PEPE"]
lista_contrasenia= ["123"]

def nuevo_usuario():
    while True:
        print()
        nuevo_usuario = obtener_entrada("Por favor, elija un nombre de usuario: ", "NUEVO_USUARIO").upper()
        if nuevo_usuario in lista_usuarios:
            print(Fore.RED + "Usuario no disponible. Por favor, elija otro usuario.")
            if os.getenv("PRODUCTION") == "1":
                break  # Evitar loop infinito en producción
        else:
            nueva_contrasenia = obtener_entrada("Ingrese una contraseña para el nuevo usuario: ", "NUEVA_CONTRASENIA")
            lista_usuarios.append(nuevo_usuario)
            lista_contrasenia.append(nueva_contrasenia)
            print(Fore.GREEN + "Usuario creado con éxito.")
            time.sleep(2)
            return acceso_sistema()
        if os.getenv("PRODUCTION") == "1":
            break

def usuario_existente():
    usuario_existente = obtener_entrada("Por favor, elija un usuario: ", "USUARIO").upper()
    if usuario_existente in lista_usuarios:
        indice = lista_usuarios.index(usuario_existente)
        contrasenia = obtener_entrada("Ingrese su contraseña: ", "CONTRASENIA")
        
        if contrasenia == lista_contrasenia[indice]:
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
    print(Back.LIGHTGREEN_EX + Fore.BLUE + Style.BRIGHT + f"{{'BIENVENIDO':^30}}")
    print(Fore.BLUE + "-" * 30)
    ingreso_usuario = obtener_entrada("Ingrese [0] para iniciar sesión o [1] para crear una cuenta nueva: ", "ACCION")
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

def opcion_uno():
    articulo_ingreso = obtener_entrada("Por favor, indique el código del producto a agregar: \n", "CODIGO_ARTICULO").strip().upper()
    
    if articulo_ingreso in datos.index:
        descripcion = datos.loc[articulo_ingreso, 'Descripcion']
        categoria = datos.loc[articulo_ingreso, 'Categoria']
        stock_actual = datos.loc[articulo_ingreso, 'Stock']
        
        print()
        separador = ("-" * 62)
        print(Fore.BLUE + separador)
        print(Fore.GREEN + "Actualmente su producto tiene las siguientes características:")
        print(Fore.BLUE + separador)
        
        print(Back.LIGHTGREEN_EX + Fore.BLUE + Style.BRIGHT + f"{'Código':^10} {'Descripción':^10} {'Categoría':^10} {'Stock':^8}")
        print(Fore.BLUE + f"{articulo_ingreso.upper():^10} {descripcion.upper():^10} {categoria.upper():^10} {stock_actual:^8}\n")
        cantidad_nuevo_stock = int(obtener_entrada("Indique la cantidad a actualizar: ", "CANTIDAD_ACTUALIZAR"))
        print()
        print(Fore.YELLOW + "¿Está seguro que desea confirmar su operación?")
        print()
        respuesta = obtener_entrada("Escriba 'S' si desea confirmar la operación o 'N' si desea cancelar: \n", "CONFIRMAR_OPERACION").upper()
        if respuesta == 'S':
            nuevo_stock = stock_actual + cantidad_nuevo_stock
            datos.loc[articulo_ingreso, 'Stock'] = nuevo_stock
            
            guardar_datos_en_excel()
            print(Fore.GREEN + f"Producto actualizado. Ahora tiene {nuevo_stock} unidades del producto {descripcion}.")
            time.sleep(5)
            clear()
            menu()
        else:
            print(Fore.RED + "¡Su operación fue cancelada con éxito!")
            time.sleep(3)
            clear()
            menu()
    else:
        print()
        print(Fore.MAGENTA + "Su producto es nuevo, por favor indique lo siguiente: \n")
        descripcion_art_ingreso = obtener_entrada("Por favor, ingrese la descripción del nuevo producto: \n", "DESCRIPCION_NUEVO").strip().upper()
        print()
        categoria_art_ingreso = obtener_entrada("Por favor, ingrese la categoría del nuevo producto: \n", "CATEGORIA_NUEVO").strip().upper()
        print()
        stock_nuevo_producto = int(obtener_entrada("Indique la cantidad del nuevo producto: \n", "STOCK_NUEVO"))
        print()
        unidad_de_medida = obtener_entrada("Por favor, ingrese la unidad de medida del nuevo producto: \n", "UNIDAD_MEDIDA_NUEVO").strip().upper()
        print()
        datos.loc[articulo_ingreso] = [descripcion_art_ingreso, categoria_art_ingreso, stock_nuevo_producto, unidad_de_medida]
        guardar_datos_en_excel()
        print(Fore.GREEN + "Producto ingresado con éxito al inventario.\n")
        time.sleep(4)
        
        separador = ("-" * 62)
        print(Fore.GREEN + separador)
        print(Back.LIGHTGREEN_EX + Fore.BLUE + Style.BRIGHT + f"{'Código':^10} {'Descripción':^10} {'Categoría':^10} {'Stock':^8} {'Unidad':^8}")
        print(Fore.BLUE + f"{articulo_ingreso.upper():^10} {descripcion_art_ingreso.upper():^10} {categoria_art_ingreso.upper():^10} {stock_nuevo_producto:^8} {unidad_de_medida:^8}\n")
        print(Fore.GREEN + separador)
        clear()
        menu()

def opcion_dos():
    articulo_stock = obtener_entrada("Indique el código del artículo que desea consultar stock: \n", "CODIGO_CONSULTA").strip().upper()
    
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
        print(Fore.RED + "No se encontró el producto.")
        time.sleep(3)
        clear()
        menu()

def opcion_tres():
    articulo_buscar = obtener_entrada("Ingrese el código del artículo a buscar: \n", "CODIGO_BUSCAR").strip().upper()
    if articulo_buscar in datos.index:
        descripcion = datos.loc[articulo_buscar, 'Descripcion']
        categoria = datos.loc[articulo_buscar, 'Categoria']
        stock = datos.loc[articulo_buscar, 'Stock']
        unidad = datos.loc[articulo_buscar, 'Unidad']
        separador = ("-" * 65)
        print(Fore.GREEN + separador)
        print(Back.LIGHTGREEN_EX + Fore.BLUE + Style.BRIGHT + f"{'Código':^10} {'Descripción':^15} {'Categoría':^15} {'Stock':^8} {'Unidad':^8}")
        print(Fore.BLUE + f"{articulo_buscar:^10} {descripcion:^15} {categoria:^15} {stock:^8} {unidad:^8}")
        print(Fore.GREEN + separador)
        time.sleep(5)
        clear()
        menu()
    else:
        print(Fore.RED + "Producto no encontrado.")
        time.sleep(3)
        clear()
        menu()

def opcion_cuatro():
    articulo_salida = obtener_entrada("Por favor, indique el código del producto para salida de stock: \n", "CODIGO_SALIDA").strip().upper()
    if articulo_salida in datos.index:
        descripcion = datos.loc[articulo_salida, 'Descripcion']
        stock_actual = datos.loc[articulo_salida, 'Stock']
        print(f"Stock actual del producto {descripcion} ({articulo_salida}): {stock_actual}")
        cantidad_salida = int(obtener_entrada("Ingrese la cantidad que desea sacar: ", "CANTIDAD_SALIDA"))
        if cantidad_salida <= stock_actual:
            nuevo_stock = stock_actual - cantidad_salida
            datos.loc[articulo_salida, 'Stock'] = nuevo_stock
            guardar_datos_en_excel()
            print(Fore.GREEN + f"Salida de stock realizada. Nuevo stock: {nuevo_stock}")
            time.sleep(4)
            clear()
            menu()
        else:
            print(Fore.RED + "No hay suficiente stock para realizar la salida.")
            time.sleep(3)
            clear()
            menu()
    else:
        print(Fore.RED + "Producto no encontrado.")
        time.sleep(3)
        clear()
        menu()

def opcion_cinco():
    articulo_eliminar = obtener_entrada("Ingrese el código del artículo que desea eliminar: \n", "CODIGO_ELIMINAR").strip().upper()
    if articulo_eliminar in datos.index:
        datos.drop(articulo_eliminar, inplace=True)
        guardar_datos_en_excel()
        print(Fore.GREEN + "Artículo eliminado exitosamente.")
        time.sleep(4)
        clear()
        menu()
    else:
        print(Fore.RED + "Producto no encontrado.")
        time.sleep(3)
        clear()
        menu()

def opcion_siete():
    clear()
    print(Fore.YELLOW + "¡Gracias por usar el sistema de inventario!")
    time.sleep(2)
    clear()

def guardar_datos_en_excel():
    try:
        with ExcelWriter("Base de datos.xlsx") as writer:
            datos.to_excel(writer, sheet_name='Hoja1')
    except Exception as e:
        print(Fore.RED + f"Error al guardar el archivo Excel: {e}")

# Arreglar visualización con encabezados para mostrar siempre
datos_con_encabezado_ok = datos.copy()
datos_con_encabezado_ok.index.name = 'Código'

# Inicia el programa
if __name__ == "__main__":
    acceso_sistema()
