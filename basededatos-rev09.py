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

# -- Lista usuarios y contraseñas fijos para la demo (sin input) --
lista_usuarios= ["PEPE"]
lista_contrasenia= ["123"]

# Definir valores fijos para las "entradas" (simulando inputs)
VALORES_FIXTOS = {
    'OPCION_MENU': '6',  # solo para mostrar todos los datos
    'NUEVO_USUARIO': 'TESTUSER',
    'NUEVA_CONTRASENIA': 'testpass',
    'USUARIO': 'PEPE',
    'CONTRASENIA': '123',
    'ACCION': '0',  # iniciar sesión
    'CODIGO_ARTICULO': 'ABC123',
    'CANTIDAD_ACTUALIZAR': '10',
    'CONFIRMAR_OPERACION': 'S',
    'DESCRIPCION_NUEVO': 'PRODUCTO NUEVO',
    'CATEGORIA_NUEVO': 'GENERAL',
    'STOCK_NUEVO': '15',
    'UNIDAD_MEDIDA_NUEVO': 'UN',
    'CODIGO_CONSULTA': 'ABC123',
    'CODIGO_BUSCAR': 'ABC123',
    'CODIGO_SALIDA': 'ABC123',
    'CANTIDAD_SALIDA': '5',
    'CODIGO_ELIMINAR': 'ABC123',
}

def obtener_entrada(prompt, var_env):
    valor = VALORES_FIXTOS.get(var_env, "")
    print(Fore.BLUE + f"{prompt} {valor}")
    return valor

def menu():
    # Solo realiza opción 6 (ver todos) y luego salir
    print(Fore.CYAN + "-" * 30)
    print(Back.LIGHTCYAN_EX + Fore.GREEN + Style.BRIGHT + f"{'Menú de Inventario':^30}")
    print(Fore.CYAN + "-" * 30)
    print(Fore.CYAN +'6. Ver todos')
    print(Fore.CYAN +'7. Salir')
    print()

    opcion = obtener_entrada('Selecciona una opción: ', 'OPCION_MENU')

    if opcion == "6":
        print()
        print(datos_con_encabezado_ok)
        time.sleep(3)
        clear()
    elif opcion == "7":
        opcion_siete()

def nuevo_usuario():
    print(Fore.GREEN + "Función nuevo_usuario omitida en modo sin inputs.")

def usuario_existente():
    print(Fore.GREEN + "Simulando usuario existente con acceso correcto.")
    clear()
    menu()

def acceso_sistema():
    clear()
    print(Style.BRIGHT + Fore.CYAN + logo)
    print(Fore.BLUE + "-" * 30)
    print(Back.LIGHTGREEN_EX + Fore.BLUE + Style.BRIGHT + f"{'BIENVENIDO':^30}")
    print(Fore.BLUE + "-" * 30)
    ingreso_usuario = obtener_entrada("Ingrese [0] para iniciar sesión o [1] para crear una cuenta nueva: ", "ACCION")
    clear()
    if ingreso_usuario == "0":
        usuario_existente()
    elif ingreso_usuario == "1":
        nuevo_usuario()
    else:
        print(Fore.RED + "Opción inválida, finalizando.")
        return

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

