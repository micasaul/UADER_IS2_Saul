# -----------------------------------------------------------
# Copyright UADER FCyT-IS2©2024 - Todos los derechos reservados
# Este programa lee una clave desde la línea de comandos,
# busca su valor en un archivo JSON y lo imprime.
# Usa una estrategia de "Branching by Abstraction" para permitir
# alternar entre una versión simple y una refactorizada con Singleton.
# -----------------------------------------------------------

"""
Este módulo obtiene claves desde un archivo JSON usando una estructura con el patrón Singleton.
Copyright UADER FCyT-IS2©2024 todos los derechos reservados.
"""


import json
import sys
import os

# Constante de la versión
VERSION = "1.1"

# Constante que permite alternar entre versión original y refactorizada
NUEVO = True

# Versión ORIGINAL
def obtener_valor_original(clave):
    """
    Versión original del programa: abre el archivo JSON directamente y
    devuelve el valor asociado a la clave.
    """
    try:
        with open('sitedata.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            if clave in data:
                return data[clave]
            return f"⚠️ La clave '{clave}' no existe en el archivo."
    except Exception as e:
        return f"❌ Error al leer el archivo JSON: {e}"

# Versión REFACTORIZADA usando Singleton
class JSONLoaderSingleton:
    """
    Clase Singleton que carga y almacena el contenido del archivo JSON una sola vez.
    """
    _instance = None # Almacena la única instancia

    def __new__(cls, jsonfile='sitedata.json'):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_json(jsonfile)
        return cls._instance

    def _load_json(self, jsonfile):
        """
        Carga el archivo JSON y almacena su contenido.
        Finaliza con error controlado si no puede abrir o decodificar el archivo.
        """
        if not os.path.exists(jsonfile):
            print(f"❌ Error: El archivo '{jsonfile}' no existe.")
            sys.exit(1)
        try:
            with open(jsonfile, 'r', encoding='utf-8') as myfile:
                self._data = json.load(myfile)
        except json.JSONDecodeError:
            print(f"❌ Error: El archivo '{jsonfile}' no tiene formato JSON válido.")
            sys.exit(1)

    def get_value(self, key):
        """
        Devuelve el valor asociado a la clave dada.
        Si no existe, termina con error controlado.
        """
        if key not in self._data:
            print(f"⚠️ La clave '{key}' no existe en el archivo.")
            sys.exit(1)
        return self._data[key]

# Clase BRANCHING
class Branching:
    """
    Implementa la estrategia de 'Branching by Abstraction'.
    Decide si usar la versión original o la refactorizada con Singleton.
    """
    def __init__(self):
        if NUEVO:
            self.loader = JSONLoaderSingleton()

    def obtener_valor(self, clave):
        """
        Obtiene el valor de la clave utilizando la versión seleccionada.
        """
        if NUEVO:
            return self.loader.get_value(clave)
        return obtener_valor_original(clave)

# Función de validación de argumento
def validar_argumento(clave):
    """
    Valida que la clave ingresada sea una cadena no vacía.
    Termina con error controlado si no lo es.
    """
    if not isinstance(clave, str) or not clave.strip():
        print("❌ Error: El argumento proporcionado no es una clave válida.")
        sys.exit(1)

# Función MAIN
def main():
    """
    Función principal: maneja los argumentos de línea de comandos,
    valida la clave y muestra el valor correspondiente.
    """
    # Verifica si se pasó al menos un argumento
    if len(sys.argv) >= 2:
        clave = sys.argv[1]

        # Opción de versión
        if clave == "-v":
            print(f"getJason_branching.py - versión {VERSION}")
            sys.exit(0)

        # Ignora argumentos extra y lo informa
        if len(sys.argv) > 2:
            print(
                "ℹ️ Advertencia: Se proporcionaron argumentos adicionales. " \
                "Solo se usará el primero:", clave
            )
    else:
        # Si no se pasa argumento, se usa 'token1' por defecto
        clave = 'token1'

    # Validación del argumento
    validar_argumento(clave)

    # Crea la instancia de Branching y obtiene el valor solicitado
    branching = Branching()
    resultado = branching.obtener_valor(clave)
    print(resultado)

# Llamada al programa principal
if __name__ == "__main__":
    main()
